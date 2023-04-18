import mysql.connector


def openDB(host, user, password, database):
    return mysql.connector.connect(
        host=host, user=user, password=password, database=database
    )


def closeDB(connection):
    connection.close()


def insertInDB(connection, sql, data):
    cursor = connection.cursor()
    cursor.execute(sql, data)
    connection.commit()
    id = cursor.lastrowid
    cursor.close()

    return id


def listDB(connection, sql):
    cursor = connection.cursor()
    cursor.execute(sql)
    results = cursor.fetchall()
    cursor.close()

    return results


def updateDB(connection, sql, data):
    cursor = connection.cursor()
    cursor.execute(sql, data)
    connection.commit()
    modifiedLines = cursor.rowcount
    cursor.close()

    return modifiedLines


def deleteInDB(connection, sql, data):
    cursor = connection.cursor()
    cursor.execute(sql, data)
    connection.commit()
    modifiedLines = cursor.rowcount
    cursor.close()

    return modifiedLines
