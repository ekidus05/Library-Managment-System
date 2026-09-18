"""create borrowings table

Revision ID: dc33b0fead06
Revises: 0f21c1eb72db
Create Date: 2026-09-13 18:20:55.916846

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'dc33b0fead06'
down_revision: Union[str, Sequence[str], None] = '0f21c1eb72db'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None

def upgrade() -> None:
    op.drop_table('borrowings')  # remove the half-migrated table
    op.create_table(
        'borrowings',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('user_id', sa.Integer(), nullable=False),
        sa.Column('book_id', sa.Integer(), nullable=False),
        sa.Column('borrow_date', sa.DateTime(), nullable=False),
        sa.Column('due_date', sa.DateTime(), nullable=False),
        sa.Column('return_date', sa.DateTime(), nullable=True),
        sa.Column('status', sa.String(), nullable=False),
        sa.ForeignKeyConstraint(['user_id'], ['users.id']),
        sa.ForeignKeyConstraint(['book_id'], ['books.id']),
        sa.PrimaryKeyConstraint('id'),
    )
    op.create_index(op.f('ix_borrowings_id'), 'borrowings', ['id'], unique=False)


def downgrade() -> None:
    op.drop_index(op.f('ix_borrowings_id'), table_name='borrowings')
    op.drop_table('borrowings')
