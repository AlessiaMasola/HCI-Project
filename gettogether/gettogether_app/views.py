from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import render_to_response

def index(request):
    # Request the context of the request.
    # The context contains information such as the client's machine details, for example.
    # Construct a dictionary to pass to the template engine as its context.
    # Note the key boldmessage is the same as {{ boldmessage }} in the template!
    # Return a rendered response to send to the client.
    # We make use of the shortcut function to make our lives easier.
    # Note that the first parameter is the template we wish to use.
    return render_to_response('gettogether_app/index.html')

def events(request):
    return render_to_response('gettogether_app/events.html')

def games(request):
    return render_to_response('gettogether_app/games.html')

def useful_links(request):
    return render_to_response('gettogether_app/useful_links.html')

def forum(request):
    return render_to_response('gettogether_app/forum.html')
