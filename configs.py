import os

class Config(object):
    #Download files to which folder, ie. downloads
    DOWNLOADS_FOLDER = os.environ.get("DOWNLOADS_FOLDER", "downloads")
    #MongoDB URL
    MONGODB_URI = os.environ.get("MONGODB_URI", "mongodb+srv://raretrack907:nROK1YKWq7ytVfkz@sharktheaquaking.nqcqmbv.mongodb.net/?retryWrites=true&w=majority&appName=SharkTheAquaKing")
    #Port number for running server
    PORT = os.environ.get("PORT", 5000)
    #Bind address/IP, recommended to keep 0.0.0.0
    BIND_ADDRESS = os.environ.get("BIND_ADDRESS", "0.0.0.0")
