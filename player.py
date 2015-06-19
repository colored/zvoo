import os
import time
import random

from track import Track


def play(track):
    track.plays = 2
    time.sleep(1)
    print track.path
    print track.plays
    print track.available


def getTrackList():
    rootdir = r"C:\Users\azubko\Music"
    tracks = []
    for root, subdirs, files in os.walk(rootdir):
        for file in files:
            if file.endswith(".mp3"):
                tracks.append(Track(os.path.join(root, file)))
    # encoded = json.dumps(tracks)
    return tracks


def main():
    tracklist = getTrackList()
    while (tracklist):
        current_track = random.choice(tracklist)
        if current_track.available:
            play(current_track)


main()
