"""fix password2

Revision ID: afee0371f2f7
Revises: d8de2009fd8c
Create Date: 2023-12-15 15:38:08.120496

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'afee0371f2f7'
down_revision = 'd8de2009fd8c'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'password')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('password', sa.VARCHAR(length=50), autoincrement=False, nullable=False))
    # ### end Alembic commands ###
