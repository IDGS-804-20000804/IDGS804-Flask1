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
def username(id,username):
    return "<h1>Username: {0} <p>Id: {1}</p>!</h1>".format(username,id)


if __name__ == "__main__":
    app.run(
        debug = True,
        port = 3000
    )
