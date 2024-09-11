import uuid
import json 
from datetime import datetime

class LogEntry:

    def __init__(self, message,):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.message = message

    def __str__(self):
        return f"[LogEntry] ({self.id}) {self.message}"
    
class Logger:
    def __init__(self):
       self.__log_list = []

    def log(self, message):
        self.__log_list.append(LogEntry(message))

    def get_logs(self):
        return [str(obj) for obj in self.__log_list]
    
    def save_to_file(self, file_path):  
        with open(file_path, "w") as file: 
            

    
