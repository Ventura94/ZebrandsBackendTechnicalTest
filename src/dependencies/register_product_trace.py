from uuid import UUID

from fastapi import Depends, Request, BackgroundTasks
from sqlalchemy.orm import Session
from user_agents import parse

from src.dependencies.anonymous_user_cookie import AnonymousUserCookieDependency
from src.dependencies.db_session import get_db
from src.models import AnonymousProductTraceModel

anonymous_user_cookie = AnonymousUserCookieDependency(cookie_key="zebrands_products")


class AnonymousProductTraceBackground:
    def __init__(
        self,
        background_tasks: BackgroundTasks,
        request: Request,
        session: Session = Depends(get_db),
        anonymous_user: UUID = Depends(anonymous_user_cookie),
    ):
        self.background_tasks = background_tasks
        self.request = request
        self.session = session
        self.anonymous_user = anonymous_user

    def trace_product(self, product_uuid: UUID) -> AnonymousProductTraceModel:
        user_agent = parse(self.request.headers.get("user-agent"))
        new_instance = AnonymousProductTraceModel(
            anonymous_user_uuid=self.anonymous_user,
            ip_address=self.request.headers.get("X-Real-IP", "Unknown"),
            operating_system=user_agent.os.family,
            explorer=user_agent.browser.family,
            device=user_agent.device.family,
            product_uuid=product_uuid,
        )
        self.session.add(new_instance)
        self.session.flush()
        self.session.refresh(new_instance)
        return new_instance

    def trace_product_in_background(self, product_uuid: UUID):
        self.background_tasks.add_task(self.trace_product, product_uuid)
