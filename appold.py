#from flask import Flask, render_template,request
#este script hace el backende la bd en postgres
# hay que cambiar el nombre de la Bd por PetHotel y la clave por la clave de su gestor de bd quedaria como la sgte linea reemplazar en todos 
# conn=psycopg2.connect(user='postgres',password='suclave',host='127.0.0.1',port='5432',database='PetHotel')
from flask import Flask, render_template, json,jsonify, request

import psycopg2

app = Flask(__name__)


@app.route("/")

def main():

    return render_template('login1.html')




#link al index.html
@app.route('/showSignIndex')
def showSignIndex():
    return render_template('indexPH.html')




@app.route('/showSignUp')
def showSignUp():
    return render_template('signup.html')







@app.route('/showSignIni')

def showSignIni():

    return render_template('centroPH.html')






@app.route('/showSignUpE')
def showSignUpE():

    return render_template('NuevoEmp.html')

#Eliminar empleado
@app.route('/showSignUpDelE')
def showSignUpDelE():

    return render_template('DeleteEmp.html')

#Eliminar cliente
@app.route('/showSignUpDelC')
def showSignUpDelC():

    return render_template('DeleteCli.html')

#Update cliente
@app.route('/showSignUpDC')
def showSignUpDC():

    return render_template('updateCli.html')

#Update empleado
@app.route('/showSignUpDE')
def showSignUpDE():

    return render_template('updateEmp.html')


#crear habitacion
@app.route('/showSignUpH')
def showSignUpH():

    return render_template('NuevaHab.html')

#reservar habitacion
@app.route('/showSignUpRH')
def showSignUpRH():

    return render_template('ReservaHab.html')
#mostrar reporte
@app.route('/showSignUpRepo')
def showSignUpRepo():

    return render_template('reporte.html')

#mostrar factura
@app.route('/showSignUpFac')
def showSignUpFac():

    return render_template('FacturarHab.html')
 #nuevo proveedor   
@app.route('/showSignUpNP')
def showSignUpNP():

    return render_template('NuevoProv.html')



# create user code will be here !!

#crear nuevo cliente

@app.route('/signUp',methods=['POST'])

def signUp():
        conn=psycopg2.connect(user='postgres',password='1234',host='127.0.0.1',port='5432',database='pethotel')
    # create user code will be here !!
        id1 = request.form['txtIdSocio']
        nombre = request.form['txtNombres']
        tel = request.form['txtTelefono']
        dire = request.form['txtDireccion']
        tm = request.form['txtTipoM']
        ti = request.form['txtTarjetaI']
        correo = request.form['txtEmail']
        status1 = request.form['txtStatus']
         
        cursor = conn.cursor()
        #recoelccion de datos
        datos=(id1,nombre,tel,dire,tm,ti,correo,status1)   
        sql='INSERT INTO public."Clientes" ("ID_Cliente", "Nombre_cliente", "Telefono", "Direccion", "Tipo_Mascota", "Tarjeta_ingreso", "Email", "Status") VALUES(%s,%s,%s,%s,%s,%s,%s,%s)'
        # usamos execute
    
        cursor.execute(sql,datos)
        conn.commit()
        cursor.close()
        msg="Dato Grabado Correctamente!" 
        return msg
        #render_template('mensajeOk.html',msg=msg)
        #return 

#grabar datos del Empleado
@app.route('/signUpEmp',methods=['POST'])
def signUpEmp():
        conn=psycopg2.connect(user='postgres',password='1234',host='127.0.0.1',port='5432',database='pethotel')
    # create user code will be here !!
        id1 = request.form['txtCarnet']
        nombre = request.form['txtNombres']
        tel = request.form['txtTelefono']
        dire = request.form['txtDireccion']
        cargo = request.form['txtCargo']
        salario = request.form['txtSalario']
        prof = request.form['txtProfesion']
        fecha = request.form['txtFecha']
        area = request.form['txtArea']
        jornada = request.form['selJornada']
        user = request.form['txtUser']
        clave = request.form['txtClave']
        status1= request.form['txtStatus']
        
        cursor = conn.cursor()
        #recoelccion de datos
        datos=(id1,nombre,tel,dire,cargo,salario,prof,fecha,area,jornada,user,clave,status1)   
        sql='INSERT INTO public."Empleados" ("Carnet", "Nombre_empleado", "Telefono", "Direccion", "Cargo", "Salario", "Profesion","Fecha_de_inicio","Area_trabajo","Jornada","User","Password","Status") VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
        # usamos execute
    
        cursor.execute(sql,datos)
        conn.commit()
        cursor.close()
       # return"Error" 


          
@app.route("/signUpDelE", methods=['POST'])
def signUpDelE():
    
        carnet = request.form['txtCarnet']
        
        # Conexión a la base de datos
        conn=psycopg2.connect(user='postgres',password='1234',host='127.0.0.1',port='5432',database='pethotel')
        
        # Crear un cursor para ejecutar las consultas
        cur = conn.cursor()
        # Buscar y eliminar el dato en la tabla Empleados
        cur.execute(f'DELETE FROM "Empleados" WHERE "Carnet" = {carnet}')
        conn.commit()
        # Cerrar la conexión a la base de datos
        cur.close()
        conn.close()
        # Mostrar un mensaje indicando si se eliminó o no el dato
        if cur.rowcount > 0:
          mensaje = "El Empleado con carnet {} ha sido eliminado.".format(carnet)
        else:
          mensaje = "No se encontró ningún empleado con carnet {}.".format(carnet)

        return mensaje
       

@app.route("/signUpDelC", methods=['POST'])
def signUpDelC():
    
        carnet = request.form['txtCarnet']
        id1= str(carnet)

        # Conexión a la base de datos
        conn=psycopg2.connect(user='postgres',password='1234',host='127.0.0.1',port='5432',database='pethotel')
        
        # Crear un cursor para ejecutar las consultas
        cur = conn.cursor()
        # Buscar y eliminar el dato en la tabla Empleados
        #sql='DELETE FROM Clientes WHERE ID_Cliente =%s'
        cur.execute(f'DELETE FROM "Clientes" WHERE "ID_Cliente" ={carnet}')
        #cur.execute('DELETE FROM "Clientes" WHERE "ID_Cliente" = %s')
        
        #cur.execute(sql,str(id1))
       # delete from "Clientes" where "ID_Cliente"= '7';
        conn.commit()
        # Cerrar la conexión a la base de datos
        cur.close()
        conn.close()
        # Mostrar un mensaje indicando si se eliminó o no el dato
        if cur.rowcount > 0:
          mensaje = "El Cliente con Id {} ha sido eliminado.".format(carnet)
        else:
          mensaje = "No se encontró ningún Cliente con Id {}.".format(carnet)
#delete  from "Clientes" where "ID_Cliente"='98390345'; 
        return mensaje
         
         
# actualizar cliente
# Conexión a la base de datos
conn=psycopg2.connect(user='postgres',password='1234',host='127.0.0.1',port='5432',database='pethotel')
@app.route('/signUpdateC', methods=['GET', 'POST'])
def signUpdateC():
    if request.method == 'POST':
        id1 = request.form['txtIdSocio']
        nombre = request.form['txtNombres']
        tel = request.form['txtTelefono']
        dire = request.form['txtDireccion']
        tm = request.form['txtTipoM']
        ti = request.form['txtTarjetaI']
        correo = request.form['txtEmail']
        status1 = request.form['txtStatus']
         
           
        # Realizar la búsqueda del ID_Cliente en la tabla "clientes"
        cursor = conn.cursor()
        cursor.execute(f'SELECT * FROM "Clientes" WHERE "ID_Cliente" ={id1}')
        cliente = cursor.fetchone()

        if cliente:
            # Actualizar los datos del cliente en la tabla "clientes"
            #  "ID_Cliente", "Nombre_cliente", "Telefono", "Direccion", "", "Tarjeta_ingreso", "Email", "Status") 
            cursor.execute('UPDATE "Clientes" SET "Nombre_cliente" = %s, "Telefono" = %s, "Direccion" = %s, "Tipo_Mascota"=%s,"Tarjeta_ingreso" = %s,"Email" = %s,"Status" = %s WHERE "ID_Cliente" = %s',(nombre,tel,dire,tm,ti,correo,status1,id1))
            conn.commit()

            mensaje = "Los datos han sido actualizados en la tabla 'clientes'."
            return mensaje
        else:
            mensaje = "No se encontró el ID_Cliente en la tabla 'clientes'."
            return mensaje
            #return render_template('mensaje.html', mensaje=mensaje)

    #return render_template('updatecli.html')  
  
 # actualizar Empelado
# Conexión a la base de datos
conn=psycopg2.connect(user='postgres',password='1234',host='127.0.0.1',port='5432',database='pethotel')
@app.route('/signUpdatE', methods=['GET', 'POST'])
def signUpdatE():
    if request.method == 'POST':
        id1 = request.form['txtCarnet']
        nombre = request.form['txtNombres']
        tel = request.form['txtTelefono']
        dire = request.form['txtDireccion']
        cargo = request.form['txtCargo']
        salario = request.form['txtSalario']
        prof = request.form['txtProfesion']
        fecha = request.form['txtFecha']
        area = request.form['txtArea']
        jornada = request.form['selJornada']
        user = request.form['txtUser']
        clave = request.form['txtClave']
        status1= request.form['txtStatus']
         
           
        # Realizar la búsqueda del ID_Cliente en la tabla "clientes"
        cursor = conn.cursor()
        cursor.execute(f'SELECT * FROM "Empleados" WHERE "Carnet" ={id1}')
        empleado = cursor.fetchone()

        if empleado:
            # Actualizar los datos del cliente en la tabla "clientes"
            
            cursor.execute('UPDATE "Empleados" SET "Nombre_empleado" = %s, "Telefono" = %s, "Direccion" = %s, "Cargo"=%s,"Salario" = %s,"Profesion" = %s,"Fecha_de_inicio" = %s,"Area_trabajo" = %s,"Jornada" = %s,"User" = %s,"Password"= %s,"Status" = %s WHERE "Carnet" = %s',(nombre,tel,dire,cargo,salario,prof,fecha,area,jornada,user,clave,status1,id1))
            conn.commit()

            mensaje = "Los datos del Empleado han sido actualizados en la tabla 'Empleados'."
            return mensaje
        else:
            mensaje = "No se encontró el Carnet en la tabla 'Empleados'."
            return mensaje
            #return render_template('mensaje.html', mensaje=mensaje)

    #return render_template('updatecli.html')   
#grabar los datos en la tabla habitaciones
          
@app.route('/signUpH',methods=['POST'])

def signUpH():
        conn=psycopg2.connect(user='postgres',password='1234',host='127.0.0.1',port='5432',database='pethotel')
    # create user code will be here !!
        id1 = request.form['txtIdh']
        tipo = request.form['txtTipo']
        dispo = request.form['selDispo']
        precio1 = request.form['txtPrecio']
        descu = request.form['txtDesc']
       
         
        cursor = conn.cursor()
        #recoelccion de datos
        datos=(id1,tipo,dispo,precio1,descu)   
        sql='INSERT INTO public."Habitaciones" ("No_Habitacion", "Tipo_Habitacion", "Disponibilidad", "Precio", "Descripcion_Habitacion") VALUES(%s,%s,%s,%s,%s)'
        # usamos execute
    
        cursor.execute(sql,datos)
        conn.commit()
        cursor.close()
       # return"Error" 

#reservar habitacion
@app.route('/signUpRH',methods=['POST'])

def signUpRH():
        conn=psycopg2.connect(user='postgres',password='1234',host='127.0.0.1',port='5432',database='pethotel')
    # create user code will be here !!
        id1 = request.form['txtIdrh']
        cliente = request.form['txtCliente']
        fecha1 = request.form['txtFl']
        fecha2 = request.form['txtFs']
        tipoh = request.form['txtTh']
        desc = request.form['txtDesc']
        servicio = request.form['txtServ']
        status1 = request.form['selStatus']
         
        cursor = conn.cursor()
        #recoelccion de datos
        datos=(id1,cliente,fecha1,fecha2,tipoh,desc,servicio,status1)   
        sql='INSERT INTO public."Reservaciones" ("No_Reservacion", "Nombre_Cliente", "Fecha_llegada", "Fecha_salida", "Tipo_Habitacion", "Descripcion_Habitacion", "Servicio_Adicional", "Status") VALUES(%s,%s,%s,%s,%s,%s,%s,%s)'
        # usamos execute
    
        cursor.execute(sql,datos)
        conn.commit()
        cursor.close()
       # return"Error" 

@app.route('/signUpReporte',methods=['POST'])
def signUpReporte():
    # Consulta a la base de datos para obtener los datos de la tabla Habitaciones
    conn=psycopg2.connect(user='postgres',password='1234',host='127.0.0.1',port='5432',database='pethotel')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM "Habitaciones"')
    habitaciones = cursor.fetchall()
        
    #endfor
    cursor.close()
    conn.close()
    # Convertir los datos obtenidos en un diccionario
    datos_habitaciones = []
    for habitacion in habitaciones:
        datos_habitaciones.append({
            'No_Habitacion': habitacion[0],
            'Tipo_Habitacion': habitacion[1],
            'Disponibilidad': habitacion[2]
        })

    # Devolver los datos como JSON
    #return jsonify(datos_habitaciones)

    
    
    # Renderizar el template "reporte.html" con los datos obtenidos de la base de datos
    return render_template('reporte1.html',habitaciones=habitaciones)
    #return habitaciones
    #return render_template("reporte1.html",habitaciones)
    
    
#grabar datos del Proveedor
@app.route('/signUpNP',methods=['POST'])
def signUpNP():
        conn=psycopg2.connect(user='postgres',password='1234',host='127.0.0.1',port='5432',database='pethotel')
    # create user code will be here !!
        id1 = request.form['txtNit']
        nombre = request.form['txtNombres']
        emp = request.form['txtEmp']
        tel = request.form['txtTelefono']
        dire = request.form['txtDireccion']
        correo = request.form['txtCorreo']
        tprod = request.form['txtTipoP']
        status1= request.form['txtStatus']
        
        cursor = conn.cursor()
        #recoelccion de datos
        datos=(id1,nombre,emp,tel,dire,correo,tprod,status1)   
        sql='INSERT INTO public."Proveedores" ("Nit","Nombre_Contacto","Empresa","Telefono", "Direccion", "Email", "Tipo_Producto","Status") VALUES(%s,%s,%s,%s,%s,%s,%s,%s)'
        # usamos execute
    
        cursor.execute(sql,datos)
        conn.commit()
        cursor.close()
       # return"Error" 
       
       
       
#realizar el login en la bd

conn=psycopg2.connect(user='postgres',password='1234',host='127.0.0.1',port='5432',database='pethotel')
@app.route('/signUpLogin',methods=['GET', 'POST'])
def signUpLogin():

 if request.method == 'POST':
        user = request.form['txtUser']
        password = request.form['txtPass']
        
        # Realizar la consulta a la tabla Empleados
        cursor = conn.cursor()
        #select  * from "Empleados" where "User"='qw' and "Password" ='qw';
        cursor.execute('SELECT "User","Password" FROM "Empleados" WHERE "User" = %s AND "Password" = %s', (user, password))
        result = cursor.fetchone()
        
        if result:
            #return 'El empleado se encontró'
            return render_template('indexPH.html')
        else:
            #return 'El empleado no se encontró'
            return render_template('Error1.html')
    
 #return render_template('/indexPH')


    

@app.route('/indexPH')
def indexPH():
    return render_template('indexPH.html')
       
    
    
    

@app.errorhandler(404)
def page_not_found(error):
    return render_template("error.html", error="Página no encontrada..."), 404

if __name__ == "__main__":

    app.run()
