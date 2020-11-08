import mysql.connector

if __name__ == '__main__':
    #make database connection
    cnx = mysql.connector.connect(
        host = "dct-turtle-uav.cojdookdlkis.us-east-1.rds.amazonaws.com", #AWS RDB endpoint
        user = "admin",
        password = "DukeConservationTech1!",
        database = "dct_turtle_uav_db"
    )
    #create db cursor
    cursor=cnx.cursor()
    #insert_stmt = ("INSERT INTO sighting (turtle_tag_id) VALUES (%s) ")
    #data = (1,)
    #cursor.execute(insert_stmt, data)
    #cnx.commit()
    print(cnx.database)
