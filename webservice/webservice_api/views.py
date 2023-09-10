from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from rest_framework.request import Request
import math
import sys
MAX_DIGITS = 10**6
sys.set_int_max_str_digits(MAX_DIGITS)

from .models import Webservise, Welcome
from .serializers import (
    WebserviseSerializer,
    InfoSerializer,
    WelcomeSerializer,
)
from django.utils.timezone import now

class ExponentiationApiView(APIView):
    def get(self, request: Request, *args, **kwargs):
        data = request.GET.dict()
        if not len(data) == 2:
            return Response('You should pass only 2 args', status=status.HTTP_400_BAD_REQUEST)
        number, pow_ = int(data.get('number')), int(data.get('pow'))
        result = 0
        if isinstance(number, (int, )) and isinstance(pow_, (int, )):
            result = pow(number, pow_) 

            if int( math.log10(result)) +1 > MAX_DIGITS:
                return Response('final result is very high...', status=status.HTTP_400_BAD_REQUEST)
            return Response(
                { 'result': result },
                status=status.HTTP_200_OK,
            )
            
        return Response('number or pow is not int...', status=status.HTTP_400_BAD_REQUEST)
    
#/webservises/arifmetic?a=15&b=12&op=minimum
class ArifmeticApiView(APIView):
    def get(self, request: Request, *args, **kwargs):
       
        data = request.GET.dict()
        print(data)
        if not len(data) == 3:
            return Response('You should pass only 3 args', status=status.HTTP_400_BAD_REQUEST)
        a, b = int(data.get('a')), int(data.get('b'))
        
        result = 0
        if isinstance(a, (int, )) and isinstance(b, (int, )):
            operation = data.get('op')
            match operation:
                case 'multiplication':
                    result = a * b
                case 'addition':
                    result = a + b 
                case 'division':
                    result = a / b
                case 'subtraction':
                    result = a - b  
                case 'maximum':
                    result = max(a, b)
                case 'minimum':
                    result = min(a, b)
                case _:
                    return Response('Wrong operation passed...', status=status.HTTP_400_BAD_REQUEST)
            return Response(
                { 'result': result },
                status=status.HTTP_200_OK,
            )
        return Response('a or b is not int...', status=status.HTTP_400_BAD_REQUEST)
    
    
    
    
class WelcomeApiView(APIView):
    @staticmethod
    def get_greetings( *args, **kwargs):
        curr_time = now().time().hour
        greetings = 'Good '
        if 5 <= curr_time < 12:
            greetings += " morning"
        elif 12 <= curr_time < 18:
            greetings += " day"
        elif 18 <= curr_time < 23:
            greetings += " evening"
        else:
            greetings += " night"    
        greetings = f"{greetings}!"
        return greetings

    permission_classes = [permissions.IsAuthenticated]
    def get(self, request, *args, **kwargs) -> Response:
        
        data = {'user' : request.user.id, 'greetings': WelcomeApiView.get_greetings()}
        serializer = WelcomeSerializer(data=data, many=False)
        if serializer.is_valid():
            serializer.save()
            
            return Response(
                serializer.data,
                status=status.HTTP_200_OK,
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class InfoApiView(APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request, *args, **kwargs) -> Response:
        serializer = InfoSerializer(data={}, many=False)
        if serializer.is_valid():
            serializer.save()
            
            return Response(
                serializer.data,
                status=status.HTTP_200_OK,
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
# Create your views here.
class WebserviseListApiView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    
    
    def get(self, request, *args, **kwargs) -> Response:
        data = Webservise.objects.filter( user = request.user.id )
        serializer = WebserviseSerializer(data, many=True)
        return Response(
            serializer.data,
            status=status.HTTP_200_OK,
        )
        
        
    def post(self, request, *args, **kwargs) -> Response:
        data = {
            'timestamp' : request.data.get('timestamp'),
            'user' : request.user.id, 
        }
        serializer = WebserviseSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED,
            )
            
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)