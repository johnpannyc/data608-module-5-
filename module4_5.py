from flask import Flask, jsonify, Response
import pandas as pd

app = Flask(__name__)

def readDataFirstData():
    url = "https://data.cityofnewyork.us/resource/nwxe-4ae8.json?$limit=5000"
    df = pd.read_json(url)
    df.dropna(inplace=True)
    return df

df = readDataFirstData()

@app.route('/')
def home():
	html_data =''
	html_data = html_data + '<!DOCTYPE html>'
	html_data = html_data + '<html>'
	html_data = html_data + '<head>'
	html_data = html_data + '<style>'
	html_data = html_data + 'table {'
	html_data = html_data + '  border-collapse: collapse;'
	html_data = html_data + '  width: 100%;'
	html_data = html_data + '}'
	html_data = html_data + 'th, td {'
	html_data = html_data + '  text-align: center;'
	html_data = html_data + '  padding: 8px;'
	html_data = html_data + '}'
	html_data = html_data + 'tr:nth-child(even){background-color: #f2f2f2}'
	html_data = html_data + 'th {'
	html_data = html_data + '  background-color: #4CAF50;'
	html_data = html_data + '  color: white;'
	html_data = html_data + '}'
	html_data = html_data + '</style>'
	html_data = html_data + '</head>'
	html_data = html_data + '<body>'
	html_data = html_data + '<center><h2>API Information</h2></center>'
	html_data = html_data + '<table>'
	html_data = html_data + '  <tr>'
	html_data = html_data + '    <th>URL</th>'
	html_data = html_data + '    <th>Parameter</th>'
	html_data = html_data + '    <th>Description</th>'
	html_data = html_data + '  </tr>'
	html_data = html_data + '  <tr>'
	html_data = html_data + '    <td>/</td>'
	html_data = html_data + '    <td>-</td>'
	html_data = html_data + '    <td>Shows current page</td>'
	html_data = html_data + '  </tr>'
	html_data = html_data + '  <tr>'
	html_data = html_data + '    <td>/borough</td>'
	html_data = html_data + '    <td>-</td>'
	html_data = html_data + '    <td>Shows the Borough of trees</td>'
	html_data = html_data + '  </tr>'
	html_data = html_data + '  <tr>'
	html_data = html_data + '    <td>/borough</td>'
	html_data = html_data + '    <td>/{type}</td>'
	html_data = html_data + '    <td>Filters Borough based on parameter type</td>'
	html_data = html_data + '  </tr>'
	html_data = html_data + '  <tr>'
	html_data = html_data + '    <td>/borough</td>'
	html_data = html_data + '    <td>/{type}/limit/{limit}</td>'
	html_data = html_data + '    <td>Filters Borough based on parameter type and limits result based on limit</td>'
	html_data = html_data + '  </tr>'
	html_data = html_data + '  <tr>'
	html_data = html_data + '    <td>/species</td>'
	html_data = html_data + '    <td>-</td>'
	html_data = html_data + '    <td>Show trees species</td>'
	html_data = html_data + '  </tr>'
	html_data = html_data + '  </tr>'
	html_data = html_data + '  <tr>'
	html_data = html_data + '    <td>/species</td>'
	html_data = html_data + '    <td>/{type}</td>'
	html_data = html_data + '    <td>Show trees information based on type</td>'
	html_data = html_data + '  </tr>'
	html_data = html_data + '  <tr>'
	html_data = html_data + '    <td>/species</td>'
	html_data = html_data + '    <td>/{type}/limit/{limit}</td>'
	html_data = html_data + '    <td>Show trees information based on type and limits data using limit</td>'
	html_data = html_data + '  </tr>'
	html_data = html_data + '  <tr>'
	html_data = html_data + '    <td>/health</td>'
	html_data = html_data + '    <td>-</td>'
	html_data = html_data + '    <td>Show trees health types</td>'
	html_data = html_data + '  </tr>'
	html_data = html_data + '  <tr>'
	html_data = html_data + '    <td>/health</td>'
	html_data = html_data + '    <td>{type}</td>'
	html_data = html_data + '    <td>Show trees based on health type</td>'
	html_data = html_data + '  </tr>'
	html_data = html_data + '  <tr>'
	html_data = html_data + '    <td>/health</td>'
	html_data = html_data + '    <td>{type}/limit/{limit}</td>'
	html_data = html_data + '    <td>Show trees based on health type and limits data using limit</td>'
	html_data = html_data + '  </tr>'
	html_data = html_data + '</table>'
	html_data = html_data + '</body>'
	html_data = html_data + '</html>'


	return html_data

@app.route('/borough', methods=['GET'])
def return_borough():
	return jsonify(list(df.boroname.unique()))

@app.route('/borough/<string:word>')
def return_borough_wise_data(word):
	broough_df = df[df['boroname']==word]
	resp = Response(response=broough_df.to_json(orient='records'), status=200, mimetype="application/json")
	return resp
	
@app.route('/borough/<string:word>/limit/<int:limit>')
def return_borough_wise_data_limit(word,limit):
	broough_df = (df[df['boroname']==word]).head(n=limit)
	resp = Response(response=broough_df.to_json(orient='records'), status=200, mimetype="application/json")
	return resp

@app.route('/species')
def species():
	return jsonify(list(df.spc_common.unique()))

@app.route('/species/<string:word>')
def species_spc_common(word):
	spc_common = (df[df['spc_common']==word])
	resp = Response(response=spc_common.to_json(orient='records'), status=200, mimetype="application/json")
	return resp
	
@app.route('/species/<string:word>/limit/<int:limit>')
def species_spc_common_limit(word,limit):
	spc_common = (df[df['spc_common']==word]).head(n=limit)
	resp = Response(response=spc_common.to_json(orient='records'), status=200, mimetype="application/json")
	return resp

@app.route('/health')
def health():
	return jsonify(list(df.health.unique()))
	
@app.route('/health/<string:word>')
def health_type_limit(word):
	health_df = df[df['health']==word]
	resp = Response(response=health_df.to_json(orient='records'), status=200, mimetype="application/json")
	return resp
	
@app.route('/health/<string:word>/limit/<int:limit>')
def health_type(word, limit):
	health_df = (df[df['health']==word]).head(n=limit)
	resp = Response(response=health_df.to_json(orient='records'), status=200, mimetype="application/json")
	return resp

if __name__ == '__main__':
	app.run(host='127.0.0.1', port=8080, debug=True)
