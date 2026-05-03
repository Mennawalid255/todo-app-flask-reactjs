"""add permission overrides to users

Revision ID: e6f7a1c2d9b0
Revises: d4c6b6f0b8a1
Create Date: 2026-05-03 22:20:00.000000

"""
from alembic import op
import sqlalchemy as sa


revision = "e6f7a1c2d9b0"
down_revision = "d4c6b6f0b8a1"
branch_labels = None
depends_on = None


def upgrade():
    with op.batch_alter_table("users", schema=None) as batch_op:
        batch_op.add_column(
            sa.Column(
                "permission_overrides",
                sa.Text(),
                nullable=False,
                server_default='{"grants": [], "revokes": []}',
            )
        )

    with op.batch_alter_table("users", schema=None) as batch_op:
        batch_op.alter_column("permission_overrides", server_default=None)


def downgrade():
    with op.batch_alter_table("users", schema=None) as batch_op:
        batch_op.drop_column("permission_overrides")
