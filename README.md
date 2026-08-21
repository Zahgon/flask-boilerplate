[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)

## Welcome

Hello. Want to get started with FastAPI quickly? Good. You came to the right place. This application framework is pre-configured with **SQLAlchemy**, **WTForms**, **Jinja2**, and the **Bootstrap** frontend (among others). This will get your FastAPI app up and running, locally or on a hosting platform, quickly. Use this starter/boilerplate for all your new FastAPI projects. Cheers!

<hr>

![real-python-logo](https://raw.githubusercontent.com/realpython/about/master/rp_small.png)

**Designed for the [Real Python](http://www.realpython.com) course.**

<hr>

**What is FastAPI?** FastAPI is a modern, high-performance web framework for building APIs and web apps with Python, built on top of [Starlette](https://www.starlette.io/) (ASGI) and [Pydantic](https://docs.pydantic.dev/). It is served by an ASGI server such as [Uvicorn](https://www.uvicorn.org/).

Project Structure
--------

  ```sh
  ├── Procfile
  ├── Procfile.dev
  ├── README.md
  ├── app.py
  ├── config.py
  ├── error.log
  ├── forms.py
  ├── models.py
  ├── requirements.txt
  ├── static
  │   ├── css
  │   ├── font
  │   ├── ico
  │   ├── img
  │   └── js
  └── templates
      ├── errors
      │   ├── 404.html
      │   └── 500.html
      ├── forms
      │   ├── forgot.html
      │   ├── login.html
      │   └── register.html
      ├── layouts
      │   ├── form.html
      │   └── main.html
      └── pages
          ├── placeholder.about.html
          └── placeholder.home.html
  ```

The application exposes five pages, all rendered from Jinja2 templates:

| Route       | Name       | Template                          |
| ----------- | ---------- | --------------------------------- |
| `/`         | `home`     | `pages/placeholder.home.html`     |
| `/about`    | `about`    | `pages/placeholder.about.html`    |
| `/login`    | `login`    | `forms/login.html`                |
| `/register` | `register` | `forms/register.html`             |
| `/forgot`   | `forgot`   | `forms/forgot.html`               |

### Screenshots

![Pages](https://github.com/realpython/flask-boilerplate/blob/master/screenshots/pages.png)

![Forms](https://github.com/realpython/flask-boilerplate/blob/master/screenshots/forms.png)


### Quick Start

1. Clone the repo:

  ```sh
  $ git clone https://github.com/realpython/flask-boilerplate.git
  $ cd flask-boilerplate
  ```

2. Create and activate a virtualenv:

  ```sh
  $ python3 -m venv .venv
  $ source .venv/bin/activate
  ```

3. Install the dependencies:

  ```sh
  $ pip install -r requirements.txt
  ```

4. Run the development server:

  ```sh
  $ python app.py
  ```

   or, with autoreload:

  ```sh
  $ uvicorn app:app --reload --port 5000
  ```

5. Navigate to [http://localhost:5000](http://localhost:5000)


### Deployment

FastAPI runs behind an ASGI server. For production, serve the app with Uvicorn
directly, or with Gunicorn using the Uvicorn worker class:

  ```sh
  $ uvicorn app:app --host 0.0.0.0 --port ${PORT:-5000}
  # or
  $ gunicorn app:app -k uvicorn.workers.UvicornWorker --bind 0.0.0.0:${PORT:-5000}
  ```

On a platform such as Heroku, the included `Procfile` already declares the web
process:

  ```
  web: uvicorn app:app --host 0.0.0.0 --port ${PORT:-5000}
  ```

### Provenance

This project was migrated to FastAPI from the original Flask boilerplate by
Real Python: <https://github.com/realpython/flask-boilerplate>. The public
behavior (routes, templates, forms, and static assets) is preserved.

### Learn More

1. [FastAPI Documentation](https://fastapi.tiangolo.com/)
2. [Starlette Documentation](https://www.starlette.io/)
3. [Uvicorn Documentation](https://www.uvicorn.org/)
4. [Real Python](http://www.realpython.com) :)
