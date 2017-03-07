"""updated modules table to include is_active

Revision ID: 51f6f82e2af8
Revises: 243d0f8552d8
Create Date: 2017-03-07 16:48:46.237350

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '51f6f82e2af8'
down_revision = '243d0f8552d8'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('modules', sa.Column('is_active', sa.Boolean(), nullable=False))
    op.add_column('modules', sa.Column('subtitle', sa.String(length=50), nullable=True))
    op.add_column('modules', sa.Column('title', sa.String(length=50), nullable=True))
    op.alter_column('modules', 'type',
                    existing_type=postgresql.ENUM('featured', 'then', 'now', 'event', name='module_type'),
                    nullable=False)
    op.drop_column('modules', 'title2')
    op.drop_column('modules', 'title1')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('modules', sa.Column('title1', sa.VARCHAR(length=50), autoincrement=False, nullable=True))
    op.add_column('modules', sa.Column('title2', sa.VARCHAR(length=50), autoincrement=False, nullable=True))
    op.alter_column('modules', 'type',
                    existing_type=postgresql.ENUM('featured', 'then', 'now', 'event', name='module_type'),
                    nullable=True)
    op.drop_column('modules', 'title')
    op.drop_column('modules', 'subtitle')
    op.drop_column('modules', 'is_active')
    # ### end Alembic commands ###
