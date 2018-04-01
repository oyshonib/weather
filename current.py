import json, os

from flask import Flask, request, make_response


app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
	req = request.get_json(silent=True, force=True)
	print(json.dumps(req, indent=4))

	res = makeResponse(req)
	res = json.dumps(res, indent=4)
	r = make_response(res)
	r.headers['Content-Type'] = 'application/json'
	return r


#- start by returning the result back
#- try filling up the parameters ourselves

def makeResponse(req):
	result = req.get()
	parameters = result.get("parameters")
	city = parameters.get("geo-city")
	date = parameters.get("date")

	speech = "The forecast for"+city+ "for"+date+" is "
	return {
	"speech": speech,
	"displayText": speech,
	"source": "apiai-weather-webhook"
	}





