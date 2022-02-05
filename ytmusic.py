from ytmusicapi import YTMusic
import json
import functools

# Follow YTMusicApi docs for setup : https://github.com/sigma67/ytmusicapi
ytmusic = YTMusic('[[[HEADER AUTHENTICATION FILE]]]')

songsFile = open('[[[SONGS FILE]]]', "r")
unfound = open('./Unfound.json', "w")
unfoundDict = []
songs = json.loads(songsFile.read())

playlistId = ytmusic.create_playlist("[[[PLAYLIST NAME]]]", "[[[PLAYLIST DESCRIPTION]]]")
for song in songs:
    songTitle = song["song"]
    artists = functools.reduce(lambda x, y: str(x) + " " + str(y), song["artists"])
    search_results = ytmusic.search(str(songTitle) + " " + artists, 'songs')
    if len(search_results) > 0:
        ytmusic.add_playlist_items(playlistId, [search_results[0]['videoId']])
    else:
        unfoundDict.append(song)

json.dump(unfoundDict, unfound)

songsFile.close()
unfound.close()
    