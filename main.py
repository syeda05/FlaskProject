from flask import Flask,redirect, url_for, render_template, request, flash

#importing os to get path address of images in static folder
import os

#for uploading images for add recipe
from flask_wtf import FlaskForm
from wtforms import FileField,SubmitField
from werkzeug.utils import secure_filename

#for database
import firebase_admin
from firebase_admin import credentials, firestore

app = Flask(__name__)

class Recipe:
    def __init__(self, id, recipeName, ingredients, instructions, category, rating  ):
         self.id = id
         self.recipeName = recipeName
         self.ingredients = ingredients
         self.instruction = instructions
         self.category =category
         self.rating = rating

class RecipeManagmentSystem:
    def __init__(self, db_name = 'recipes'):
        cred = credentials.Certificate("key.json")
        firebase_admin.initialize_app(cred)
        self.db = firestore.client()
        self.collection = self.db.collection(db_name)

@app.route("/")
def hello_world():
    print("hello")

if __name__ == '__main__':
    app.run()