from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
import re
from.utils.validators import validate_input


# Create your views here.

@api_view(['POST'])
def test_endpoint(request):
    data = request.data
    validate_input(data)
    return Response('testing')
   