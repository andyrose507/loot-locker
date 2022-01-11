"""create reviews table, add reviews to items, add some nullables

Revision ID: c483df68ec17
Revises: 10dc889f1ea4
Create Date: 2022-01-11 13:38:19.314279

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = "c483df68ec17"
down_revision = "10dc889f1ea4"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "reviews",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("user_id", sa.Integer(), nullable=True),
        sa.Column("item_id", sa.Integer(), nullable=False),
        sa.Column("rating", sa.Integer(), nullable=False),
        sa.Column("comment", sa.Text(), nullable=False),
        sa.Column(
            "created_at", sa.DateTime(), server_default=sa.text("now()"), nullable=True
        ),
        sa.Column(
            "updated_at", sa.DateTime(), server_default=sa.text("now()"), nullable=True
        ),
        sa.ForeignKeyConstraint(
            ["user_id"],
            ["users.id"],
        ),
        sa.ForeignKeyConstraint(
            ["item_id"],
            ["items.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
    )

    op.alter_column(
        "cart_items",
        "created_at",
        existing_type=postgresql.TIMESTAMP(),
        nullable=False,
        existing_server_default=sa.text("now()"),
    )
    op.alter_column(
        "cart_items",
        "updated_at",
        existing_type=postgresql.TIMESTAMP(),
        nullable=False,
        existing_server_default=sa.text("now()"),
    )
    op.alter_column("items", "user_id", existing_type=sa.INTEGER(), nullable=False)
    op.alter_column(
        "items",
        "created_at",
        existing_type=postgresql.TIMESTAMP(),
        nullable=False,
        existing_server_default=sa.text("now()"),
    )
    op.alter_column(
        "items",
        "updated_at",
        existing_type=postgresql.TIMESTAMP(),
        nullable=False,
        existing_server_default=sa.text("now()"),
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("reviews")

    op.alter_column(
        "items",
        "updated_at",
        existing_type=postgresql.TIMESTAMP(),
        existing_server_default=sa.text("now()"),
    )
    op.alter_column(
        "items",
        "created_at",
        existing_type=postgresql.TIMESTAMP(),
        existing_server_default=sa.text("now()"),
    )
    op.alter_column(
        "items",
        "user_id",
        existing_type=sa.INTEGER(),
    )
    op.alter_column(
        "cart_items",
        "updated_at",
        existing_type=postgresql.TIMESTAMP(),
        existing_server_default=sa.text("now()"),
    )
    op.alter_column(
        "cart_items",
        "created_at",
        existing_type=postgresql.TIMESTAMP(),
        existing_server_default=sa.text("now()"),
    )
    # ### end Alembic commands ###
