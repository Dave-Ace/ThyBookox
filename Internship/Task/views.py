from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

from django.http import JsonResponse

#View to calculate sum
class Sum(APIView):
    def get(self, request, number1, number2):
        Sum = number1 + number2
        data = {'Sum':{
            "1st Number":number1,
            "2nd Number":number2,
            "Sum": Sum
        }}
        return Response(data)

#View to calculate sum
class difference(APIView):
    def get(self, request, number1, number2):
        difference = number1 - number2
        data = {'Difference':{
            "1st Number":number1,
            "2nd Number":number2,
            "Difference": Sum
        }}
        return Response(data)

#View to calculate sum
class multiplication(APIView):
    def get(self, request, number1, number2):
        multiplied = number1 * number2
        data = {'Multiplication':{
            "1st Number":number1,
            "2nd Number":number2,
            "multiplied": Sum
        }}
        return Response(data)

#View to calculate sum
class Division(APIView):
    def get(self, request, number1, number2):
        divide = number1 / number2
        data = {'Division':{
            "1st Number":number1,
            "2nd Number":number2,
            "Division": divide
        }}
        return Response(data)