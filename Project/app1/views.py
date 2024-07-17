from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def httpRequestParam(request):
    path = request.path
    schema = request.scheme
    method = request.method
    address = request.META['REMOTE_ADDR']
    user_agent = request.META['HTTP_USER_AGENT']
    path_info = request.path_info

    respose = HttpResponse()
    respose.headers['Age'] = 20
    
    msg = f'''<br>
      <br>Path : {path}
      <br>Schema : {schema}
      <br>Method : {method}
      <br>Address : {address}
      <br>User Agent : {user_agent}
      <br>Path Info : {path_info}
      <br>HTTP Response : {respose.headers}
      '''
    return HttpResponse(msg)

def home(request,bandName):
    return render(request,'page1.html')