from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

# Create your views here.

def index(request):
    template = "index.html"
    context = {}
    return render(request, template, context)

@api_view(['GET'])
def apigetbarmi(request):
    # context = {"ize": 7}
    return Response('Szia!')

    