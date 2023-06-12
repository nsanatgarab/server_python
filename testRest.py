from flask import Flask, request
from flask_restx import Resource, Api, fields

app = Flask(__name__)
api = Api(app)

# Exemple de données stockées en mémoire
data = {}

example_model = api.model('Example', {
    'param': fields.Integer(description='Le paramètre'),
    'value1': fields.Integer(description='La valeur 1'),
    'value2': fields.Integer(description='La valeur 2')
})

@api.route('/example/<int:param>')
class ExampleResource(Resource):
    @api.doc(responses={200: 'Valeur récupérée avec succès', 404: 'Paramètre non trouvé'})
    def get(self, param):
        # Votre code pour le GET avec un paramètre int
        if param in data:
            return data[param]
        else:
            return "Paramètre non trouvé", 404

    @api.expect(example_model, validate=True)
    @api.doc(responses={201: 'Données ajoutées avec succès'})
    def post(self):
        # Votre code pour le POST avec un paramètre string et deux int
        param = request.json['param']
        value1 = request.json['value1']
        value2 = request.json['value2']
        data[param] = (value1, value2)
        return "Données ajoutées avec succès", 201

    @api.doc(responses={200: 'Données supprimées avec succès', 404: 'Paramètre non trouvé'})
    def delete(self, param):
        # Votre code pour le DELETE avec un paramètre int
        if param in data:
            del data[param]
            return "Données supprimées avec succès", 200
        else:
            return "Paramètre non trouvé", 404

if __name__ == '__main__':
    app.run(debug=True)
