from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
import re
from .utils.validators import validate_input
from .utils.micromort_model import calculate_micromorts


# Create your views here.

@api_view(['POST'])
def get_micromorts(request):
    ''' This function performs all of the validation and calculation needed for our micromort service. '''

    # validate input data
    validated_data = validate_input(request.data)

    # if request input not in correct format, return error
    if 'error' in validated_data:
        return Response({'error': str(validated_data['error'])}, status=status.HTTP_400_BAD_REQUEST)

    # else, proceed with micromort calculation

    total_micromorts = calculate_micromorts(validated_data)

    return Response({'commuterID': validated_data['commuterID'], 'total_micromorts': total_micromorts}, status=status.HTTP_200_OK)
    
