from flask_admin.contrib.sqla import ModelView


class DetailView(ModelView):
    can_delete = True
    can_edit = True
