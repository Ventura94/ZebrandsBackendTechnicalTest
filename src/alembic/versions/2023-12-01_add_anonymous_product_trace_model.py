"""add anonymous product trace model

Revision ID: 7ffb6fd1edcf
Revises: d0728ec0f375
Create Date: 2023-12-01 12:45:14.496494

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7ffb6fd1edcf'
down_revision = 'd0728ec0f375'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('anonymous_products_trace',
    sa.Column('anonymous_user_uuid', sa.UUID(), nullable=False),
    sa.Column('ip_address', sa.String(), nullable=False),
    sa.Column('operating_system', sa.String(), nullable=False),
    sa.Column('explorer', sa.String(), nullable=False),
    sa.Column('device', sa.String(), nullable=False),
    sa.Column('product_uuid', sa.UUID(), nullable=True),
    sa.Column('uuid', sa.UUID(), nullable=False),
    sa.ForeignKeyConstraint(['product_uuid'], ['products.uuid'], ),
    sa.PrimaryKeyConstraint('uuid')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('anonymous_products_trace')
    # ### end Alembic commands ###
