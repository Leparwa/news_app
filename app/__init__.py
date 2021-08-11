from flask import Flask
from .config import DevConfig

# Initializing app
app = Flask(__name__, instance_relative_config = True)

# Setting up configuration
app.config.from_pyfile('config.py')
app.config.from_object(DevConfig)


from app.views import views


# if __name__ == "__main__":
#     app.run(debug=True)
