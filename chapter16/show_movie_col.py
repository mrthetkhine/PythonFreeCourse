from mysql.connector import connect, Error

try:
    with connect(
        host="localhost",
        user="root",
        password="root123!@#",
        database="python_free_course",
    ) as connection:
        #print(connection)
        sql = """SELECT * FROM movie"""
        print(sql)
        with connection.cursor() as cursor:
            cursor.execute(sql)
            for movie in cursor.fetchmany(size=3):
            #for movie in cursor.fetchall():
                print("Name name ",movie[1])
except Error as e:
    print(e)