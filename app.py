from flask import Flask, redirect, render_template, request, url_for
from flaskext.mysql import MySQL

app = Flask(__name__)

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

#hace la verificacion de coneccion y regresa a la vista inmueble
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
        

#INICIO DE SESION



@app.route('/login', methods=['POST'])
def login():
    #verificacion de metodo, sirve para saber si esta haciendo el envio de los datos
        print(request.form["usuaname"])
        print(request.form["usupass"])
        return render_template("login.html")



if __name__ == "__main__":
    app.run(debug=True)
