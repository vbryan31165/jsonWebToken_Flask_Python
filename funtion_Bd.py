from flask_mysqldb import MySQL

conexion = MySQL()

def listar_users():
    try:
        cursor = conexion.connection.cursor()
        sql = "SELECT id, usuario FROM usuarios"
        cursor.execute(sql)
        datos = cursor.fetchall()
        users = []
        for fila in datos:
            users = {'id': fila[0], 'usuario': fila[1]}
            users.append(users)
        return users
    except Exception as ex:
        error="Error en datos consultados"
        return error