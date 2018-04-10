import connexion
from flask_swagger_ui import get_swaggerui_blueprint

from banxit.app.extensions import db
from banxit import encoder


def create_app():
    connexion_app = connexion.FlaskApp(__name__, specification_dir='../..')
    app = connexion_app.app
    # app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'  # TODO: 'sqlite:////tmp/test.db'
    app.json_encoder = encoder.JSONEncoder
    register_extensions(app)

    # Must be done last because Connexion loads your controller, loading all their dependencies, which results in
    #  all of your project loaded before you have initialised all extensions
    connexion_app.add_api('swagger.yaml', arguments={'title': 'Sample Application Flow OAuth2 Project'})
    register_swagger_ui(app)
    return app


def register_extensions(app):
    db.init_app(app)
    db.create_all(app=app)


def register_swagger_ui(app):
    SWAGGER_URL = '/api/docs'  # URL for exposing Swagger UI (without trailing '/')
    API_URL = 'http://localhost:8080/condensat/banxit/1.0.2/swagger.json'  # Our API url (can of course be a local resource)

    # Call factory function to create our blueprint
    swaggerui_blueprint = get_swaggerui_blueprint(
        SWAGGER_URL,  # Swagger UI static files will be mapped to '{SWAGGER_URL}/dist/'
        API_URL,
        config={  # Swagger UI config overrides
            'app_name': "Test application"
        },
        # oauth_config={  # OAuth config. See https://github.com/swagger-api/swagger-ui#oauth2-configuration .
        #    'clientId': "your-client-id",
        #    'clientSecret': "your-client-secret-if-required",
        #    'realm': "your-realms",
        #    'appName': "your-app-name",
        #    'scopeSeparator': " ",
        #    'additionalQueryStringParams': {'test': "hello"}
        # }
    )
    app.register_blueprint(swaggerui_blueprint, url_prefix=SWAGGER_URL)

# Initialize Flask-Injector. This needs to be run *after* you attached all
# views, handlers, context processors and template globals.

# FlaskInjector(app=app, modules=[injection_configuration])
