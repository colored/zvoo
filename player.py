import os
import time
import random
import pickle

from track import Track
from logger import Logger


def play(track):
    time.sleep(1)
    print track.path
    logger = Logger("test_log.txt")
    logger.info(track.path)
    os.system("omxplayer -o local " + "\"" + track.path + "\"")
    track.plays -= 1


def getTrackList():
    rootdir = r"/home"  # r"C:\Users\azubko\Music"

    tracks = get_track_list("tracklist.p")

    if len(tracks) == 0:
        for root, subdirs, files in os.walk(rootdir):
            for file in files:
                if file.endswith(".mp3") or file.endswith(".flac"):
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
