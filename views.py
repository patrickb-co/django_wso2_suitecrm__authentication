from django.http import HttpResponse
import requests # pip install requests

#suitecrm api request data:
# example 
instance_api_url = "http://localhost:8888/SuiteCRM-7.11.13/Api/"

auth_url = instance_api_url + "access_token"
# Oauth 'password type' suitecrm credentials
client_id = ""
client_secret = ""
# regular suitecrm credentials
username = ""
password = ""

def index(request):
    payload = {"grant_type":"password","client_id":client_id,"client_secret":client_secret,"username":username,"password":password}
    auth_request = requests.post(auth_url,data = payload)
    crm_token = format(auth_request.json()["access_token"])
    
    return HttpResponse(crm_token)
