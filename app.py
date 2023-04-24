from flask import Flask, render_template
from dotenv import load_dotenv
import requests
import os

load_dotenv()
app = Flask(__name__)
api_key = os.getenv('API_KEY')
page = 1


@app.route('/', defaults = {'page': 1})
@app.route('/<page>')
def index(page):
    req = requests.get(f'https://api.themoviedb.org/3/discover/movie?api_key={api_key}&language=pt-BR&page={page}')
    r = req.json()
    return render_template('index.html', r = r)

if __name__ == '__main__':
    app.run(debug= True)