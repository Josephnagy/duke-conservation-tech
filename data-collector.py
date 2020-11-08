import mysql.connector as sql

if __name__ == '__main__':
    database = sql.connect(
        host = "dct-turtle-uav.cojdookdlkis.us-east-1.rds.amazonaws.com", #AWS RDB endpoint
        user = "admin",
        password = "DukeConservationTech1!"
    )
    mycursor=database.cursor()
    print(database)
