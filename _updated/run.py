import os

from app import create_app

app = create_app('config.development')

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host='127.0.0.1', port=int(os.environ.get('PORT', 5000)))
