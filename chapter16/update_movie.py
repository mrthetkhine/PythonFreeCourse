from mysql.connector import connect, Error

try:
    with connect(
        host="localhost",
        user="root",
        password="root123!@#",
        database="python_free_course",
    ) as connection:
        #print(connection)
        id = input("Enter movie Id to update ")
        title= input ("Enter title to update ")
        description  = input("Enter description to update")
        year = input("Enter year to update")
        sql = "UPDATE movie SET title=\'"+title+"\',description=\'"+description+"\',year="+year+" WHERE id="+id;
        print(sql)
        with connection.cursor() as cursor:
            cursor.execute(sql)
            connection.commit()
except Error as e:
    print(e)