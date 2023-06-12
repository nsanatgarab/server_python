from flask import Flask, request
from flask_restx import Resource, Api, fields

app = Flask(__name__)
api = Api(app)

# Example in-memory data
data = {}

example_model = api.model('Example', {
    'param': fields.Integer(description='The parameter'),
    'value1': fields.Integer(description='Value 1'),
    'value2': fields.Integer(description='Value 2')
})

@api.route('/example/<int:param>')
class ExampleResource(Resource):
    @api.doc(responses={200: 'Value retrieved successfully', 404: 'Parameter not found'})
    def get(self, param):
        # Your code for GET with an integer parameter
        if param in data:
            return data[param]
        else:
            return "Parameter not found", 404

    @api.expect(example_model, validate=True)
    @api.doc(responses={201: 'Data added successfully'})
    def post(self):
        # Your code for POST with a string parameter and two integers
        param = request.json['param']
        value1 = request.json['value1']
        value2 = request.json['value2']
        data[param] = (value1, value2)
        return "Data added successfully", 201

    @api.doc(responses={200: 'Data deleted successfully', 404: 'Parameter not found'})
    def delete(self, param):
        # Your code for DELETE with an integer parameter
        if param in data:
            del data[param]
            return "Data deleted successfully", 200
        else:
            return "Parameter not found", 404

if __name__ == '__main__':
    app.run(debug=True)
