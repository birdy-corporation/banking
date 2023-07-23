#!/bin/env python3

import json
from dataclasses import dataclass
from flask import Flask
from nacl.secret import SecretBox

app = Flask(__name__)


@dataclass
class Drink:
    """Define drinks"""
    name: str
    description: str
    recipie: str
    price: float 

class DrinkEncoder(json.JSONEncoder):
    '''Class serializable encoder.'''
    def default(self, o):
        return o.__dict__


data = { 'drinks': [] } 

data["drinks"].append(Drink(name="Grape",
                            description="Delicious grape fruit drink",
                            recipie="2 grapes, 1/2 milk cup, 1/2 vodka",
                            price=13.10 ))

data["drinks"].append(Drink(name="Lemon",
                            description="A mojito lemon undiluted drink",
                            recipie="1 lemon, 3 scoops of sugar, 1 spoon of " + 
                                "condensed milk grapes, 1/2 cup of aguardente",
                            price=7.89 ))

data["drinks"].append(Drink(name="Mango",
                            description="A non-alchoolic mango drink",
                            recipie="1 mango, 3/4 milk, 1/4 condensed milk, ice cubes",
                            price=8.19 ))

@app.route("/")
def index():
        return "Drinks API"

@app.route('/drinks', methods = ['GET'])
def get_drinks():
    response = app.response_class(
        response=json.dumps(data, cls=DrinkEncoder, indent=4),
        mimetype='application/json'
    )
    return response


if __name__ == "__main__":
    app.debug = True
    app.run()
