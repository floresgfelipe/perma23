"""participantes tabla

Revision ID: 531c96026156
Revises: fd1fde8a0104
Create Date: 2023-08-16 10:52:10.490692

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '531c96026156'
down_revision = 'fd1fde8a0104'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('participante',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nombres', sa.String(length=50), nullable=False),
    sa.Column('apellido_p', sa.String(length=50), nullable=False),
    sa.Column('apellido_m', sa.String(length=50), nullable=False),
    sa.Column('sexo', sa.String(length=20), nullable=False),
    sa.Column('telefono', sa.String(length=10), nullable=False),
    sa.Column('servicio', sa.String(length=20), nullable=False),
    sa.Column('coordinador', sa.String(length=2), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('participante')
    # ### end Alembic commands ###