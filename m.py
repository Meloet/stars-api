import pandas as pd
from flask import Flask, jsonify, request
app = Flask(__name__)
df=pd.read_csv('calcutate.csv')
mass=df['mass'].tolist()
radi=df['radious'].tolist()
grav=df['gravity'].tolist()
dist=df['distance'].tolist()
data=[
    {
        'mass':mass,
        'radi':radi,
        'grav':grav,
        'dist':dist
    }
]
@app.route('/stars')
def show():
    return jsonify({
        'data':data
    })
if(__name__=="__main__"):
    app.run(debug=True)