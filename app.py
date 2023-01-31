import flask,requests,time
from flask import Flask, render_template, request

app=Flask(__name__,template_folder="html")




@app.route('/')
def index_html():
    return render_template('index.html')
@app.route('/api')
def api_request():
    api = request.args.get("url")
    print(api)
    response = requests.get(api)
    if response.headers.get('Content-Type').startswith('application/json'):
        print("true")
        return response.json()
    else:
        print("false")
        return response.text


app.run()