import flask

app = flask.Flask(__name__)
app.config["DEBUG"] = True


@app.route('/', methods=['GET'])
def home():
    return "<h1>Distant Reading Archive</h1><p>This site is a prototype API for Flask web Framework.</p>"


@app.route('/poststuff', methods=['POST'])
def postStuff():
    title = flask.request.json['title']
    return flask.jsonify(title)
    
if __name__ == '__main__':
    app.run()