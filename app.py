from flask import Flask, render_template, request
import requests
import json

app = Flask(__name__)

def fetch_song_info(song_name):
    access_token = 'Z-_ZaDOxbkVPJz5aIZ4cWHA2OXWT9DROd755M1ur-HISETuxP-OHGDot4XvFiQhc'
    base_url = 'https://api.genius.com'
    search_endpoint = '/search'
    params = {'q': song_name}
    headers = {'Authorization': 'Bearer ' + access_token}
    response = requests.get(base_url + search_endpoint, params=params, headers=headers)
    json_data = response.json()
    if 'response' in json_data:
        hits = json_data['response']['hits']
        if hits:
            song_info = hits[0]['result']
            return {
                'title': song_info['title'],
                'artist': song_info['primary_artist']['name'],
                'url': song_info['url']
            }
    return None

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search', methods=['POST'])
def search():
    song_name = request.form['song_name']
    song_info = fetch_song_info(song_name)
    if song_info:
        return render_template('results.html', song_info=song_info)
    else:
        return "Song not found."

if __name__ == "__main__":
    app.run(debug=True)
