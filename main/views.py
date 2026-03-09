from django.http import HttpRequest, HttpResponse, JsonResponse

from .models import Resource

# TODO: login
username = "jaturner"


def index(request: HttpRequest) -> HttpResponse:
    resources = Resource.objects.all()

    # TODO: username = request.user.username
    message = f"Hello {username}. You're at the index.</br></br>"
    for r in resources:
        message += f"Name: {r.name},  Owner: {r.owner}</br>"

    return HttpResponse(message)


def add_resource(request: HttpRequest) -> JsonResponse:
    name = request.POST.get("name")
    resource = Resource.objects.create(name=name)

    return JsonResponse({
        "name": resource.name,
        "owner": resource.owner,
    })


def take_resource(request: HttpRequest) -> JsonResponse:
    name = request.POST.get("name")
    resource = Resource.objects.get(name=name)

    # TODO: username = request.user.username
    resource.owner = username
    resource.save()

    return JsonResponse({
        "name": resource.name,
        "owner": resource.owner,
    })


def release_resource(request: HttpRequest) -> JsonResponse:
    name = request.POST.get("name")
    resource = Resource.objects.get(name=name)

    resource.owner = None
    resource.save()

    return JsonResponse({
        "name": resource.name,
        "owner": resource.owner,
    })
