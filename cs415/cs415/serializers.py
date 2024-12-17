from rest_framework import serializers
from cs415.models import Pagedata, Phonetype, Useraddress, Userinfo, Userphone, Webuser, Addresstype

class WebuserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Webuser
        fields = ['web_user_id', 'first_name', 'last_name', 'email', 'created_date', 'is_active', 'last_login']

class AddresstypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Addresstype
        fields = '__all__'

class PagedataSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pagedata
        fields = '__all__'

class PhonetypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Phonetype
        fields = '__all__'

class UseraddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Useraddress
        fields = '__all__'

class UserinfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Userinfo
        fields = '__all__'

class UserphoneSerializer(serializers.ModelSerializer):
    class Meta:
        model = Userphone
        fields = '__all__'