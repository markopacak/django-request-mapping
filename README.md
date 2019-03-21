# Django request mapping system

This short snipped allows mapping the same `path` to multiple functions depending on the HTTP method, like below:

```python
# urls.py

urlpatterns = [
    path('object/<int:id>', req_map(
        POST=views.obj_create,
        DELETE=views.obj_delete,
        GET=views.obj_get,
        PATCH=views.obj_edit
    ), name="object")
]

```

where in `views.py`

```python

# views.py

def obj_create(request, id=-1):
    return HttpResponse("POST")


def obj_delete(request, id):
    return HttpResponse("DELETE")


def obj_get(request, id):
    return HttpResponse("GET")


def obj_edit(request, id):
    return HttpResponse("PATCH")


def obj_replace(request, id=-1):
    return HttpResponse("PUT")

```

----

Developed by Marko Pacak (`info @ myfullname dot com`)
