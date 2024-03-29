import mysql.connector
import datetime
import os
import cv2
from PIL import Image
from PIL.ExifTags import TAGS, GPSTAGS
import exifread as ef

#insert sighting into sighting table
def insert_sighting(cursor, cnx, turtle_tag_id, latitude, longitude, drone_image, timestamp): #no sighting_id bc AI field
    insert_stmt = ("""INSERT INTO sighting (turtle_tag_id, latitude, longitude, drone_image, timestamp)
                    VALUES (%s,%s,%s,%s,%s)""") #parameters are always %s
    data = (turtle_tag_id, latitude, longitude, drone_image, timestamp)
    #update db with new data
    cursor.execute(insert_stmt, data)
    cnx.commit()
    return

def get_exif(filename):
    exif = Image.open(filename)._getexif()
    if exif is not None:
        for key, value in exif.items():
            name = TAGS.get(key, key)
            exif[name] = exif.pop(key)
    print(exif.keys())

def get_timestamp(path):
    t = os.path.getmtime(path)
    if(t):
        return datetime.datetime.fromtimestamp(t)
    else:
        print("No timestamp available")
        return None

def load_images_from_folder(folder):
    images = []
    for filename in os.listdir(folder):
        img = cv2.imread(os.path.join(folder,filename))
        if img is not None:
            images.append(img)
    return images

def connect_to_db(host, user, pw, db):
    return mysql.connector.connect(host = host,user = user,password = pw,database = db)

if __name__ == '__main__':
    #DB credentials
    host = "dct-turtle-uav.cojdookdlkis.us-east-1.rds.amazonaws.com" #AWS RDB endpoint
    # user = *insert user* 
    # password = *insert password*
    database = "dct_turtle_uav_db"

    #establish DB connection
    #cnx = connect_to_db(host, user, password, database)

    #test get exif
    path = "/Users/josephnagy/Desktop/test.jpg"
