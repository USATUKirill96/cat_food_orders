from flask_admin import Admin

from storage import database as db
from storage.models import Detail, Item, Order

from .detail import DetailView
from .item import ItemView
from .order import OrderView

admin = Admin(name="Cat food", template_mode="bootstrap4")

admin.add_view(ItemView(Item, db.session))
admin.add_view(ItemView(Detail, db.session))
admin.add_view(ItemView(Order, db.session))


def init_admin(app):
    admin.init_app(app)

    return app
