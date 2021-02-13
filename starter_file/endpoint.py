import requests
import json

#Replace scoring URI and key with their corresponding values.
scoring_uri = 'http://04580459-2f0a-475f-93e9-718991121d05.southcentralus.azurecontainer.io/score'
key = '9qcgCTJk82rgEpHadVyOjwiGN9FsYmGY'

# Two sets of data to score, so we get two results back
data = {"data":
        [
          {
          
            "id":9046,
            "gender":"Male",
            "age":67,
            "hypertension":0,
            "heart_disease":1,
            "ever_married":"Yes",
            "work_type":"Private",
            "Residence_type":"Urban",
            "avg_glucose_level":228.69,
            "bmi":36.6,
            "smoking_status":"formerly smoked",
          },
          {
            
            "id":51676,
            "gender":"Female",
            "age":61,
            "hypertension":0,
            "heart_disease":0,
            "ever_married":"Yes",
            "work_type":"Self-employed",
            "Residence_type":"Rural",
            "avg_glucose_level":202.21,
            "bmi":"N/A",
            "smoking_status":"never smoked",
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
