from fastapi import FastAPI
import uvicorn
from PropertyVariables import PropertyPricePrediction
import pandas as pd
import joblib

# 1. Create the Application Object
PropertyPricePredictionApp = FastAPI()

# 2. Load the model from disk
fileName = 'property_price_prediction_using_voting_regression.sav'
loaded_model = joblib.load(fileName)

# 3. Index route, opens automatically on http://127.0.0.1:8000
@PropertyPricePredictionApp.get('/')
def index():
    return {"message":'Hello!!! Welcome to the Property Price Prediction Model'}


# 4. Expose the prediction functionality, make a prediction from the passed
#    JSON data and return the predicted price with the confidence (http://127.0.0.1:8000/predictprice)
@PropertyPricePredictionApp.post('/predictprice')
def price_prediction(data: PropertyPricePrediction):
    print('\n\nBefore converting Dict',data)
    data = data.dict()
    print('\n\nAfter converting Dict',data)
    
    data = pd.DataFrame([data])
    print('\n\nDataframe output-\n',data)
    
    predicted_value = loaded_model.predict(data)
    print(str(predicted_value))
    return str(predicted_value)

# 5. Run the API with uvicorn
#    Will run on http://127.0.0.1:8000
if __name__ == '__main__':
    uvicorn.run("app:PropertyPricePredictionApp",host='127.0.0.1', port=8005, reload=True, debug=True, workers=3)