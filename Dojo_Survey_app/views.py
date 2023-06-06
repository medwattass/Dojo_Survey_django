from django.shortcuts import render, redirect


def index(request):
    return render(request,"index.html")


def results(request):
    name = request.POST['name']
    location = request.POST['location']
    language = request.POST['language']
    database = request.POST['database']
    framework = request.POST['framework']
    comment = request.POST['comment']
    survey_info = {
        "name" : name,
        "location" : location,
        "language" : language,
        "database" : database,
        "framework" : framework,
        "comment" : comment
    }
    return render(request,"result.html", survey_info)
