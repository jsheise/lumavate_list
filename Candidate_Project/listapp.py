from flask import Flask, render_template
from flask_restful import Resource, Api

app = Flask(__name__)

# api = Api(app)
#
# class ListItem(Resource):
#     def get(self):
#         return render_template('list.html');
#
# api.add_resource(ListItem, '/')

@app.route('/')
def index():
        return render_template('list.html')

if __name__ == '__main__':
    app.run(debug=True)
