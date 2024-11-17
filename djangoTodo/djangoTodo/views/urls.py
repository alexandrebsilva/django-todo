from django.http import HttpResponse
from django.http import JsonResponse

def my_view(request):
    # Your logic here
    data = {
        "message": "Hello, this is my controller logic!"
    }
    return JsonResponse(data)