from src.forms.user_forms import UserCreateForm, UserUpdateForm
from src.querys.user_query import UserQuery
from src.routes.base_routes import create_router
from src.services.user_service import UserService
from src.shemas.user_schema import UserSchema

router = create_router(
    schema=UserSchema,
    service=UserService,
    query=UserQuery,
    create_form=UserCreateForm,
    update_form=UserUpdateForm,
    prefix="/user",
    tags=["User"],
)
