'''
Jayati Samar
Last edited: 08/13/2024
CS6620: Cloud Computing - Final Project
Objective: This file sets up an S3 bucket that can contain weather and location measurements and hosts the website
'''
from flask import Flask, request, jsonify, render_template
import boto3
import os
import json

def create_app():
	app = Flask(__name__)
	return app
	
app = create_app()

# S3 bucket configuration 
aws_access_key_id = os.environ.get('AWS_ACCESS_KEY_ID','default')
aws_secret_access_key = os.environ.get('AWS_SECRET_ACCESS_KEY','secret')
aws_region = os.environ.get('AWS_DEFAULT_REGION','us-east-1')
s3 = boto3.client('s3', 
                  endpoint_url='http://localstack:4566',
                  aws_access_key_id=aws_access_key_id,
                  aws_secret_access_key=aws_secret_access_key,
                  region_name=aws_region)

S3_BUCKET = os.environ.get('S3_BUCKET', 'measurements-bucket')


# GET for all locations, GET for specific location,
'''
@app.route('/measurements', methods=['GET'])
def get_measurements():
# Add code for this method
'''

@app.route('/measurements', methods=['POST'])
def add_measurement():
    new_measurement = request.get_json()
    if not new_measurement:
         return jsonify({"Error":"Invalid data format, expected JSON."}),400
    object_name = new_measurement['location_name'] + '.json'
    try: 
        s3.put_object(Bucket = S3_BUCKET,Key=object_name,Body=json.dumps(new_measurement))
    except Exception as e:
        return jsonify({"error":str(e)}),500 
    

# Add an update function


@app.route("/measurements/<location_name>", methods=["DELETE"])
def delete_measurement(location_name):
     # Name is based on location_name
     object_name = location_name + '.json'
     # Try to delete the object
     try:
          s3.delete_object(Bucket = S3_BUCKET,Key=object_name) 
     except Exception as e:
          return jsonify({"error":str(e)}),500
     

@app.route('/')
def website():
    return render_template('map.html')



if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True)
