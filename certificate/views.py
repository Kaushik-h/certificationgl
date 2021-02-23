from django.shortcuts import render
from .upload import pdf_upload
from rest_framework import generics, views, permissions ,response, status

class CertificateView(views.APIView):
	# permission_classes = [permissions.IsAuthenticated,]
	http_method_names=['post']
	def post(self, request, *args, **kwargs): 
		try:
			pdf=request.data.get('pdf')
			user=self.request.user
			pdf_name=user.email+request.data.get("certname")
			request.data["pdf_url"]='https://storage.googleapis.com/certificate_pdf/'+pdf_name
			pdf_upload(pdf,pdf_name)
			serializer = CertificateSerializer(data=request.data)
			if serializer.is_valid:
				serializer.save()
			return response.Response(serializer.data,status=status.HTTP_200_OK)
		except Exception as e:
			return response.Response(str(e))