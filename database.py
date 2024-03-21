import mysql.connector as mysql

connect_params = {
    'user':"root",
    'password':'MariaDB',
    'host':"localhost",
    'database':"ecole"
}

with mysql.connect(**connect_params) as db:
    with db.cursor() as cursor:
        cursor.execute("SELECT * FROM ETUDIANTS")
        cursor.execute(sql)
        etudiants = cursor.fetchall()
        #print(etudiants)




