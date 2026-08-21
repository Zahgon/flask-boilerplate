#----------------------------------------------------------------------------#
# Imports
#----------------------------------------------------------------------------#

import os
import logging
from logging import Formatter, FileHandler

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

import config
from forms import *

#----------------------------------------------------------------------------#
# App Config.
#----------------------------------------------------------------------------#

basedir = os.path.abspath(os.path.dirname(__file__))

app = FastAPI(debug=config.DEBUG)
#db = SQLAlchemy(app)

templates = Jinja2Templates(directory=os.path.join(basedir, 'templates'))
# The shared templates call ``get_flashed_messages``. FastAPI has no
# flash-message machinery and no route sets one, so expose a no-op global
# to keep the shared templates rendering unchanged.
templates.env.globals['get_flashed_messages'] = lambda *args, **kwargs: []

app.mount(
    '/static',
    StaticFiles(directory=os.path.join(basedir, 'static')),
    name='static',
)

# Automatically tear down SQLAlchemy.
'''
@app.teardown_request
def shutdown_session(exception=None):
    db_session.remove()
'''

# Login required decorator.
'''
def login_required(test):
    @wraps(test)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return test(*args, **kwargs)
        else:
            flash('You need to login first.')
            return redirect(url_for('login'))
    return wrap
'''
#----------------------------------------------------------------------------#
# Controllers.
#----------------------------------------------------------------------------#


@app.get('/', name='home', response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse(request, 'pages/placeholder.home.html')


@app.get('/about', name='about', response_class=HTMLResponse)
def about(request: Request):
    return templates.TemplateResponse(request, 'pages/placeholder.about.html')


@app.get('/login', name='login', response_class=HTMLResponse)
def login(request: Request):
    form = LoginForm()
    return templates.TemplateResponse(request, 'forms/login.html', {'form': form})


@app.get('/register', name='register', response_class=HTMLResponse)
def register(request: Request):
    form = RegisterForm()
    return templates.TemplateResponse(request, 'forms/register.html', {'form': form})


@app.get('/forgot', name='forgot', response_class=HTMLResponse)
def forgot(request: Request):
    form = ForgotForm()
    return templates.TemplateResponse(request, 'forms/forgot.html', {'form': form})

# Error handlers.


@app.exception_handler(500)
def internal_error(request: Request, error):
    #db_session.rollback()
    return templates.TemplateResponse(request, 'errors/500.html', status_code=500)


@app.exception_handler(404)
def not_found_error(request: Request, error):
    return templates.TemplateResponse(request, 'errors/404.html', status_code=404)

if not config.DEBUG:
    file_handler = FileHandler('error.log')
    file_handler.setFormatter(
        Formatter('%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]')
    )
    logger = logging.getLogger('uvicorn.error')
    logger.setLevel(logging.INFO)
    file_handler.setLevel(logging.INFO)
    logger.addHandler(file_handler)
    logger.info('errors')

#----------------------------------------------------------------------------#
# Launch.
#----------------------------------------------------------------------------#

# Default port:
if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host='127.0.0.1', port=int(os.environ.get('PORT', 5000)))

# Or specify port manually:
'''
if __name__ == '__main__':
    import uvicorn
    port = int(os.environ.get('PORT', 5000))
    uvicorn.run(app, host='0.0.0.0', port=port)
'''
