from flask import Flask
app = Flask(__name__)
global counter
counter = 0

@app.route('/')
def counterPage():
    global counter
    counter = counter + 1
    return 'Hello, world!'


@app.route('/asfd')
def logPage():
    with open("log.txt", "a") as myfile:
        myfile.write( str(counter) + "\n" )
    return str(counter)

counterPage()
logPage()