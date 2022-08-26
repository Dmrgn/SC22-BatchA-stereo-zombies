# import requirements needed
from flask import Flask, render_template, request
from utils import get_base_url
import json
from aitextgen import aitextgen

# setup the webserver
# port may need to be changed if there are multiple flask servers running on same server
port = 33930
base_url = get_base_url(port)

app = Flask(__name__, static_url_path=base_url+'static')

ai = aitextgen(model_folder="model_folder")

# set up the routes and logic for the webserver
@app.route(f'{base_url}', methods = ['POST'])
def getData():
    print(request.json)
    responses = []
    # create 5 responses for each query
    for x in range(5):
        responses.append(ai.generate_one(prompt=request.json['prompt'], temperature=float(request.json['temp'])/10, max_length=100).split("\n")[0])
        print(responses)
    return json.dumps({'message':responses})

# set up the routes and logic for the webserver
@app.route(f'{base_url}', methods = ['GET'])
def home():
    return render_template('index.html')

if __name__ == '__main__':
    # IMPORTANT: change url to the site where you are editing this file.
    website_url = 'https://cocalc4.ai-camp.dev'
    
    print(f'Try to open\n\n    https://{website_url}' + base_url + '\n\n')
    app.run(host = '0.0.0.0', port=port, debug=True)
