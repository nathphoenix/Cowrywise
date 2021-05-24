from flask import Flask, jsonify, Blueprint, send_from_directory
from flask_restful import Api
from flask_cors import CORS
import os
from flask_mongoengine import MongoEngine

# import your resources here.
from .resources.uuid_resource import Generate_ids


app = Flask(__name__, instance_relative_config=True, static_url_path='', static_folder='static/')
# api = Api(app)

app.url_map.strict_slashes = False

CORS(app, resources={r'/v1/*'})
db = MongoEngine(app)



api_blueprint = Blueprint('api', __name__)
api = Api(api_blueprint)

# define your endpoints here.
#api.add_resource(Summary, "/summary", "/blogger/<path:article_URL>", endpoint='summary')
api.add_resource(Generate_ids, '/generate', endpoint='generate')

app.register_blueprint(api_blueprint, url_prefix='/v1')


@app.route('/')
def home():
    return jsonify({
        "message": "Welcome Home!"
    })


@app.route('/v1')
def v1_home():
    return jsonify({
        "message": "Welcome Home v1 API!"
    })

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(os.getcwd(), 'static'), 'apple-touch-icon.png')

@app.errorhandler(404)
def route_not_found(error):
    return jsonify({
        "message": "Route not found."
    }),


if __name__ == "__main__":
    print(True)
    port = int(os.environ.get('PORT', 5000))
    app.run(port=port, host='127.0.0.1', debug=True)



