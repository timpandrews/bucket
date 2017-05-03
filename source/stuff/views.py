from django.shortcuts import render

from stuff.forms import ItemForm
from stuff.models import Item

def stuff_list(request):
    context = {
        "title": "list"
    }
    return render(request, "stuff_list.html", context)

def stuff_create(request):
    if not request.user.is_authenticated:
        raise Http404

    form = ItemForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        instance = form.save(commit=False)
        instance.user = request.user
        instance.save()
        messages.success(request, "Successfully Created")
        return HttpResponseRedirect(instance.get_absolute_url())

    context = {
        "title": "Add New Stuff",
        "form": form,
    }
    return render(request, "stuff_form.html", context)


def stuff_update(request, id=None):
    context = {
        "title": "update"
    }
    return render(request, "stuff_form.html", context)

def stuff_detail(request, id=None):
    context = {
        "title": "detail"
    }
    return render(request, "stuff_detail.html", context)

def stuff_delete(request, id=None):
    context = {
        "title": "delete"
    }
    return render(request, "home.html", context)