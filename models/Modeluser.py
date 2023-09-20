from .entities.User import User
class modelUser():
    @classmethod
    def login(self, db, correo):
            try:
                cursor=db.connection.cursor()
                sql=""""SELECT idUsuario, correo, password1, nombre_completo FROM Usuario 
                WHERE correo = ` {}` """.format(correo.correoxd)
                cursor.execute(sql)
                row=cursor.fetchone()
                if row != None:
                    correo=User(row[0],row[1],User.check_password(row[2],User.password1), row[3])
                    return correo
                else: 
                    return None
        
            except Exception as ex:
                raise Exception(ex)