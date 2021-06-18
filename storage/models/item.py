from storage import database as db


class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    quantity = db.Column(db.Integer)

    detail_id = db.Column(db.Integer, db.ForeignKey("detail.id"), nullable=False)
    detail = db.relationship("Detail", backref="item_set")

    order_id = db.Column(db.Integer, db.ForeignKey("order.id"), nullable=False)
    order = db.relationship("Order", backref=db.backref("items"))

    def __repr__(self):
        return f"order {self.order}, item {self.id}"
