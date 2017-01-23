from django.shortcuts import render

def stuff_list(request):
    context = {
        "title": "list"
    }
    return render(request, "home.html", context)

def stuff_create(request):
    context = {
        "title": "create"
    }
    return render(request, "home.html", context)

def stuff_update(request, id=None):
    context = {
        "title": "update"
    }
    return render(request, "home.html", context)

def stuff_detail(request, id=None):
    context = {
        "title": "detail"
    }
    return render(request, "home.html", context)

def stuff_delete(request, id=None):
    context = {
        "title": "delete"
    }
    return render(request, "home.html", context)