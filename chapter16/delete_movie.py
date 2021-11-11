from mysql.connector import connect, Error

try:
    with connect(
        host="localhost",
        user="root",
        password="root123!@#",
        database="python_free_course",
    ) as connection:
        #print(connection)
        id = input("Enter movie Id to delete ")
        sql = "DELETE FROM movie WHERE id="+id;
        print(sql)
        with connection.cursor() as cursor:
            cursor.execute(sql)
            connection.commit()
except Error as e:
    print(e)