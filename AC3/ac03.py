import os
from flask import Flask, render_template, json, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/exemplo', methods=['POST'])
def exempo():

    json = request.get_json()
    name = json['name'].upper()
    team = json['team'].upper()
    position = json['position'].upper()
    return jsonify(name=name, team=team, position=position)




if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5050))
    app.run(host='0.0.0.0', port=port)