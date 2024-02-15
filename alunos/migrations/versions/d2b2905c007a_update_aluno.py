"""update aluno

Revision ID: d2b2905c007a
Revises: 946bb671922e
Create Date: 2023-12-11 09:41:45.039598

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'd2b2905c007a'
down_revision = '946bb671922e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('aluno', schema=None) as batch_op:
        batch_op.alter_column('pasta_id',
               existing_type=mysql.INTEGER(),
               type_=sa.Text(),
               existing_nullable=True)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('aluno', schema=None) as batch_op:
        batch_op.alter_column('pasta_id',
               existing_type=sa.Text(),
               type_=mysql.INTEGER(),
               existing_nullable=True)

    # ### end Alembic commands ###