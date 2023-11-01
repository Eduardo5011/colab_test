"""empty message

Revision ID: c9f5581761ed
Revises: 
Create Date: 2023-11-01 17:42:36.519180

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c9f5581761ed'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('cuisine',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('restaurant',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('address', sa.String(), nullable=True),
    sa.Column('city', sa.String(), nullable=True),
    sa.Column('state', sa.String(), nullable=True),
    sa.Column('zip_code', sa.String(), nullable=True),
    sa.Column('latitude', sa.Float(), nullable=True),
    sa.Column('longitude', sa.Float(), nullable=True),
    sa.Column('average_rating', sa.Float(), nullable=True),
    sa.Column('review_count', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(), nullable=False),
    sa.Column('email', sa.String(), nullable=False),
    sa.Column('password', sa.String(), nullable=False),
    sa.Column('profile_picture', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('username')
    )
    op.create_table('friendship',
    sa.Column('user_id1', sa.Integer(), nullable=True),
    sa.Column('user_id2', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_id1'], ['user.id'], ),
    sa.ForeignKeyConstraint(['user_id2'], ['user.id'], )
    )
    op.create_table('restaurant_cuisines',
    sa.Column('restaurant_id', sa.Integer(), nullable=False),
    sa.Column('cuisine_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['cuisine_id'], ['cuisine.id'], ),
    sa.ForeignKeyConstraint(['restaurant_id'], ['restaurant.id'], ),
    sa.PrimaryKeyConstraint('restaurant_id', 'cuisine_id')
    )
    op.create_table('review',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('comment', sa.String(), nullable=False),
    sa.Column('rating', sa.Integer(), nullable=False),
    sa.Column('date', sa.DateTime(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('restaurant_id', sa.Integer(), nullable=False),
    sa.Column('cuisine_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['cuisine_id'], ['cuisine.id'], ),
    sa.ForeignKeyConstraint(['restaurant_id'], ['restaurant.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('review')
    op.drop_table('restaurant_cuisines')
    op.drop_table('friendship')
    op.drop_table('user')
    op.drop_table('restaurant')
    op.drop_table('cuisine')
    # ### end Alembic commands ###
