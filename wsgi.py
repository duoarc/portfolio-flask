import os
from app.resume import app

if __name__ == "__main__":
        app.run()
        app.secret_key = os.environ.get('SECRET_KEY')