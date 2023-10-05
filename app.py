
from flask import Flask, redirect, render_template, request, url_for
from flaskext.mysql import MySQL

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
    return render_template("DescripcionInmueble.html")
@app.route("/cat")
def cat():
    return render_template("inmueble.html")


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
