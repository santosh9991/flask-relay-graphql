from flask import Flask,request,jsonify
from flask_graphql import GraphQLView

from models import *
from schema import schema
import os
app = Flask(__name__)
app.debug = os.getenv('debug',True)
app.add_url_rule(
    '/graphql',
    view_func=GraphQLView.as_view(
        'graphql',
        schema=schema,
        graphiql=True # for having the GraphiQL interface
    )
)

@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()

if __name__ == '__main__':
    app.run(host="0.0.0.0",port=8002)
