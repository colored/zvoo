import os
import time
import random
import pickle

from track import Track


def play(track):
    time.sleep(1)
    print track.path
    print track.plays
    print track.available
    track.plays += 1


def getTrackList():
    rootdir = r"C:\Users\azubko\Music"
    tracks = []

    tracks = get_track_list("tracklist.p")

    if len(tracks) == 0:
        for root, subdirs, files in os.walk(rootdir):
            for file in files:
                if file.endswith(".mp3"):
                    tracks.append(Track(os.path.join(root, file)))
    return tracks


def getTrash():
    return get_track_list("trash.p")


def get_track_list(filename):
    tracks = []
    try:
        tracklist_file = open(filename, "rb")
        tracks = pickle.load(tracklist_file)
    except IOError:
        pass
    return tracks


def main():
    tracklist = getTrackList()
    trash = getTrash()
    while (tracklist):
        current_track = random.choice(tracklist)
        if current_track.available:
            play(current_track)
        else:
            print str(current_track) + " ------------ UNAVAILABLE"
            tracklist.remove(current_track)
            trash.append(current_track)

        pickle.dump(tracklist, open("tracklist.p", "wb"))
        pickle.dump(trash, open("trash.p", "wb"))

main()
