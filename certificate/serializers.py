from rest_framework import serializers
from.models import *

class CertificateSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    class Meta:
        model=Patient
        fields=('user','csp','level','certname','certid','certified_date','expiry_date','pdf_url','validity')