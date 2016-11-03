from app import app

if __name__ == '__main__':
    #Para desplegar la aplicación con gunicorn:
    # gunicorn -b 0.0.0.0:80 wsgi:app
    app.run()
