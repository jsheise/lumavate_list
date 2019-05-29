from flask import Flask, render_template
from flask_restful import Resource, Api
from flask_triangle import Triangle

# data.py contains class information for entries
#from data import EntryData

app = Flask(__name__)
Triangle(app)

# EntryData = EntryData

# api = Api(app)
#
# class ListItem(Resource):
#     def get(self):
#         return render_template('list.html');
#
# api.add_resource(ListItem, '/')

@app.route('/')
def index():
    return render_template('list.html') #, entryData = EntryData)

if __name__ == '__main__':
    app.run(debug=True)
