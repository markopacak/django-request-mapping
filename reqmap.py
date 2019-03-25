# from django.urls import path
# from django.http import HttpRequest, HttpResponseNotAllowed
# from . import views


def req_map(**mapping_table):
    """
    Maps functions to suitable HTTP methods. Common REST HTTP methods are:
        * GET / HEAD        for resource retrieval
        * POST              for resource creation
        * PUT               for resource replacement / update
        * DELETE            for resource deletion
        * PATCH             for resource edit / partial replacement
    :param:
        mapping_table:  A [key,value] table containing HTTP method types as keys and the function to
                execute as value
    :return:
        The function that will elaborate the request (based on the HTTP method).
        A HttpResponseNotAllowed object with a list of supported methods will be returned, in case a
        suitable method wasn't supplied.
    """
    
    def wrapper(request: HttpRequest, *args, **kwargs):

        handler = mapping_table.get(
            request.method,
            lambda req, *args, **kwargs : HttpResponseNotAllowed(mapping_table.keys())
        )
        return handler(request, *args, **kwargs)

    return wrapper
