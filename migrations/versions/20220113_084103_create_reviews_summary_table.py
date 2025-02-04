"""Create reviews summary table

Revision ID: b13a7672fefe
Revises: f430ff5a4160
Create Date: 2022-01-13 08:41:03.067753

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

import os
environment = os.getenv("FLASK_ENV")
SCHEMA = os.environ.get("SCHEMA")

# revision identifiers, used by Alembic.
revision = 'b13a7672fefe'
down_revision = 'f430ff5a4160'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('review_summaries',
        sa.Column('item_id', sa.Integer(), nullable=False),
        sa.Column('num_of_reviews', sa.Integer(), nullable=False),
        sa.Column('ratings_total', sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(['item_id'], ['items.id'], ),
        sa.PrimaryKeyConstraint('item_id')
    )

    if environment == "production":
        op.execute(f"ALTER TABLE review_summaries SET SCHEMA {SCHEMA};")
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('review_summaries')
    # ### end Alembic commands ###
