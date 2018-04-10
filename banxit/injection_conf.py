# In the Injector world, all dependency configuration and initialization is
# performed in modules (http://packages.python.org/injector/#module) The
# same is true with Flask-Injector. You can see some examples of configuring
# Flask extensions through modules below.

# Accordingly, the next step is to create modules for any objects we want made
# available to the application. Note that in this example we also use the
# Injector to gain access to the `flask.Config`:


from flask_injector import request
from injector import Module

from sqlalchemy.orm import scoped_session


class AppModule(Module):
    def __init__(self, app):
        self.app = app

    """Configure the application."""
    def configure(self, binder):
        # We configure the DB here, explicitly, as Flask-SQLAlchemy requires
        # the DB to be configured before request handlers are called.
        from repositories import db_session
        binder.bind(scoped_session, to=db_session, scope=request)
