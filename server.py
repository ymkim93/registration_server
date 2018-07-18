from flask import Flask, request
import json

app = Flask(__name__)

@app.route('/create', method=['POST'])
def test():
	dict_d = json.loads(request.json)

if __name__=='__main__':
	app.run(host='0.0.0.0')
