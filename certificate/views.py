from django.shortcuts import render
from .upload import Upload
from rest_framework import generics, views, permissions ,response, status
from rest_framework.parsers import MultiPartParser, FormParser, JSONParser
from .serializers import *

class CertificateView(views.APIView):
	permission_classes = [permissions.IsAuthenticated,]
	http_method_names=['get','post']
	parser_classes = (MultiPartParser, FormParser, JSONParser)
	def get(self, request, *args, **kwargs): 
		# try:
			user=self.request.user
			queryset=Certificates.objects.filter(user=user)
			serializer=CertificateSerializer(queryset,many=True)
			return response.Response(serializer.data,status=status.HTTP_200_OK)
		# except Exception as e:
			# return response.Response(str(e))

	def post(self, request, *args, **kwargs): 
		try:
			user=self.request.user	
			request.data["user"]=user.id
			pdf=request.FILES['pdf']
			pdf_name=user.name+request.data.get("certid")+'.pdf'
			a=Upload.upload_pdf(pdf, pdf_name)
			request.data["pdf_url"]='https://storage.googleapis.com/certificate_pdf/pdf/'+pdf_name
			serializer = CertificateSerializer(data=request.data)
			if serializer.is_valid():
				serializer.save()
			return response.Response(serializer.data,status=status.HTTP_200_OK)
		except Exception as e:
			return response.Response(str(e))
		