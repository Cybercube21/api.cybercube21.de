from flask import Flask
from flask_restful import Resource, Api, reqparse
import pandas as pd
import ast
import os, random

app = Flask(__name__)
api = Api(app)
file_list=os.listdir(r"../memes/")

class Memes(Resource):
    def get(self):
        meme = random.choice(file_list)
        return {'url': 'https://api.cybercube21.de/memes/' + meme}, 200  # return data and 200 OK

api.add_resource(Memes, '/memes')

if __name__ == '__main__':
    app.run(port=6969)