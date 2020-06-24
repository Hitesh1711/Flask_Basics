import os
from flask import Flask, flash, request, redirect, url_for,render_template
from werkzeug.utils import secure_filename
app = Flask(__name__)
app.config['UPLOAD_FOLDER']='/Users/lenova/Desktop/my-sample-python-project'


@app.route('/')
def default_index():
    return render_template('home_up.html')


@app.route('/upload')
def upload_file():
   return render_template('upload.html')



@app.route('/uploader', methods = ['GET', 'POST'])
def upload_file1():
   if request.method == 'POST':
      f = request.files['file']
      f.save(secure_filename(f.filename))
      return render_template('after.html')

if __name__ == '__main__':
   app.run(debug = True)
