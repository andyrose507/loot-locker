from sqlalchemy.sql import func

from .db import db, environment, SCHEMA, add_prefix_for_prod

class Category(db.Model):
    __tablename__ = 'categories'

    if environment == "production":
        __table_args__ = {'schema': SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), nullable=False)

    items = db.relationship('Item', back_populates='category')

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name
        }
