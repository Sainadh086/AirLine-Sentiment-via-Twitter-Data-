# AirLine-Sentiment-via-Twitter-Data-

## Implemented
### Machine Learning models
  - Logistic Regression
  - Naive Bayes Model

### Deep learning Model
  - Simple Neural Network model

### Sentiment Analysis API
  - Implemented Pyramid for deploying my navie bayed model as API
  - Implemented FastAPI for including the swagger  documentation
###  To run the API's
  - #### Pyramid
      - pserver development.ini *for deploying in local server
      - pserver production.ini  *for deploying in production environment
  - #### FastAPI
      - uvicorn text_api:app --host 0.0.0.0 *for production environment
