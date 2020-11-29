from flask import Flask, render_template, request, redirect, url_for
from werkzeug.utils import secure_filename
import pandas as pd

app = Flask(__name__)

def allowed_file(filename):
    return '.' in filename and \
        filename.strip().split('.')[-1] == 'csv'

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        file_csv = request.files['file']
        if file_csv and allowed_file(file_csv.filename):
            filename = secure_filename(file_csv.filename)
            df = pd.read_csv(file_csv)
            df = df.sort_values(by='Ранг')
            return df.to_html()
    return '''
    <!doctype html>
    <title>Home</title>
    <h1>Upload csv file</h1>
    <form action="" method=post enctype=multipart/form-data>
    <p><input type="file" name=file>
        <input type=submit value=Upload>
    </form>
    '''

app.run(host='0.0.0.0', port=80)
