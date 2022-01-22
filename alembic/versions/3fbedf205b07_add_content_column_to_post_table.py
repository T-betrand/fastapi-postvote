"""add content column to post table

Revision ID: 3fbedf205b07
Revises: ec8c82898b79
Create Date: 2022-01-20 16:21:14.020911

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3fbedf205b07'
down_revision = 'ec8c82898b79'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade():
    op.drop_column('posts', 'content')
    pass
