"""fix password1

Revision ID: d8de2009fd8c
Revises: 1aa22ae41491
Create Date: 2023-12-15 15:36:21.061075

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd8de2009fd8c'
down_revision = '1aa22ae41491'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('test', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'test')
    # ### end Alembic commands ###