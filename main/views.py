from django.http import HttpRequest, HttpResponse, JsonResponse

from .models import Resource


def index(request: HttpRequest) -> HttpResponse:
    resources = Resource.objects.all()

    message = f"Hello {request.user}. You're at the index.</br></br>"
    for res in resources:
        message += f"UUID: {res.uuid},  Name: {res.name},  Owner: {res.owner}</br>"

    return HttpResponse(message)


def add_resource(request: HttpRequest) -> JsonResponse:
    name = request.POST.get("name")
    resource = Resource.objects.create(name=name)

    return JsonResponse({
        "uuid": resource.uuid,
        "name": resource.name,
        "owner": resource.owner,
    })
