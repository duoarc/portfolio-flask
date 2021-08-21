import os
from app.resume import app

if __name__ == "__main__":
    app.secret_key = 'SECRET_KEY'
    app.run()
        