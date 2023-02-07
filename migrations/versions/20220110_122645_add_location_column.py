"""add location column

Revision ID: 10dc889f1ea4
Revises: 75375e9458ab
Create Date: 2022-01-10 12:26:45.173503

"""
from alembic import op
import sqlalchemy as sa

import os
environment = os.getenv("FLASK_ENV")
SCHEMA = os.environ.get("SCHEMA")


# revision identifiers, used by Alembic.
revision = '10dc889f1ea4'
down_revision = '75375e9458ab'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('location', sa.String(length=40), nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'location')
    # ### end Alembic commands ###
