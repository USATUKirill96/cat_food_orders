from flask_admin.contrib.sqla import ModelView


class ItemView(ModelView):
    can_delete = True
    can_edit = True
