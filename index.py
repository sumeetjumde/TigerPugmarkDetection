from flask import Flask, render_template, request, redirect, flash, url_for
import main
import urllib.request
from app import app, UPLOAD_FOLDER
from werkzeug.utils import secure_filename
from main import getPrediction
import os

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/', methods=['POST'])
def submit_file():
    if request.method == 'POST':
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        if file.filename == '':
            flash('No file selected for uploading')
            return redirect(request.url)
        if file:
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'],filename))
            getPrediction(filename)
            label, acc = getPrediction(filename) # pass the image to our model, makes sure it gives label and accuracy.
            flash(label)
            flash(acc)
            # filename = UPLOAD_FOLDER + "//" + filename
            flash(filename)
            return render_template('index.html',image=filename)

if __name__ == "__main__":
    app.run()


# put the model in main file
# put all images in static folder and keep uploads folder as it is