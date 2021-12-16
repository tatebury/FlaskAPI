"""empty message

Revision ID: 2ffe3e9366c5
Revises: 1a152c7b1378
Create Date: 2021-12-15 16:11:30.956238

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2ffe3e9366c5'
down_revision = '1a152c7b1378'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('edit', sa.Integer(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'edit')
    # ### end Alembic commands ###