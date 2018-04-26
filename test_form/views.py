from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
import requests
from requests_toolbelt.multipart.encoder import MultipartEncoder
# Create your views here.
from django.shortcuts import render_to_response
from django.views.decorators.csrf import csrf_exempt
from json import dumps
from django.http import HttpResponseRedirect

@csrf_exempt
def test_form_collection(request):
    if request.method == 'GET':
        return render(request, 'index.html')

    elif request.method == 'POST':
        first_name= request.POST.get('first_name', '')
        print ("vipul gangwar")
        print (first_name)
        last_name= request.POST.get('last_name', '')
        email= request.POST.get('email', '')
        print (email)
        auth_url  = 'https://test-mindful.herokuapp.com/test_form/'
        payload = {'first_name': first_name, 'last_name': last_name, 'email': email }
        headers = {'content-type':'application/json'}
        r = requests.post(auth_url, headers=headers, data= dumps(payload))
        return HttpResponseRedirect('https://test-mindful.herokuapp.com/test_form/')
        #return render (request, 'index.html', {'email': "data is saved"})
