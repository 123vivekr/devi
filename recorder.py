import os

DIRECTORY_NAME = "store"

class Recorder:
    def __init__(self, record):
        self.record_name = record
        self.record_dir = None

        if record is None:
            return

        self.record_dir = os.path.join(DIRECTORY_NAME, record)
        if not os.path.exists(DIRECTORY_NAME):
            os.makedirs(DIRECTORY_NAME)
            os.makedirs(self.record_dir)
    
    def record(self, stage, type, content):
        if self.record_name is None:
            return

        file_path = os.path.join(self.record_dir, f"{stage}-{type}.txt")
        with open(file_path, "w") as file:
            file.write(content + "\n") 
