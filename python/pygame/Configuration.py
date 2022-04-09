import configparser, os

class Configuration:
    
    def __init__(self, filename):
        self.parser = configparser.ConfigParser()
        self.filename = filename
        self.init()
        
    def init(self):
        if os.path.exists(self.filename): return
        
        # Initialize default settings
        if self.filename == "settings.ini":
            self.parser["DISPLAY"] = {"width": "700",
                                      "height": "500"}
        
        self.save()
        self.load()
    
    def save(self):
        with open(self.filename, "w") as f:
            self.parser.write(f)
    
    def load(self):
        if os.path.exists(self.filename):
            self.parser.read(self.filename)