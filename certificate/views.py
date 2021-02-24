from django.shortcuts import render
from .upload import Upload
from rest_framework import generics, views, permissions ,response, status
from rest_framework.parsers import MultiPartParser, FormParser, JSONParser
from .serializers import *

class CertificateView(views.APIView):
	permission_classes = [permissions.IsAuthenticated,]
	http_method_names=['post']
	parser_classes = (MultiPartParser, FormParser, JSONParser)
	def post(self, request, *args, **kwargs): 
			user=self.request.user	
			request.data["user"]=user.id
			pdf=request.FILES['pdf']
			pdf_name=user.name+request.data.get("certid")+'.pdf'
			a=Upload.upload_pdf(pdf, pdf_name)
			request.data["pdf_url"]='https://storage.googleapis.com/certificate_pdf/pdf/'+pdf_name
			serializer = CertificateSerializer(data=request.data)
			if serializer.is_valid():
				serializer.save()
			print(serializer.data)
			return response.Response(serializer.data,status=status.HTTP_200_OK)
		