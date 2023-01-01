from django.shortcuts import render


def index(request):
	return render(request, 'index.html', {})

def portfolio_details(request):
	return render(request, 'portfolio_details.html', {})
