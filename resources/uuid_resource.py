from flask_restful import Resource, reqparse
from ..functions.get_uuid import generate_uuid


class Generate_ids(Resource):
    def get(self):
        try:
            result = generate_uuid()
            payload = result

            return {
                'status': 'success',
                'data': payload,
                'message': 'Operation successful'
            }, 200

        except Exception as e:
            return {
               'status': 'failed',
               'data': None,
               'message': str(e)
            }, 500
