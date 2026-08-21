import os

from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from app.forms import *

router = APIRouter()

templates_dir = os.path.join(
    os.path.dirname(os.path.dirname(__file__)), 'templates'
)
templates = Jinja2Templates(directory=templates_dir)
templates.env.globals['get_flashed_messages'] = lambda *args, **kwargs: []


@router.get('/', name='home', response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse(
        request, 'pages/placeholder.home.html'
    )


@router.get('/about', name='about', response_class=HTMLResponse)
def about(request: Request):
    return templates.TemplateResponse(
        request, 'pages/placeholder.about.html'
    )


@router.get('/login', name='login', response_class=HTMLResponse)
def login(request: Request):
    form = LoginForm()
    return templates.TemplateResponse(
        request, 'forms/login.html', {'form': form}
    )


@router.get('/register', name='register', response_class=HTMLResponse)
def register(request: Request):
    form = RegisterForm()
    return templates.TemplateResponse(
        request, 'forms/register.html', {'form': form}
    )


@router.get('/forgot', name='forgot', response_class=HTMLResponse)
def forgot(request: Request):
    form = ForgotForm()
    return templates.TemplateResponse(
        request, 'forms/forgot.html', {'form': form}
    )
