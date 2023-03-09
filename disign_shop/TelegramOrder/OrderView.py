from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework.views import APIView

from .messaging import send_telegram


class OrderView(APIView):
    renderer_classes = [JSONRenderer]

    def post(self, request):
        message = request.data['message']
        if request.data['user']:
            user = request.user
            send_telegram("User: " + user.username + "\n" + message)
            return Response(status=200)
        else:
            send_telegram(message)
            return Response(status=200)
