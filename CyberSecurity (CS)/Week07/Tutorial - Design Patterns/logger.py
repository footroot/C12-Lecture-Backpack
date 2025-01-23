from datetime import datetime

class Logger():
    _instance = None

    def __new__(cls, *args, **kwargs):

        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance
    
    def log(self, message):
        raise NotImplementedError("Log method must be implemented by subclasses.")

class ConsoleLogger(Logger):
    def log(self, message):
        print(f"[LOG] {message}")

class FileLogger(Logger):
    def __init__(self):
        self.file = open("log.txt", "a")

    def log(self, message):
        self.file.write(f"{message}\n")
        self.file.flush()

class LoggerFactory:
    @staticmethod
    def get_logger(logger_type):
        if logger_type == "console":
            return ConsoleLogger()
        elif logger_type == "file":
            return FileLogger()
        else:
            raise ValueError("Unsupported logger type!")

class LoggerDecorator(Logger):
    def __init__(self, logger):
        self._logger = logger

    def log(self, message):
        self._logger.log(message)

class TimestampDecorator(LoggerDecorator):
    def log(self, message):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        super().log(f"{timestamp} - {message}")

class SeverityLevelDecorator(LoggerDecorator):
    def __init__(self, logger, level):
        super().__init__(logger)
        self.level = level

    def log(self, message):
        super().log(f"[{self.level}] - {message}")
