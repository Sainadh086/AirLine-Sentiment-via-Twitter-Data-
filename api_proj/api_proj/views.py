from pyramid.view import view_config
import sys
sys.path.insert(1,'/EntHireTask/')
from nlp_train import model_predict

@view_config(route_name='home',request_method='GET', renderer='templates/mytemplate.jinja2')
def my_view(request):
    return {'project': 'api_proj'}

@view_config(route_name='predict',request_method='POST', renderer='json')
def predict_api(request):
    if request.method=="POST":
        text = request.POST['text']
        sentiment = model_prdict(text)
        return {'Sentiment' : sentiment}
    return {"data" : "No data"}

''' Tried to include swagger documentation but it is not fully integrated
@view_config(route_name="api.predict", request_method='POST', renderer='json')
def predict_swagger(request):
    text = request.swagger_data['text']
    return {'data' : text}
'''