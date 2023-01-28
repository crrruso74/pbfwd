import os
import logging
class Config:                                                                   
    API_ID = int(os.environ.get("API_ID", "21818317"))
    API_HASH = os.environ.get("API_HASH", "bc6ab154300cc41fe127ca4d658dc75d")       
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "5988361578:AAHukwb3OyI0BDGmkyVGszSbBSKjEnZUQbo")
    BOT_SESSION = os.environ.get("BOT_SESSION", "forwardbot")
    OWNER_ID = os.environ.get("OWNER_ID", "5757479875")                             
    DATABASE_URI = os.environ.get("DATABASE_URI", "mongodb+srv://terabox:terabox@cluster0.nrehwsq.mongodb.net/?retryWrites=true&w=majority")  
    DATABASE_NAME = os.environ.get("DATABASE_NAME", "Cluste0")
    COLLECTION_NAME = os.environ.get('COLLECTION_NAME', 'Data')
    SESSION = os.environ.get("SESSION", "AQC-f3L_3VxvyMkjPmaUbEGtrU45mkCUIibS3vTn1N48PJmLpVGMhzzTVwFupjIzTMGJulVGykzlXEnNnZaDpAQl5i90WQR1L2WSl2pW-CN6sgnoRKpewh1fRAKOtui7EX70o1O_lVNI9UzuHi5_ConWG_75gBfa_rHI-D3G5fAOzK9tN29_2EKQUL2Oy-8AYfM666RqoH9Gkm6gNlJx2sNHn2WPxrTWF8R0HTraMTJWITJW-Tfn0aOS_3-A3OVv2l3zPUo9T8I2YQ-9hPBIpTopSJnSIGMST8lWLxBbEbXanP5a625v27736Q_Oz_1CYmKIXkgPFMPlB2YJTiJK__jyAAAAAVcsK8MA")   
    TO_CHANNEL = int(os.environ.get("TO_CHANNEL", "-1001252405271"))
    BOT_USERNAME= os.environ.get("BOT_USERNAME", "MX-Forward-Bot")


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
