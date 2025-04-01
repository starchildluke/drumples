# /// script
# requires-python = ">=3.10"
# dependencies = [
#     "marimo",
#     "spotipy"
# ]
# ///

import marimo

__generated_with = "0.11.31"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo
    # import glob
    import random

    random.seed(0,random.randint(1, 9999))

    button = mo.ui.button(label="Generate new set")
    return button, mo, os, random


@app.cell
def _(button):
    button
    return


@app.cell
def _(button, random):
    button

    # Uncomment this audio_files variable and replace it with the example one to use local files!
    # audio_files = glob.glob('/path/to/wav_files', recursive=True)

    audio_files = ['https://github.com/starchildluke/drumples/raw/bcd9d88f7494e93c4a97dc857e1d01e85eecaaea/drums/kicks/kick 09.wav',
    'https://github.com/starchildluke/drumples/raw/bcd9d88f7494e93c4a97dc857e1d01e85eecaaea/drums/kicks/kick 10.wav',
    'https://github.com/starchildluke/drumples/raw/bcd9d88f7494e93c4a97dc857e1d01e85eecaaea/drums/kicks/kick 30.wav',
    'https://github.com/starchildluke/drumples/raw/bcd9d88f7494e93c4a97dc857e1d01e85eecaaea/drums/kicks/kick_croup_001.wav',
    'https://github.com/starchildluke/drumples/raw/bcd9d88f7494e93c4a97dc857e1d01e85eecaaea/drums/kicks/kick_croup_002.wav',
    'https://github.com/starchildluke/drumples/raw/bcd9d88f7494e93c4a97dc857e1d01e85eecaaea/drums/snares/!Snare 63.wav',
    'https://github.com/starchildluke/drumples/raw/bcd9d88f7494e93c4a97dc857e1d01e85eecaaea/drums/snares/!Snare 64.wav',
    'https://github.com/starchildluke/drumples/raw/bcd9d88f7494e93c4a97dc857e1d01e85eecaaea/drums/snares/!Snare 68.wav',
    'https://github.com/starchildluke/drumples/raw/bcd9d88f7494e93c4a97dc857e1d01e85eecaaea/drums/snares/!Snare 69.wav',
    'https://github.com/starchildluke/drumples/raw/bcd9d88f7494e93c4a97dc857e1d01e85eecaaea/drums/snares/!Snare 76.wav',
    'https://github.com/starchildluke/drumples/raw/bcd9d88f7494e93c4a97dc857e1d01e85eecaaea/drums/hats/!Hat 10.wav',
    'https://github.com/starchildluke/drumples/raw/bcd9d88f7494e93c4a97dc857e1d01e85eecaaea/drums/hats/!Hat 11.wav',
    'https://github.com/starchildluke/drumples/raw/bcd9d88f7494e93c4a97dc857e1d01e85eecaaea/drums/hats/!Hat 7.wav',
    'https://github.com/starchildluke/drumples/raw/bcd9d88f7494e93c4a97dc857e1d01e85eecaaea/drums/hats/!Hat 8.wav',
    'https://github.com/starchildluke/drumples/raw/bcd9d88f7494e93c4a97dc857e1d01e85eecaaea/drums/hats/!Hat 9.wav']

    kicks = [kick for kick in audio_files if any(k_str in kick for k_str in ['kick', 'Kick'])]
    snares = [snare for snare in audio_files if any(s_str in snare for s_str in ['snare', 'Snare'])]
    hats = [hat for hat in audio_files if any(h_str in hat for h_str in ['hat', 'Hat'])]

    k = random.randint(0,len(kicks)-1)
    s = random.randint(0,len(snares)-1)
    h = random.randint(0,len(hats)-1)
    return audio_files, h, hats, k, kicks, s, snares


@app.cell
def _(h, hats, k, kicks, mo, s, snares):
    mo.vstack(
                [
                    mo.hstack([mo.audio(kicks[k]), kicks[k].replace('https://github.com/starchildluke/drumples/raw/bcd9d88f7494e93c4a97dc857e1d01e85eecaaea', '')]),
                    mo.hstack([mo.audio(snares[s]), snares[s].replace('https://github.com/starchildluke/drumples/raw/bcd9d88f7494e93c4a97dc857e1d01e85eecaaea', '')]),
                    mo.hstack([mo.audio(hats[h]), hats[h].replace('https://github.com/starchildluke/drumples/raw/bcd9d88f7494e93c4a97dc857e1d01e85eecaaea', '')])
                ])
    return


@app.cell
def _(random):
    import spotipy
    from spotipy.oauth2 import SpotifyClientCredentials

    # Authentication to access the Spotify API. You can change this to something more secure

    client_id = "CLIENT_ID"
    client_secret = "CLIENT_SECRET"

    if not client_id or not client_secret:
        raise ValueError("Spotify Client ID and Secret required.")

    sp = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials(client_id, client_secret))

    def get_random_song_from_playlists(playlist_ids):
        """
        Retrieves a random song from a list of Spotify playlists.

        Args:
            playlist_ids: A list of playlist IDs (strings).

        Returns:
            A tuple containing the song ID and the playlist name, or None if no songs are found.
        """
        all_songs = []

        for playlist_id in playlist_ids:
            try:
                playlist = sp.playlist(playlist_id=playlist_id)
                songs = playlist['tracks']['items']
                for song in songs:
                    all_songs.append((song['track']['external_urls']['spotify'], playlist_id))  
            except spotipy.SpotifyException as e:
                print(f"Error retrieving playlist '{playlist_id}': {e}")
                continue

        if not all_songs:
            return None

        return random.choice(all_songs)
    return (
        SpotifyClientCredentials,
        client_id,
        client_secret,
        get_random_song_from_playlists,
        sp,
        spotipy,
    )


@app.cell
def _(button, get_random_song_from_playlists, mo):
    button

    # Added some example playlists to demo the function
    my_playlists = ["3ba3QuIhfe01u0tnYDEnPI", "47h7HSJ3DEJ2rAxo8Q8r7I"]
    random_song = get_random_song_from_playlists(my_playlists)

    song_name, playlist_id = random_song
    mo.Html(f'''
        <iframe style="border-radius:12px" src="https://open.spotify.com/embed/track/{random_song[0].replace('https://open.spotify.com/track/', '')}" width="100%" height="352" frameBorder="0" allowfullscreen="" allow="autoplay; clipboard-write; encrypted-media; fullscreen; picture-in-picture" loading="lazy"></iframe>
    ''')
    return my_playlists, playlist_id, random_song, song_name


if __name__ == "__main__":
    app.run()
