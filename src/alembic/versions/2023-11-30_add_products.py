"""add products

Revision ID: 7013fd78a8e1
Revises: 3bb35615b9bf
Create Date: 2023-11-30 16:01:14.434315

"""
import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = "7013fd78a8e1"
down_revision = "3bb35615b9bf"
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "products",
        sa.Column("sku", sa.String(), nullable=False),
        sa.Column("name", sa.String(), nullable=False),
        sa.Column("price", sa.DECIMAL(), nullable=False),
        sa.Column("brand", sa.String(), nullable=False),
        sa.Column("create_at", sa.DateTime(), nullable=False),
        sa.Column("is_delete", sa.Boolean(), nullable=False),
        sa.Column("delete_at", sa.DateTime(), nullable=True),
        sa.Column("uuid", sa.UUID(), nullable=False),
        sa.PrimaryKeyConstraint("uuid"),
        sa.UniqueConstraint("sku"),
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("products")
    # ### end Alembic commands ###
