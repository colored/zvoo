import os
import time
import random

from track import Track


def play(track):
    time.sleep(3)
    print track.path


def getTrackList():
    rootdir = r"C:\Users\azubko\Music"
    tracks = []
    for root, subdirs, files in os.walk(rootdir):
        for file in files:
            if file.endswith(".mp3"):
                try:
                    tracks.append(Track(os.path.join(root, file)))
                except TypeError:
                    pass

    return tracks


def main():
    tracklist = getTrackList()
    random.shuffle(tracklist)
    for track in tracklist:
        play(track)


main()
