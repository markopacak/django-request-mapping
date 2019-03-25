# from django.urls import path
# from django.http import HttpRequest, HttpResponseNotAllowed
# from . import views


def req_map(**mapping_table):
    """
    Wraps multiple executable functions for each suitable HTTP method and returns the corresponding view function in
    case it exists, or
    As per REST standard, only the following HTTP methods should be allowed:
        * GET       to retrieve and object with a given identifier (ID)
        * POST      to create a new object
        * PUT       to replace an object
        * DELETE    to delete an object with a given identifier (ID)
        * PATCH     to edit an object with a given identifier (ID)
    :param:
        mapping_table:  A [key,value] table containing HTTP method types as key and the function to
                execute as value
    :return:
        The function that will elaborate the request (based on the HTTP method).
        A HttpResponseNotAllowed object with a list of supported methods, in case the given HTTP method
        is not tied to any view method.
    """
    def invalid_method(request: HttpRequest, *args, **kwargs):
        """
        A function returning a HttpResponseNotAllowed object, as not matching HTTP method was found.
        :param request: the incoming HTTP request
        :param args: unused
        :param kwargs: named path arguments
        :return: a HttpResponseNotAllowed object containing a list of supported methods (as per standard)
        """
        return HttpResponseNotAllowed(mapping_table.keys())

    def wrapper(request: HttpRequest, *args, **kwargs):
        """
        Attempts to find a suitable function to execute for the HTTP method and returns a HttpResponseNotAllowed
        object in case no suitable function exists.
        :param request: the incoming HTTP Request
        :param args: unused
        :param kwargs: named path arguments
        :return:
        """
        handler = mapping_table.get(request.method, invalid_method)
        print(args)
        print(kwargs)
        return handler(request, *args, **kwargs)
    return wrapper
