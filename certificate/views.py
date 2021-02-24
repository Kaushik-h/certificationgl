from django.shortcuts import render
from .upload import pdf_upload
from rest_framework import generics, views, permissions ,response, status
from rest_framework.parsers import MultiPartParser, FormParser, JSONParser
from .serializers import *

class CertificateView(views.APIView):
	permission_classes = [permissions.IsAuthenticated,]
	http_method_names=['post']
	parser_classes = (MultiPartParser, FormParser, JSONParser)
	def post(self, request, *args, **kwargs): 
		# try:
			user=self.request.user	
			request.data["user"]=user.id
			pdf=request.FILES['pdf']
			pdf_name=user.email+request.data.get("certname")
			request.data["pdf_url"]='https://storage.googleapis.com/certificate_pdf/'+pdf_name
			pdf_upload(pdf,pdf_name)
			serializer = CertificateSerializer(data=request.data)
			if serializer.is_valid():
				print(serializer.data)
				serializer.save()
			print(serializer.data)
			return response.Response(serializer.data,status=status.HTTP_200_OK)
		# except Exception as e:
		# 	return response.Response(str(e))