import mysql.connector
import datetime
import os


def get_timestamp(path):
    t = os.path.getmtime(path)
    if(t):
        return datetime.datetime.fromtimestamp(t)
    else:
        print("No timestamp available")
        return None

#method: insert sighting into sighting table
def insert_sighting(cursor, cnx, turtle_tag_id, latitude, longitude, drone_image, timestamp): #no sighting_id bc AI field
    insert_stmt = ("""INSERT INTO sighting (turtle_tag_id, latitude, longitude, drone_image, timestamp)
                    VALUES (%s,%s,%s,%s,%s)""") #parameters are always %s
    data = (turtle_tag_id, latitude, longitude, drone_image, timestamp)

    #update db with new data
    cursor.execute(insert_stmt, data)
    cnx.commit()

def connect_to_db(host, user, pw, db):
    #setup db connection
    cnx = mysql.connector.connect(
        host = host,
        user = user,
        password = pw,
        database = db
    )
    cursor=cnx.cursor() #create db cursor
    return cnx, cursor

if __name__ == '__main__':
    host = "dct-turtle-uav.cojdookdlkis.us-east-1.rds.amazonaws.com", #AWS RDB endpoint
    user = "admin",
    password = "DukeConservationTech1!",
    database = "dct_turtle_uav_db"

    #connect to DB
    cxn, cursor = connect_to_db(host, user, password, database)

    #test get_timestamp method
    path = "/Users/josephnagy/Desktop/test.jpg"
    print(get_timestamp(path))
