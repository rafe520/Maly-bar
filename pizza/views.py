from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
def index(request):
    #kontekst = {'komunikat': 'Witaj w aplikacji Pizza!'}
	#return render(request, 'pizza/index.html',kontekst,)
	template=loader.get_template('pizza/index.html')
	kontekst = {'komunikat': 'Witaj w aplikacji Pizza!'}
	return HttpResponse(template.render(kontekst, request))