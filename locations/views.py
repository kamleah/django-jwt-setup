from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
# Create your views here.

from django.http import HttpResponse

class Locations(APIView):
    permission_classes=[IsAuthenticated]
    def get(self, request):
        return Response({"Message":"Hello, world. You're at the polls index."})
    
    def post(self, request):
        return Response({"Message":"Hello, world. You're at the polls index."})