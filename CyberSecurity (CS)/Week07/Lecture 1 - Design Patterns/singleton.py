class Logger:
    _instance = None
    file_name = "log.txt"

    def __new__(cls):
        if not cls._instance:
            cls._instance = super(Logger, cls).__new__(cls)
        return cls._instance

    def log(self, message):
        with open(self.file_name, "a") as file:
            file.write(message + "\n")

logger = Logger()


Logger().log("Sorted arrays {}")