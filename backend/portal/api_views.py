from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(["GET"])
def ping(request):
    user = request.user.username if request.user.is_authenticated else None
    return Response({"status": "ok", "user": user})
