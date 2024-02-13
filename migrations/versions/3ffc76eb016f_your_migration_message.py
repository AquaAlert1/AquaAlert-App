"""Your migration message

Revision ID: 3ffc76eb016f
Revises: 
Create Date: 2024-01-31 09:57:10.687456

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3ffc76eb016f'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=20), nullable=False),
    sa.Column('password', sa.String(length=60), nullable=False),
    sa.Column('place', sa.String(length=50), nullable=False),
    sa.Column('phone_number', sa.String(length=15), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('username')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user')
    # ### end Alembic commands ###
