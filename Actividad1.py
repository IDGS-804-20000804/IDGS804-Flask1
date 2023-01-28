from flask import Flask
from flask import request

app = Flask(__name__)

@app.route("/suma", methods=["GET","POST"])
def suma():
    if request.method=="POST":
        num1 = request.form.get("num1")
        num2 = request.form.get("num2")
        opt =  request.form.get("opr")
        if opt == "suma":
            res = float(num1) + float(num2)
        if opt == "resta":
            res = float(num1) - float(num2)
        if opt == "multiplicacion":
            res = float(num1) * float(num2)
        if opt == "division":
            res = float(num1) / float(num2)
        return "<h1> La {0} es: {1} </h1>".format(opt, res)
    else: 
        return '''
            <form action = '/suma' method="POST">
                <label>N1: </label>
                <input type="text" name="num1"/></br></br>
                
                <label>N2: </label>
                <input type="text" name="num2"/></br></br>
    
                <p>Selecciona la operación:</p>
                <input type="radio" id="suma" name="opr" value="suma">
                <label for="suma">suma</label><br>
                <input type="radio" id="resta" name="opr" value="resta">
                <label for="resta">resta</label><br>  
                <input type="radio" id="age3" name="opr" value="100">
                <label for="multiplicacion">multiplicacion</label><br>
                <input type="radio" id="division" name="opr" value="multiplicacion">
                <label for="division">division</label><br><br>
                <input type="submit" value="Submit"> 
            </form>
        '''


if __name__ == "__main__":
    app.run(
        debug = True,
        port = 3000
    )

