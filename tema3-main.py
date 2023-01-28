from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "<h1>Hello, World!</h1>"

@app.route("/hi")
def hi():
    return "<h1>Welcome!</h1>"

@app.route("/user/<string:user>")
def user(user):
    return "<h1>Hola {0}!</h1>".format(user)

@app.route("/edad/<int:edad>")
def edad(edad):
    return "<h1>Tu edad es de {0}!</h1>".format(edad)

@app.route("/username/<int:id>/<string:username>")
def username(id, username):
    return "<h1>Username: {0} <p>Id: {1}</p>!</h1>".format(username,id)

@app.route("/suma/<float:num1>/<float:num2>")
def suma(num1, num2):
    return "<h1>La suma de {0} y {1} es  {2}</h1>".format(num1, num2, num1 + num2)


if __name__ == "__main__":
    app.run(
        debug = True,
        port = 3000
    )
