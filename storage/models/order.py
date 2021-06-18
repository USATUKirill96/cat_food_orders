import datetime

from storage import database as db


class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.DateTime, default=datetime.datetime.now())
    user_id = db.Column(db.Integer)
    payed = db.Column(db.Boolean)
    status = db.Column(db.String(64))

    def __repr__(self):
        return str(self.id)
