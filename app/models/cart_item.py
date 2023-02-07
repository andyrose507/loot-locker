from sqlalchemy import PrimaryKeyConstraint
from sqlalchemy.sql import func

from .db import db, environment, SCHEMA, add_prefix_for_prod


class CartItem(db.Model):
    __tablename__ = 'cart_items'

    if environment == "production":
        __table_args__ = {'schema': SCHEMA}

    user_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod('users.id')), nullable=False)
    item_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod('items.id')), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    created_at = db.Column(db.DateTime, server_default=func.now(), nullable=False)
    updated_at = db.Column(db.DateTime, server_default=func.now(), onupdate=func.now(), nullable=False)

    __table_args__ = (
        PrimaryKeyConstraint(user_id, item_id, name='user_cart_item_pk'),
    )

    item = db.relationship('Item')

    def to_dict(self):
        return {
            'item': self.item.to_dict(),
            'quantity': self.quantity,
            'createdAt': self.created_at,
            'updatedAt': self.updated_at,
        }
