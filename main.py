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

class UploadFileForm(FlaskForm):
    file = FileField("File")
    submit= SubmitField("submit")

app = Flask(__name__)
app.config['SECRET_KEY']='supersecretkey'

picFolder = os.path.join('static', 'images')
#print(picFolder) --> static/images

app.config['UPLOAD_FOLDER'] = picFolder

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
    
    
recipes_list = db_connection()
recipe_list_backup = recipe_list

@app.route("/")
def view_recipes():
    print(recipes_list)
    logo = os.path.join(app.config['UPLOAD_FOLDER'], 'logo.jpg')
    return render_template("home.html",logo=logo,recipe_list=recipes_list)

<<<<<<< HEAD
<<<<<<< HEAD
@app.route("/deleteRecipe")
def deleteRecipe():

    logo = os.path.join(app.config['UPLOAD_FOLDER'], 'logo.jpg')
    recipe_id = request.args.get("id")
    i= 0 
    for recipe in recipe_list_backup:
        if recipe_id == str(recipe['id']):
            recipe_list_backup.pop(i)
        i=i+1
    #return render_template("delete-confirmation.html",logo=logo)
    print("deleted")
=======
>>>>>>> parent of bc3d2b8 (created delteRecipe function)
=======
>>>>>>> parent of bc3d2b8 (created delteRecipe function)

if __name__ == '__main__':
    app.run()

