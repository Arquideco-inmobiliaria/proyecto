from  flask import Flask , render_template, request
from flaskext.mysql import MySQL
app=Flask(__name__)

#conexion con la base de datos
mysql=MySQL()
app.config['MySQL_DATABASE_HOST']='localhost'
app.config['MySQL_DATABASE_USER']='root'
app.config['MySQL_DATABASE_PASSWORD']=''
app.config['MySQL_DATABASE_DB']='arquideco'
app.config['MYSQL_PORT'] = 3306
mysql.init_app(app)

#direccionamiento al index
@app.route('/')
def index():
    return render_template('index.html')


@app.route('/registrar')
def registrar():
    sql="INSERT INTO `usuario` (`IdUsuario`, `nombre`, `apellido`, `correo`, `fechaNacimiento`, `edad`, `telefono`, `direccion`, `tipoGenero`, `tipoDocumento`, `password`, `password2`, `fk_IdRol`, `fk_IdAgenda`) VALUES (NULL, 'milo', NULL, 'milo@gey.com', NULL, NULL, '3052257849', '', NULL, NULL, '123456', '123456', '2', NULL);"

    conn=mysql.connect()
    cursor=conn.cursor()
    cursor.execute(sql)
    conn.comit()
    return render_template('registrar.html')

@app.route('/reg', methods=['POST'])
def reg():
    _nombre=request.form['usua_nombre']
    _correo=request.form['clie_correo']
    _celular=request.form['clie_telefono']
    _cont=request.form['usua_clave']
    _cont2=request.form['usua_clave2']
    #if _cont==_cont2:
    sql="INSERT INTO `usuario` (`IdUsuario`, `nombre`, `apellido`, `correo`, `fechaNacimiento`, `edad`, `telefono`, `direccion`, `tipoGenero`, `tipoDocumento`, `password`, `password2`, `fk_IdRol`, `fk_IdAgenda`) VALUES (NULL, 'milo', NULL, 'milo@gey.com', NULL, NULL, '3052257849', '', NULL, NULL, '123456', '123456', '2', NULL);"

    #sql="INSERT INTO `usuario` (`IdUsuario`, `nombre`, `apellido`, `correo`, `fechaNacimiento`, `edad`, `telefono`, `direccion`, `tipoGenero`, `tipoDocumento`, `password`, `password2`, `fk_IdRol`, `fk_IdAgenda`) VALUES (NULL, %s, NULL, '%s', NULL, NULL, '%s', 'NULL', NULL, NULL, '%s', '%s', '2', NULL);"
    #datos=(_nombre,_correo,_celular,_cont,_cont2)
    conn=mysql.connect()
    cursor=conn.cursor()
    cursor.execute(sql)
    conn.comit()
    return render_template('index.html')
    #else:
     #print("uwu")
    # return render_template('register.html')


    

if __name__=='__main__':
    app.run(debug=True)