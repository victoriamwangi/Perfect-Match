"""empty message

Revision ID: 21c7edd79b6d
Revises: 1a64ab0208a2
Create Date: 2022-05-19 11:49:58.189904

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '21c7edd79b6d'
down_revision = '1a64ab0208a2'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('images',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=50), nullable=False),
    sa.Column('uploader_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['uploader_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('images')
    # ### end Alembic commands ###