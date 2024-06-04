from rest_framework import status, serializers
from functools import wraps
from rest_framework.response import Response


# Decorators
def validate(serializer_class):
	def decorator(func):
		@wraps(func)
		def wrapped(self, request, *args, **kwargs):
			serializer = serializer_class(data=request.data)
			if serializer.is_valid():
				return func(self, request, serializer.validated_data, *args, **kwargs)
			return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

		return wrapped

	return decorator
