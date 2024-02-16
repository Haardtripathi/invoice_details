from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from .models import *
from .serializers import *

class get_detailsAPI(APIView):
    def get(self,request):
        invoice_details_objects=InvoiceDetails.objects.all()
        serializers=InvoiceDetailsSerializer(invoice_details_objects,many=True)
        return Response({"status": 200,"payload":serializers.data})
    
    def post(self, request):
        data=request.data
        serializers=InvoiceDetailsSerializer(data=data)
        if not serializers.is_valid():
            print("123")
            print(serializers.errors)
            return Response({"status": 403,"errors":serializers.errors,"message":"Something went wrong"})
        serializers.save()
        return Response({"status": 200,"payload":data,"message":"DATA SAVED"})
    
    def put(self,request):
        try:
            data=request.data
            id=request.GET.get('id')
            invoice_details_object=InvoiceDetails.objects.get(id=id)
            serializers=InvoiceDetailsSerializer(invoice_details_object,data=request.data,partial=True)
            if not serializers.is_valid():
                print(serializers.errors)
                return Response({"status": 403,"errors":serializers.errors,"message":"Something went wrong"})
            serializers.save()
            
            return Response({"status": 200,"payload":serializers.data,"message":"DATA UPDATED"})
        except Exception as e:
            print(e)
            return Response({"status": 403,"message":"Invalid id"})