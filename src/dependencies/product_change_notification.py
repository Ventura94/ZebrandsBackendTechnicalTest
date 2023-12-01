from typing import Iterable

from fastapi import BackgroundTasks, Depends
from fastapi_mail import MessageSchema, FastMail, MessageType
from sqlalchemy.orm import Session

from src.configs.email import email_config
from src.dependencies.db_session import get_db
from src.models import UserModel


class ProductChangeNotificationBackground:
    def __init__(self,
                 background_tasks: BackgroundTasks,
                 session: Session = Depends(get_db), ):
        self.background_tasks = background_tasks
        self.session = session
        self.fast_mail = FastMail(email_config)

    def get_users(self) -> Iterable[UserModel]:
        for user in self.session.query(UserModel).yield_per(1):
            yield user

    async def notificate(self, message: str):
        for user in self.get_users():
            message_schema = MessageSchema(
                subject="Zebrants Product Change",
                recipients=[user.email],
                body=message,
                subtype=MessageType.plain
            )
            await self.fast_mail.send_message(message_schema)

    def notificate_in_background(self, message: str):
        self.background_tasks.add_task(self.notificate, message)
