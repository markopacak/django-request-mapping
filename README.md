# Django request mapping system


Imagine you have the following methods in `views.py`:

```python
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
