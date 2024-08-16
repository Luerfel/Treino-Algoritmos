from flask import Flask
from bd import Carros

app = Flask(__name__)

def get_carros():
    return Carros

app.run()