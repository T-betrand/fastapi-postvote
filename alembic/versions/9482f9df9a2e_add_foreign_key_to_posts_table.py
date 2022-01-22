"""add foreign-key to posts table

Revision ID: 9482f9df9a2e
Revises: e309794fb412
Create Date: 2022-01-20 20:49:38.115041

"""

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9482f9df9a2e'
down_revision = 'e309794fb412'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column('owner_id', sa.Integer(), nullable=False))
    op.create_foreign_key('post_user_fk', source_table="posts", referent_table="users", local_cols=['owner_id'], remote_cols=['id'], ondelete="CASCADE")
    pass


def downgrade():
    op.drop_constraint('post_users_fk', table_name="posts")
    op.drop_column('posts', 'owner_id')
    pass
