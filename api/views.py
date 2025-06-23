# DJANGO IMPORT
from django.shortcuts import render, HttpResponse


# DRF IMPORT
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics,permissions,filters
from rest_framework.decorators import api_view
from rest_framework import status

# MODEL IMPORT
from .models import PrivacyPolicy, TermsAndConditions

# PRIVACY POLICY API VIEW

'''
This endpoint gets and returns the lastest updated version from the 'PrivacyPolicy' model
'''
@api_view(['GET'])
def privacy_policy(request):
    # try and except to catch errors
    try:
        # get all objects of model 'PrivacyPolicy' and filter the latest updated one
        queryset = PrivacyPolicy.objects.all().latest('updated_at')
        # if the query exists
        if queryset:
            # creates a dictionary from details from the model object
            data = {
                'title': queryset.title, 
                'content': queryset.content, 
                'is_active': queryset.is_active, 
                'created_at': queryset.created_at, 
                'updated_at': queryset.updated_at
            }
            return Response({'status': True,'message':'Privacy policy retrieved successfully.','data':data},status=status.HTTP_200_OK)     
        # if query does not exist, handle the response
        else:
            return Response({'status': False,'message':'Privacy policy not found.','data':None},status=status.HTTP_400_BAD_REQUEST)
    
    # return exception in results
    except Exception as e:
       return Response({'status': False,'message':f'Error: {e}.','data':None},status=status.HTTP_400_BAD_REQUEST) 


# TERMS AND CONDITIONS API VIEW

'''
This endpoint gets and returns the lastest updated version from the 'TermsAndConditions' model
'''
@api_view(['GET'])
def terms_and_condition(request):
    # try and except to catch errors
    try:
        # get all objects of model 'TermsAndConditions' and filter the latest updated one
        queryset = TermsAndConditions.objects.all().latest('updated_at')
        # if the query exists
        if queryset:
            # creates a dictionary from details from the model object
            data = {
                'title': queryset.title, 
                'content': queryset.content, 
                'is_active': queryset.is_active, 
                'created_at': queryset.created_at, 
                'updated_at': queryset.updated_at
            }
            return Response({'status': True,'message':'Terms and Conditions retrieved successfully.','data':data},status=status.HTTP_200_OK)
        # if query does not exist, handle the response
        else:
            return Response({'status': False,'message':'Terms and conditions not found.','data':None},status=status.HTTP_400_BAD_REQUEST)
    # return exception in results
    except Exception as e:
       return Response({'status': False,'message':f'Error: {e}.','data':None},status=status.HTTP_400_BAD_REQUEST) 
