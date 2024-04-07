import tkinter as tk
from tkinter import messagebox
import requests

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

def search_song():
    song_name = entry.get()
    song_info = fetch_song_info(song_name)
    if song_info:
        title_label.config(text="Title: " + song_info['title'])
        artist_label.config(text="Artist: " + song_info['artist'])
        url_label.config(text="Genius URL: " + song_info['url'])
    else:
        messagebox.showerror("Error", "Song not found.")

root = tk.Tk()
root.title("Song Information Retrieval")

label = tk.Label(root, text="Enter a sample of the lyrics or the name of the song:")
label.pack()

entry = tk.Entry(root, width=50)
entry.pack()

search_button = tk.Button(root, text="Search", command=search_song)
search_button.pack()

title_label = tk.Label(root, text="")
title_label.pack()

artist_label = tk.Label(root, text="")
artist_label.pack()

url_label = tk.Label(root, text="")
url_label.pack()

root.mainloop()
