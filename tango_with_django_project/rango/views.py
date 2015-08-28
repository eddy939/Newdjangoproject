from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def index(request):

    # Construct a dictionary to pass to the template engine as its context.
    #Not the key boldmessage is the same as {{ boldmessage }} in the template!

    context_dict = {'boldmessage': "I am bold font from the context"}

    #Return a rendered response to send to the client.
    #We make use of the shortcut function to make our lives easier
    #Note that the first parameter is the template we wish to use

    return render(request, 'rango/index.html', context_dict)

def about(request):

    # construct a dictionary to pass to the template engine as its context.
    #Not the key boldmessage is the same as {{ boldmessage )) in the template!

    context_dict = {'boldmessage': "You are doing great buddy!"}

    #Return a rendered response to send to the client.
    #WE make use of th eshortcut function to make our lives easier
    #Note that the first parameter is the template we wish to use

    return render(request, 'rango/about.html', context_dict)