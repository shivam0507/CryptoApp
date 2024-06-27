import flask
from flask import Flask




if __name__ == "__main__":
    app = Flask("Crypto App")
    app.run(port=8080)