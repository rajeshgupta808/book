"""create book table

Revision ID: dfbeba5caf13
Revises: 
Create Date: 2022-03-21 16:52:41.891810

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'dfbeba5caf13'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'book2',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('title', sa.String(50), nullable=False),
        sa.Column('description', sa.Unicode(200)),
    )
def downgrade():
    pass
