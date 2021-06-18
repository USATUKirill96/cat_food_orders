from . import settings


def load_config(app):
    app.config.from_object(settings)
    return app
