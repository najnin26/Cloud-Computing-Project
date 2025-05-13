import json
import requests

input_data = {
  "pregnancies": 0,
  "Glucose": 0,
  "BloodPressure": 0,
  "SkinThickness": 0,
  "Insulin": 0,
  "BMI": 0,
  "DiabetesPedigreeFunction": 0,
  "Age": 0
}

url='http://localhost/diabetes_prediction'

json_object=json.dumps(input_data)

response=requests.post(url,data=json_object)

print(response.text)