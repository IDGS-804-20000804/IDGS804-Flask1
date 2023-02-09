from flask import Flask
from flask import request
from flask import render_template
import math

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("Cinepolis.html")


@app.route("/resultadosCinepolis", methods = ["POST"])
def resultadosCinepolis():
    nombre = request.form.get("inputNombre")
    cantidadCompradores = int(request.form.get("inputCantidadCompradores") or 0)
    tarjetaCineco = "NO"
    if request.form.get("radioTarjetaCineco") == "true":
        tarjetaCineco = "SI"
    cantidadBoletas = int(request.form.get("inputCantidadBoletas"))
    boletosPermitidos = cantidadCompradores * 7
    mensaje = ""
    descuento = 0
    valorPagar = 0
    if( boletosPermitidos < cantidadBoletas):
        mensaje = "No se pueden comprar tantos boletos"
    else :
        if( cantidadBoletas > 5):
            descuento = 15
        elif ( cantidadBoletas >= 3 ):
            descuento = 10
        else:
            descuento = 0
        subTotal = cantidadBoletas * 12
        valorPagar = subTotal * ( (100-descuento)/100 )
        if request.form.get("radioTarjetaCineco") == "true":
            valorPagar = valorPagar * 0.9
    return render_template("Cinepolis2.html",
                           nombre = nombre,
                           cantidadCompradores = cantidadCompradores,
                           tarjetaCineco = tarjetaCineco,
                           cantidadBoletas = cantidadBoletas,
                           boletosPermitidos = boletosPermitidos,
                           valorPagar = valorPagar,
                           mensaje = mensaje
    )

if __name__ == "__main__":
    app.run(
        debug = True,
        port = 3000
    )

