from pyramid.config import Configurator

import os


def home(context, request):
    """Default Home view. Should be overwritten by an app."""
    response = """
Request info:
    request.client_addr: {request.client_addr}
    request.remote_addr: {request.remote_addr}
    request.environ['REMOTE_ADDR']: {REMOTE_ADDR}
    request.headers['X-Forwarded-For']: {X_Forwarded_For}

    """.format(
        request=request,
        REMOTE_ADDR=request.environ['REMOTE_ADDR'],
        X_Forwarded_For=request.headers.get('X-Forwarded-For', 'Not set'),
    )

    return response


def main(global_config, **settings):
    """Return a Pyramid WSGI application."""

    config = Configurator(settings=settings)

    config.add_view('ips.home', renderer='string')
    return config.make_wsgi_app()
