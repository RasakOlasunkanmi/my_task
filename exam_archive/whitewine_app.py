from fastapi import FastAPI
from pydantic import BaseModel
import numpy as np
import joblib
import uvicorn



# Lets load our saved model
model = joblib.load('best_random_forest_model.pkl')
scaler = joblib.load('scaler.pkl')

# Lets initialize the FastAPI app
app = FastAPI()

# Lets create our pydantic model for input features
class WineFeatures(BaseModel):
    fixed_acidity: float
    volatile_acidity: float
    citric_acid: float
    residual_sugar: float
    chlorides: float
    free_sulfur_dioxide: float
    total_sulfur_dioxide: float
    density: float
    pH: float
    sulphates: float
    alcohol: float


# Lets create our endpoints

# home endpoints - home
@app.get("/")
def Home():
    return {"Welcome To Wine Quality Prediction"}

# predict endpoint - to predict wine quality
# convert the features to 2d numpy array using [[]]
@app.post("/predict")
def predict_quality(wine: WineFeatures):
    features = np.array([[wine.fixed_acidity, wine.volatile_acidity, wine.citric_acid,
                        wine.residual_sugar, wine.chlorides, wine.free_sulfur_dioxide,
                        wine.total_sulfur_dioxide, wine.density, wine.pH,
                         wine.sulphates, wine.alcohol]])
    
    # Lets scale our input features using the loaded scaler (to normalize the input features)
    scaled_features = scaler.transform(features)
    
    # Lets make prediction using the loaded model
    prediction = model.predict(scaled_features)
    
    # Return the prediction as a string for serialization
    return {"predicted_quality": str(prediction[0])}

# Lets run the app
if __name__ == "__main__":
    host = "127.0.0.1"
    port = 8000
    uvicorn.run(app, host=host, port=port)