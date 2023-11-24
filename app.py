from flask import Flask, redirect, render_template, request, url_for
from flaskext.mysql import MySQL
from datetime import datetime
""" import mysql.connector """

app = Flask(__name__)


#models
from models.Modeluser import modelUser

#entities
from models.entities.User import User



# Configuración de la base de datos
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = ''
app.config['MYSQL_DATABASE_DB'] = 'arquideco'  # Ajusta el nombre de la base de datos si es diferente

# Inicialización de MySQL
mysql = MySQL()
mysql.init_app(app)

# Rutas para mostrar vistas
@app.route("/")
def index():    
    return render_template("index.html")

@app.route("/regi")
def registrar():
    return render_template("registrar.html")

@app.route("/ini")
def ini():
    return render_template("login.html")

@app.route("/desc")
def desc():
    return render_template("inmuebleadmin.html")
@app.route("/cat")
def cat():
    return render_template("inmueble.html")
@app.route("/regIn")
def rin():
    return render_template("pruebaI.html")


#proceso de registro de usuario
@app.route('/reci', methods=['POST'])
def reci():
    #asigna una variable a cada dato escrito en el formulario
    _nombre = request.form["nameusu"]
    _correo = request.form["emailusu"]
    _cumple = request.form["cumusu"]
    _celular = request.form["celusu"]
    _documento = request.form["docusu"]
    _pass = request.form["passusu"]
    _pass2 = request.form["passusu2"]
    
#los guarda en la variable datos
    datos = (_nombre, _correo, _cumple, _celular, _documento, _pass, _pass2)
#verirfica que las contraseñas sean iguales
    if _pass==_pass2:
#ejecuta la sentencia       
       sql = "INSERT INTO `usuario` (`IdUsuario`, `nombre_completo`, `correo`, `fechaNacimiento`, `telefono`, `Documento`, `password1`, `password2`, `fk_IdRol`,`fk_IdAgenda`) VALUES (NULL, %s, %s, %s, %s, %s, %s, %s, 2202, NULL);"

#hace la verificacion de conexion y regresa a la vista inmueble
       try:
           conn = mysql.connect()
           cursor = conn.cursor()
           cursor.execute(sql, datos)  # Corregido aquí: pasar los datos al método execute
           conn.commit()
       except Exception as e:
            return f"Error en la inserción: {str(e)}"
       finally: 
        cursor.close()
        conn.close()
    
        return render_template("inmueble.html")
    else:
        return render_template("registrar.html")
   
   
     
     
@app.route('/inmuebleR', methods=['POST'])
def inmuebleR():
    nImagen=0
    _descpricion = request.form["descpricion"]
    _habitaciones = request.form["habitaciones"]
    _baños = request.form["baños"]
    _precio = request.form["precio"]
    _estrato = request.form["estrato"]
    _ubicacion = request.form["ubicacion"]
    _tipo_inmueble = request.form['tipo_inmueble']
    imagenes = request.files.getlist('imagenes')

    datos = (_descpricion, _habitaciones, _baños, _precio, _estrato, _ubicacion, _tipo_inmueble)

    sql = "INSERT INTO `inmueble` (`IdInmueble`, `descpricion`, `habitaciones`, `baños`, `precio`, `estrato`, `ubicacion`, `TipoInmueble`) VALUES (NULL, %s, %s, %s, %s, %s, %s, %s);"

    try:
        conn = mysql.connect()
        cursor = conn.cursor()
        print("uwu")
        cursor.execute(sql, datos)
        conn.commit()
        print("uwu2")
        id_inmueble = cursor.lastrowid  # Guarda el ID del inmueble recién registrado
        print(str(id_inmueble) + "uwuwuwuwuwuwuw")
        for imagen in imagenes:
            nImagen=nImagen+1
            print("entro al for")
            now = datetime.now()
            tiempo = now.strftime("%Y%H%M%S")
            nuevoNombreFoto = str(tiempo)+str(nImagen) + imagen.filename
            try:
                imagen.save("uploads/" + nuevoNombreFoto)
                ruta = "uploads/" + nuevoNombreFoto
                print("Imagen guardada en:", ruta)
                datos2 = (ruta, id_inmueble)
                sql = "INSERT INTO `Imagenesinmueble` (`idImagen`, `nombreImagen`, `fk_IdInmueble`) VALUES (NULL, %s, %s);"

                try:
                    cursor.execute(sql, datos2)
                    conn.commit()
                except Exception as e:
                    return f"Error en la inserción de imágenes: {str(e)}"
            except Exception as e:
                return f"Error al guardar la imagen: {str(e)}"

    except Exception as e:
        return f"Error en la inserción de inmueble: {str(e)}"

    finally:
        cursor.close()
        conn.close()

    return render_template("inmueble.html")
   
     
 #LOGIN   
@app.route('/log', methods=['POST'])
def log():
    user = request.form['usuario']
    passw = request.form['contrasena']

    conn = mysql.connect()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM usuario WHERE correoUsuario= %s AND contraseñausuario = %s", (user, passw))
    user = cursor.fetchone()
    cursor.close()

    if user:
        # Inicio de sesión exitoso
        return redirect("catalogo")
    else:
        # Inicio de sesión fallido
        return redirect("login")


# CONSULTAR DATOS
@app.route("/crud")
def crud():
    sql = "select * from usuario"
    conn = mysql.connect()
    cursor = conn.cursor()
    cursor.execute(sql)  # Corregido aquí: pasar los datos al método execute
    usuario=cursor.fetchall()
    conn.commit()
    print(usuario)
    
    return render_template("crud.html", usuario=usuario)
#CONSULTAR INMUEBLES
@app.route("/inmuebleC")
def inmuebleC():
    sql = "SELECT i.descpricion,i.precio,i.ubicacion FROM inmueble i;"
    conn = mysql.connect()
    cursor = conn.cursor()
    cursor.execute(sql)  # Corregido aquí: pasar los datos al método execute
    inmueble=cursor.fetchall()
    conn.commit()
    print(inmueble)
    
    return render_template("crud.html", inmueble=inmueble)

#ELIMINAR DATOS
@app.route("/destroy/<int:id>")
def destroy(id):
    
    conn = mysql.connect()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM usuario where idUsuario=%s",(id))  # Corregido aquí: pasar los datos al método execute
    
    conn.commit()
    
    
    return redirect("/crud")

#EDITAR DATOS
@app.route("/edit/<int:id>")
def edit(id):
    
    
    conn = mysql.connect()
    cursor = conn.cursor()
    
    cursor.execute("select * from usuario where idUsuario=%s",(id))  # Corregido aquí: pasar los datos al método execute
    
    usuario=cursor.fetchall()
    conn.commit()
    return render_template("edit.html", usuario=usuario)

@app.route('/update', methods=['POST'])
def update():
    #asigna una variable a cada dato escrito en el formulario
    _nombre = request.form["nameusu"]
    _correo = request.form["emailusu"]
    _cumple = request.form["cumusu"]
    _celular = request.form["celusu"]
    _documento = request.form["docusu"]
    _pass = request.form["passusu"]
    _pass2 = request.form["passusu2"]
    _rol = request.form["rol"]
    _id = request.form["id"]
    
#los guarda en la variable datos 
    datos = (_nombre, _correo, _cumple, _celular, _documento, _pass,_pass2,_rol,_id)
    
        
        
        
    sql = "UPDATE `usuario` SET `nombre_completo` = %s, `correo` = %s, `fechaNacimiento` =%s, `telefono` = %s, `Documento` = %s, `password1` = %s, `password2` = %s, `fk_IdRol` = %s WHERE `IdUsuario` =%s;"

#hace la verificacion de conexion y regresa a la vista inmueble
    
    conn = mysql.connect()
    cursor = conn.cursor()
    cursor.execute(sql, datos)  # Corregido aquí: pasar los datos al método execute
    conn.commit()
    
    cursor.close()
    conn.close()
    
    return redirect("/crud")
    
    
   
        

    
    





        
    


if __name__ == "__main__":
    app.run(debug=True)
