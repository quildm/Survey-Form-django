from django.shortcuts import render, HttpResponse, redirect

def index(request):
	print "survey form page"
	return render (request, 'survey_form/index.html')


def formProcess(request):
    if 'counter' in request.session:
        request.session['counter'] += 1
    else:
        request.session['counter'] = 1

    request.session['data'] = {
        "Name": request.POST['name'],
        "Dojo Location": request.POST['dojoLocation'],
        "Favorite Language": request.POST['favLang'],
        "Comments": request.POST['comments']
    }
    return redirect('/survey_form/showResults')

def showResults(request):
    print "Go to show results!"
    print request.session
    return render(request, 'survey_form/result.html')