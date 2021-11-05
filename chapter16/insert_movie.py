from mysql.connector import connect, Error

try:
    with connect(
        host="localhost",
        user="root",
        password="root123!@#",
        database="python_free_course",
    ) as connection:
        #print(connection)
        title = input("Enter title ")
        description = input("Enter description ")
        year = input("Enter year")
        sql = "INSERT INTO movie(title,description,year) VALUES (\'"+title+"\',\'"+description+"\',"+year+");"
        print(sql)
        with connection.cursor() as cursor:
            cursor.execute(sql)
            connection.commit()
except Error as e:
    print(e)