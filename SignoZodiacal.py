from flask import Flask
from flask import request
from flask import render_template
from datetime import datetime
from dateutil.relativedelta import relativedelta
    
app = Flask(__name__)

@app.route("/", methods = ["GET","POST"])
def index():
    return render_template("Actividad4Form.html")


@app.route("/resultadoActividad4", methods = ["POST"])
def resultadoActividad4():
    action = request.form.get("action")
    if action == "Siguiente":
        sexo = request.form.get("inputSexo")
        nombre = request.form.get("inputNombre")
        aMaterno = request.form.get("inputAMaterno")
        aPaterno = request.form.get("inputAPaterno")
        dia = request.form.get("inputDia")
        mes = request.form.get("inputMes")
        anio = request.form.get("inputAnio")
        return render_template("Actividad4Suma.html",
                                                sexo = sexo,
                                                nombre = nombre,
                                                aMaterno = aMaterno,
                                                aPaterno = aPaterno,
                                                dia = dia,
                                                mes = mes,
                                                anio = anio
        )
    else:
        return render_template("Actividad4Form.html")


@app.route("/resultadoFinalActividad4", methods = ["POST"])
def resultadoFinalActividad4():
    test1 = int(request.form.get("inputTest1") or 0);
    test2 = int(request.form.get("inputTest2") or 0);
    test3 = int(request.form.get("inputTest3") or 0);
    test4 = int(request.form.get("inputTest4") or 0);
    test5 = int(request.form.get("inputTest5") or 0);
    resultado = test1 + test2 + test3 + test4 + test5
    sexo = request.form.get("inputSexo")
    nombre = request.form.get("inputNombre")
    aMaterno = request.form.get("inputAMaterno")
    aPaterno = request.form.get("inputAPaterno")
    dia = int(request.form.get("inputDia") or 0)
    mes = int(request.form.get("inputMes") or 0)
    anio = int(request.form.get("inputAnio") or 0)
    signo = "Error al encontrar signo"
    path = "../static/img/"
    if mes == 1:
        if dia <= 20:
            signo = "Capricornio"
            path += "capricornio.png"
        else:
            signo = "Acuario"
            path += "aquario.png"
    elif mes == 2:
        if dia <= 18:
            signo = "Acuario"
            path += "aquario.png"
        else:
            signo = "Piscis"
            path += "piscis.png"
    elif mes == 3:
        if dia <= 20:
            signo = "Piscis"
            path += "piscis.png"
        else:
            signo = "Aries"
            path += "aries.png"
    elif mes == 4:
        if dia <= 20:
            signo = "Aries"
            path += "aries.png"
        else:
            signo = "Tauro"
            path += "tauro.png"
    elif mes == 5:
        if dia <= 21:
            signo = "Tauro"
            path += "tauro.png"
        else:
            signo = "Géminis"
            path += "geminis.png"
    elif mes == 6:
        if dia <= 21:
            signo = "Géminis"
            path += "geminis.png"
        else:
            signo = "Cáncer"
            path += "cancer.png"
    elif mes == 7:
        if dia <= 22:
            signo = "Cáncer"
            path += "cancer.png"
        else:
            signo = "Leo"
            path += "leo.png"
    elif mes == 8:
        if dia <= 23:
            signo = "Leo"
            path += "leo.png"
        else:
            signo = "Virgo"
            path += "virgo.png"
    elif mes == 9:
        if dia <= 23:
            signo = "Virgo"
            path += "virgo.png"
        else:
            signo = "Libra"
            path += "libra.png"
    elif mes == 10:
        if dia <= 23:
            signo = "Libra"
            path += "libra.png"
        else:
            signo = "Escorpio"
            path += "scorpio.png"
    elif mes == 11:
        if dia <= 22:
            signo = "Escorpio"
            path += "scorpio.png"
        else:
            signo = "Sagitario"
            path += "sagitario.png"
    elif mes == 12:
        if dia <= 21:
            signo = "Sagitario"
            path += "sagitario.png"
        else:
            signo = "Capricornio"
            path += "capricornio.png"
    
    stringDia = request.form.get("inputDia")
    stringMes = request.form.get("inputMes")
    stringAnio = request.form.get("inputAnio")
    
    fechaNacimietno = "{0}/{1}/{2}".format(stringDia, stringMes, stringAnio)
    objetoFechaNacimiento = datetime.strptime(fechaNacimietno, "%d/%m/%Y")
    edad = relativedelta(datetime.now(), objetoFechaNacimiento)

    return render_template("Actividad4Signo.html",
                            signo = signo,
                            resultado = resultado,
                            path = path,
                            sexo = sexo,
                            nombre = nombre,
                            aMaterno = aMaterno,
                            aPaterno = aPaterno,
                            dia = dia,
                            mes = mes,
                            anio = anio
    )


if __name__ == "__main__":
    app.run(
        debug = True,
        port = 3000
    )

