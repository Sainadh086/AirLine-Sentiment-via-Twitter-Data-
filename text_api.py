import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel
from nlp_train import model_predict
#Using FastAPI
app = FastAPI()

#Loading our data for the API
class review_data(BaseModel):
    text : str

#The first page of the API. Basic Get Request
@app.get('/')
def index():
    return {"Hi, welcome to find the sentiment of your user's comments, reviews, feedback and thier experience from various\nsocial media platforms and learn the flow of your  businees."}


#Deploying our model at the endpoint /sentiment with a post request
@app.post('/sentiment')
def review_api(data:review_data):
    data = data.dict()
    text = data['text']
    sentiment = model_predict(text)
    return {'sentiment':sentiment}

# Using uvicorn server for deployment
if __name__ == '__main__':
    uvicorn.run(app, port = 80)

