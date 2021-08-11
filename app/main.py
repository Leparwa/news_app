from flask import Flask

# Initializing app
app = Flask(__name__)

from app.views import views


# if __name__ == "__main__":
#     app.run(debug=True)
