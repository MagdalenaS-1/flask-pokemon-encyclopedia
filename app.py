from flask import Flask

app = Flask(__name__)


@app.get("/")
def pokemon_list():
    return "bulbasaur, charmander, pikachu, eevee, diglet"

@app.get("/bulbasaur")
def bulbasaur_data():
    return "This is bulbasaur, a generation 1 pokemon who looks like a little dinosaur"

@app.get("/charmander")
def charmander_data():
    return "This is charmander, a generation 1 pokemon who looks like a little dragon"

@app.get("/pikachu")
def pikachu_data():
    return "This is pikachu, a generation 1 pokemon who looks like a little rodent"

@app.get("/eevie")
def eevie_data():
    return "This is eviee, a generation 1 pokemon who looks like a tiny fox"

@app.get("/diglet")
def diglet_data():
    return "This is diglet, a generation 1 pokemon who looks like a mole"


if __name__ == "__main__":
    app.run()