from django.http import JsonResponse
from models import Athlete
from serializers import AthleteSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

