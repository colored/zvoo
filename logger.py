import datetime


class Logger(object):
    def __init__(self, filepath):
        self.file_path = filepath

    def info(self, record):
        with open(self.file_path, "a") as log_file:
            log_file.write("INFO: " + str(datetime.datetime.utcnow()) + record + "\n")
