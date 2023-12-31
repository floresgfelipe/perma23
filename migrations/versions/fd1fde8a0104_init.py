"""Init

Revision ID: fd1fde8a0104
Revises: 
Create Date: 2023-08-13 21:15:43.936340

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'fd1fde8a0104'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('alumno',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nombres', sa.String(length=50), nullable=False),
    sa.Column('apellido_p', sa.String(length=50), nullable=False),
    sa.Column('apellido_m', sa.String(length=50), nullable=False),
    sa.Column('dia_nac', sa.Integer(), nullable=False),
    sa.Column('mes_nac', sa.String(length=20), nullable=False),
    sa.Column('año_nac', sa.Integer(), nullable=False),
    sa.Column('decanato', sa.String(length=50), nullable=False),
    sa.Column('parroquia', sa.String(length=80), nullable=False),
    sa.Column('telefono', sa.String(length=10), nullable=False),
    sa.Column('correo', sa.String(length=50), nullable=False),
    sa.Column('foto', sa.String(length=200), nullable=False),
    sa.Column('grado', sa.Integer(), nullable=False),
    sa.Column('modalidad', sa.Integer(), nullable=False),
    sa.Column('boleta_carta', sa.String(length=200), nullable=False),
    sa.Column('servicio', sa.String(length=2), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('alumno')
    # ### end Alembic commands ###
