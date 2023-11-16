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


def db_connection():
    cred = credentials.Certificate("key.json")
    firebase_admin.initialize_app(cred)
    db = firestore.client()
    collection = db.collection("recipes").get()
    recipes_list=[]
    for r in collection:
        recipes_list.append(r.to_dict())
    return recipes_list
    
    

@app.route("/")
def view_recipes():
    recipes= db_connection()
    print(recipes)
    return render_template("home.html")


if __name__ == '__main__':
    app.run()

