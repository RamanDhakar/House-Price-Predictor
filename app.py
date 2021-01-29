import flask
from flask import request
app = flask.Flask(__name__)
#app.config["DEBUG"] = True

from flask_cors import CORS
CORS(app)

# main index page route
@app.route('/')
def home():
    return '<h1>API is working.. </h1>'

@app.route('/predict',methods=['GET'])
def predict():
    import joblib
    model = joblib.load('house_price_predict_model.ml')
    predicted_price = model.predict([[float(request.args['rm']),
                            float(request.args['zn']),
                            float(request.args['age']),
                            float(request.args['rad']),
                            float(request.args['crim']),
                            float(request.args['nox']),
                            float(request.args['tax']),
                            float(request.args['indus']),
                            float(request.args['ptratio']),
                            float(request.args['lstat']),
                                               ]])
    
    return str(round(predicted_price[0],2))


if __name__ == "__main__":
    app.run(debug=True)
