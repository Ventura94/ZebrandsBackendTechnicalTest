from src.forms.product_forms import ProductCreateForm, ProductUpdateForm
from src.querys.product_query import ProductQuery
from src.routes.base_routes import create_router
from src.services.product_service import ProductService
from src.shemas.product_schema import ProductSchema

router = create_router(
    schema=ProductSchema,
    service=ProductService,
    query=ProductQuery,
    create_form=ProductCreateForm,
    update_form=ProductUpdateForm,
    prefix="/products",
    tags=["Product"],
)
