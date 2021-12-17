from django.shortcuts import render
from django.db import transaction
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth import get_user_model

from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token

from .serializers import UserRegisterSerializer, UserListSerializer
# Create your views here.

User = get_user_model()


class CustomAuthToken(ObtainAuthToken):
	@transaction.atomic
	def post(self, request, *args, **kwargs):
		serializer = self.serializer_class(data=request.data, context={'request': request})
		serializer.is_valid(raise_exception=False)
		try:
			user = serializer.validated_data['user']
			token, created = Token.objects.get_or_create(user=user)
			return Response({
				'status': True,
				'msg': 'Login Successful',
				'data': {
					'token': token.key,
					'user_id': user.pk,
					'username': user.username,
				}
			})
		except KeyError:
			return Response({
				'status': False,
				'msg': 'Wrong username or password.',
			})



class UserRegisterView(APIView):
	serializer_class = UserRegisterSerializer

	def post(self, request, *args, **kwargs):
		serializer = self.serializer_class(data=request.data)
		serializer.is_valid(raise_exception=True)
		serializer.save()
		return Response(serializer.data)



class UserListView(APIView):
	serializer_class = UserListSerializer

	def get(self, request, pk=None):
		if pk:
			user = User.objects.get(id=pk)
			serializer = UserListSerializer(user)
			return Response(serializer.data)

		users = User.objects.all()
		serializer = UserListSerializer(users, many=True)
		return Response(serializer.data)