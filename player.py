import os
import time
import random

from track import Track


def play(track):
    track.plays += 1
    time.sleep(3)
    print track.path
    print track.plays


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
        if (current_track.plays == 3):
            tracklist.remove(current_track)
            print str(current_track) + " REMOVED ! ! !"
            continue
        play(current_track)


main()
