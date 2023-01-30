import os
import logging
class Config:                                                                   
    API_ID = int(os.environ.get("API_ID", "24198383"))
    API_HASH = os.environ.get("API_HASH", "819a631e42b840a60ac6f923e1290bce")       
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "5729182401:AAF96cHFyRfRK--BznUeybplrV8OyZIxbXU")
    BOT_SESSION = os.environ.get("BOT_SESSION", "forwardbot")
    OWNER_ID = os.environ.get("OWNER_ID", "5757479875")                             
    DATABASE_URI = os.environ.get("DATABASE_URI", "mongodb+srv://terabox:terabox@cluster0.nrehwsq.mongodb.net/?retryWrites=true&w=majority")  
    DATABASE_NAME = os.environ.get("DATABASE_NAME", "Cluste0")
    COLLECTION_NAME = os.environ.get('COLLECTION_NAME', 'Data')
    SESSION = os.environ.get("SESSION", "AQBj16L_sBXWngUR-iJ5lj5ufmOIdxvKVOE7G2yBvvKf-mLpOdOKf8biFPSFNIJ6vJlHVOYT3qBccdLiU5CH4lj0TEXemJbbggurIQWGsng3FJsrqGS5SVblFOGcA1s_qqy2nmm5Lp3ced1VRFN3TbYlycFQm032H-5lIFXIgFizlAMCvi8ssTOqzaogYGeUtKh6vtXss00dESPKmdnYzY30rCitW43_tiO9zq5gPKgQbrLyEdLacZv-q-o6ugxrGq8LpHyVCXn4D2KLJtc09x-0H3OVmdRM9fYyBnNFZHy-sMJdMVr5ltEEok03Upigfv5k9BtlnDDyqen4_SKD8MOcAAAAAVcsK8MA")   
    TO_CHANNEL = int(os.environ.get("TO_CHANNEL", "-1001617435227"))
    BOT_USERNAME= os.environ.get("BOT_USERNAME", "My_Frwd_Bot")


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
