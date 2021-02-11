import requests
import json

#Replace scoring URI and key with their corresponding values.
scoring_uri = ''
key = ''

# Two sets of data to score, so we get two results back
data = {"data":
        [
          {
            "id":9046,
            "gender":0,
            "age":67,
            "hypertension":0,
            "heart_disease":1,
            "ever_married":1,
            "work_type":0,
            "Residence_type":1,
            "avg_glucose_level":228.69,
            "smoking_status":0,
          },
          {
            "id":51676,
            "gender":1,
            "age":61,
            "hypertension":0,
            "heart_disease":0,
            "ever_married":1,
            "work_type":0,
            "Residence_type":0,
            "avg_glucose_level":202.21,
            "smoking_status":0,
          },
      ]
    }

#Convert to JSON string
input_data = json.dumps(data)
with open("data.json", "w") as _f:
   _f.write(input_data)

#Set the content type
headers = {'Content-Type': 'application/json'}

#If authentication is enabled, set the authorization header
headers['Authorization'] = f'Bearer {key}'

#Make the request and display the response
resp = requests.post(scoring_uri, input_data, headers=headers)
print(resp.json())
