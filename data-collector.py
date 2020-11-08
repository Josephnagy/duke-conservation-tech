import mysql.connector

#method: insert sighting into sighting table
def insert_sighting(cursor, cnx, turtle_tag_id, latitude, longitude, drone_image, timestamp): #no sighting_id bc AI field
    insert_stmt = ("""INSERT INTO sighting (turtle_tag_id, latitude, longitude, drone_image, timestamp)
                    VALUES (%s,%s,%s,%s,%s)""") #parameters are always %s
    data = (turtle_tag_id, latitude, longitude, drone_image, timestamp)

    #update db with new data
    cursor.execute(insert_stmt, data)
    cnx.commit()

if __name__ == '__main__':
    #make database connection
    cnx = mysql.connector.connect(
        host = "dct-turtle-uav.cojdookdlkis.us-east-1.rds.amazonaws.com", #AWS RDB endpoint
        user = "admin",
        password = "DukeConservationTech1!",
        database = "dct_turtle_uav_db"
    )
    cursor=cnx.cursor() #create db cursor
