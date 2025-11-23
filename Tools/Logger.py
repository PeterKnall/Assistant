from datetime import datetime

class Log:
    def __init__(self):
        self.filename = "log.txt"
        with open(self.filename, "w") as file:
            file.write(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')} : Application Started.")

    @staticmethod
    def logit(self, entry):
        with open(self.filename, "a") as file:
            file.write(f"\n{datetime.now().strftime('%Y-%m-%d %H:%M:%S')} : {entry}")