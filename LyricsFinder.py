# Basic Lyrics Finder
# DO :- pip install lrclibapi

from lrclib import LrcLibAPI

api = LrcLibAPI(user_agent="lyricsComplete/1.0")

song = input("Enter song name: ")
artist = input("Enter artist name: ")
album_name = input("Enter album: ")
duration = input("Enter duration of the lyrics (only digits, eg: 241): ")

Lyrics = api.get_lyrics (
    track_name = song,
    artist_name = artist,
    album_name = album_name,
    duration = duration
)

found_lyrics = Lyrics.synced_lyrics or Lyrics.plain_lyrics

print("\n".join(found_lyrics.split("\n")[:5]))   

  
    
