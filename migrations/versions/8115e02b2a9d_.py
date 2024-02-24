"""empty message

Revision ID: 8115e02b2a9d
Revises: e7a5c202cb4e
Create Date: 2024-02-18 19:50:21.104115

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '8115e02b2a9d'
down_revision: Union[str, None] = 'e7a5c202cb4e'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
