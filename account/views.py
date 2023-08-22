from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import RegisterSerializer
from django.contrib.auth import authenticate, login, logout


class RegisterView(APIView):
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=201)


class LoginView(APIView):

    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')

        user = authenticate(request, username=username, password=password)
        print('===========')
        print(user)
        print('===========')

        if user:
            login(request, user)
            return Response({'message':'Вы успешно залогинены'}, status=200)
        else:
            return Response('Переданы не корректные данные', status=400)




