from flask_admin.contrib.sqla import ModelView


class OrderView(ModelView):
    can_delete = True
    can_edit = True
