## Django Rest-Framework
This is the short exercise tutorials to getting started with Django REST Framework. Followed the official [documentation](https://www.django-rest-framework.org/).

## Application Structure
Following are the details of django projects and  applications:
- [Project](#project)
  - [Function Based Views](#function-based-views)
  - [Class Based Views](#class-based-views)
  - [Generic Api View](#generic-api-views)
  - [Api Viewsets](#api-viewsets)
- [Project Setup](#project-setup)

### Project
All the project configurations is registered in a django project `core` where you can configure settings, applications, database configurations, general settings, server files and lots of other cool options.

### Function Based Views
`REST framework` also allows you to work with regular function based views. It provides a set of simple decorators that wrap your function based views to ensure they receive an instance of `Request` (rather than the usual Django HttpRequest) and allows them to return a `Response` (instead of a Django HttpResponse), and allow you to configure how the request is processed.

*Reference*:
- An application(`d01_fn_api_view`) demonstrates the usage of function based views.
- Official: https://www.django-rest-framework.org/api-guide/views/#function-based-views

### Class Based Views
REST framework provides an `APIView` class, which subclasses Django's View class. APIView classes are different from regular View classes in the following ways:
- `Requests` passed to the handler methods will be REST framework's Request instances, not Django's HttpRequest instances.
- Handler methods may return REST framework's `Response`, instead of Django's HttpResponse. The view will manage content negotiation and setting the correct renderer on the response.
- Any `APIException exceptions` will be caught and mediated into appropriate responses.
- Incoming requests will be authenticated and appropriate permission and/or throttle checks will be run before dispatching the request to the handler method.

Using the APIView class is pretty much the same as using a regular `View` class, as usual, the incoming request is dispatched to an appropriate handler method such as `.get()` or `.post()`. Additionally, a number of attributes may be set on the class that control various aspects of the API policy.

*References*:
- An application(`d02_cls_api_view`) demonstrates the usage of class based views.
- Official: https://www.django-rest-framework.org/api-guide/views/#class-based-views

### Generic Api Views
One of the key benefits of class-based views is the way they allow you to compose bits of reusable behavior. REST framework takes advantage of this by providing a number of pre-built views that provide for commonly used patterns.

The `generic` views provided by REST framework allow you to quickly build API views that map closely to your database models.

*References*:
- An application(`d03_generic_api_view`) demonstrates the usage of generic api views.
- Official: https://www.django-rest-framework.org/api-guide/generic-views/

### Api Viewsets
Django REST framework allows you to combine the logic for a set of related views in a single class, called a `ViewSet`. In other frameworks you may also find conceptually similar implementations named something like 'Resources' or 'Controllers'.

A ViewSet class is simply a type of class-based View, that does not provide any method handlers such as .get() or .post(), and instead provides actions such as `.list()` and `.create()`.

The method handlers for a ViewSet are only bound to the corresponding actions at the point of finalizing the view, using the `.as_view()` method.

*References*:
- An application(`d04_api_viewsets`) demonstrates the usage of api viewsets.
- Official: https://www.django-rest-framework.org/api-guide/viewsets/

## Project Setup
1. Clone this project and navigate to this directory.
2. Create a virtual environment `virtualenv venv` provided that you have installed virtualenv globally.
3. Install the depedencies `pip install -r requirements.txt`.
4. Start the django application `py manage.py runserver`
