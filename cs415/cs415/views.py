from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from datetime import datetime
from cs415.models import Pagedata, Phonetype, Useraddress, Userinfo, Userphone, Webuser, Addresstype
from cs415.serializers import PagedataSerializer, PhonetypeSerializer, UseraddressSerializer, UserinfoSerializer, UserphoneSerializer, WebuserSerializer, AddresstypeSerializer
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

class WebUserAPIView(APIView):
    @swagger_auto_schema(responses={200: WebuserSerializer(many=True)})
    def get(self, request):
        webusers = Webuser.objects.all()
        serializer = WebuserSerializer(webusers, many=True)
        return Response(serializer.data)
    
    @swagger_auto_schema(operation_description="Add New User", request_body=WebuserSerializer)
    def post(self, request, *args, **kwargs):
        request.data['created_date'] = str(datetime.now())
        request.data['is_active'] = 1
        serializer = WebuserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response({'errors': serializer.errors},
                                status=status.HTTP_400_BAD_REQUEST)

class SingleWebUserAPIView(APIView):
    def get(self, request, web_user_id):
        user_data = {}
        user = Webuser.objects.get(web_user_id=web_user_id)
        user_serial = WebuserSerializer(user)
        user_data.update({"user": user_serial.data})
        addresses = UseraddressSerializer(Useraddress.objects.filter(web_user=user), many=True)
        user_data.update({"addresses": addresses.data})
        info = UserinfoSerializer(Userinfo.objects.filter(web_user=user), many=True)
        user_data.update({"info": info.data})
        phone = UserphoneSerializer(Userphone.objects.filter(web_user=user).select_related(), many=True)
        user_data.update({"phones": phone.data})
        return Response(user_data)

    @swagger_auto_schema(operation_description="Update WebUser", request_body=WebuserSerializer)
    def patch(self,request,web_user_id):
        webuser_obj = Webuser.objects.get(web_user_id=web_user_id)
        serializer = WebuserSerializer(webuser_obj, data=request.data,partial=True)
        if (serializer.is_valid()):
            serializer.save()
            return Response(serializer.data)
        return Response({'errors': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


class AddresstypeAPIView(APIView):
    @swagger_auto_schema(responses={200: AddresstypeSerializer(many=True)})
    def get(self, request):
        addresstypes = Addresstype.objects.all()
        serializer = AddresstypeSerializer(addresstypes, many=True)
        return Response(serializer.data)
    
    def post(self, request, *args, **kwargs):
        serializer = AddresstypeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response({'errors': serializer.errors},
                                status=status.HTTP_400_BAD_REQUEST)
    
class SingleAddresstypeAPIView(APIView):
    def get(self, request, address_type_id):
        addresstype = Addresstype.objects.get(address_type_id=address_type_id)
        serializer = AddresstypeSerializer(addresstype)
        return Response(serializer.data)
    
    @swagger_auto_schema(operation_description="Update Address Type", request_body=AddresstypeSerializer)
    def patch(self,request,address_type_id):
        addresstype_obj = Addresstype.objects.get(address_type_id=address_type_id)
        serializer = AddresstypeSerializer(addresstype_obj, data=request.data,partial=True)
        if (serializer.is_valid()):
            serializer.save()
            return Response(serializer.data)
        return Response({'errors': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

class PagedataAPIView(APIView):
    @swagger_auto_schema(responses={200: PagedataSerializer(many=True)})
    def get(self, request):
        pagedatas = Pagedata.objects.all()
        serializer = PagedataSerializer(pagedatas, many=True)
        return Response(serializer.data)
    
    def post(self, request, *args, **kwargs):
        serializer = PagedataSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response({'errors': serializer.errors},
                                status=status.HTTP_400_BAD_REQUEST)

class SinglePagedataAPIView(APIView):
    def get(self, request, page_id):
        pagedata = Pagedata.objects.get(page_id=page_id)
        serializer = PagedataSerializer(pagedata)
        return Response(serializer.data)
    
    @swagger_auto_schema(operation_description="Update Page Data", request_body=PagedataSerializer)
    def patch(self,request,page_id):
        pagedata_obj = Pagedata.objects.get(page_id=page_id)
        serializer = PagedataSerializer(pagedata_obj, data=request.data,partial=True)
        if (serializer.is_valid()):
            serializer.save()
            return Response(serializer.data)
        return Response({'errors': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
    
class PhonetypeAPIView(APIView):
    @swagger_auto_schema(responses={200: PhonetypeSerializer(many=True)})
    def get(self, request):
        phonetypes = Phonetype.objects.all()
        serializer = PhonetypeSerializer(phonetypes, many=True)
        return Response(serializer.data)
    
    def post(self, request, *args, **kwargs):
        serializer = PhonetypeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response({'errors': serializer.errors},
                                status=status.HTTP_400_BAD_REQUEST)
    
class SinglePhonetypeAPIView(APIView):
    def get(self, request, phone_type_id):
        phonetype = Phonetype.objects.get(phone_type_id=phone_type_id)
        serializer = PhonetypeSerializer(phonetype)
        return Response(serializer.data)
    
    @swagger_auto_schema(operation_description="Update Phone Type", request_body=PhonetypeSerializer)
    def patch(self,request,phone_type_id):
        phonetype_obj = Phonetype.objects.get(phone_type_id=phone_type_id)
        serializer = PhonetypeSerializer(phonetype_obj, data=request.data,partial=True)
        if (serializer.is_valid()):
            serializer.save()
            return Response(serializer.data)
        return Response({'errors': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

class UseraddressAPIView(APIView):
    @swagger_auto_schema(responses={200: UseraddressSerializer(many=True)})
    def get(self, request):
        useraddresses = Useraddress.objects.all()
        serializer = UseraddressSerializer(useraddresses, many=True)
        return Response(serializer.data)
    
    def post(self, request, *args, **kwargs):
        request.data['created_date'] = str(datetime.now())
        serializer = UseraddressSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response({'errors': serializer.errors},
                                status=status.HTTP_400_BAD_REQUEST)
    
class SingleUseraddressAPIView(APIView):
    def get(self, request, user_address_id):
        useraddress = Useraddress.objects.get(user_address_id=user_address_id)
        serializer = UseraddressSerializer(useraddress)
        return Response(serializer.data)
    
    @swagger_auto_schema(operation_description="Update User Address", request_body=UseraddressSerializer)
    def patch(self,request,user_address_id):
        useraddress_obj = Useraddress.objects.get(user_address_id=user_address_id)
        serializer = UseraddressSerializer(useraddress_obj, data=request.data,partial=True)
        if (serializer.is_valid()):
            serializer.save()
            return Response(serializer.data)
        return Response({'errors': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

class UserinfoAPIView(APIView):
    @swagger_auto_schema(responses={200: UserinfoSerializer(many=True)})
    def get(self, request):
        userinfos = Userinfo.objects.all()
        serializer = UserinfoSerializer(userinfos, many=True)
        return Response(serializer.data)
    
    def post(self, request, *args, **kwargs):
        serializer = UserinfoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response({'errors': serializer.errors},
                                status=status.HTTP_400_BAD_REQUEST)

class SingleUserinfoAPIView(APIView):
    def get(self, request, user_id):
        userinfo = Userinfo.objects.get(user_id=user_id)
        serializer = UserinfoSerializer(userinfo)
        return Response(serializer.data)
    
    @swagger_auto_schema(operation_description="Update User Info", request_body=UserinfoSerializer)
    def patch(self,request,user_id):
        userinfo_obj = Userinfo.objects.get(user_id=user_id)
        serializer = UserinfoSerializer(userinfo_obj, data=request.data,partial=True)
        if (serializer.is_valid()):
            serializer.save()
            return Response(serializer.data)
        return Response({'errors': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

class UserphoneAPIView(APIView):
    @swagger_auto_schema(responses={200: UserphoneSerializer(many=True)})
    def get(self, request):
        userphones = Userphone.objects.all()
        serializer = UserphoneSerializer(userphones, many=True)
        return Response(serializer.data)
    
    def post(self, request, *args, **kwargs):
        request.data['created_date'] = str(datetime.now())
        request.data['is_active'] = 1
        serializer = UserphoneSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response({'errors': serializer.errors},
                                status=status.HTTP_400_BAD_REQUEST)

class SingleUserphoneAPIView(APIView):
    def get(self, request, user_phone_id):
        userphone = Userphone.objects.get(user_phone_id=user_phone_id)
        serializer = UserphoneSerializer(userphone)
        return Response(serializer.data)
    
    @swagger_auto_schema(operation_description="Update User Phone", request_body=UserphoneSerializer)
    def patch(self,request,user_phone_id):
        userphone_obj = Userphone.objects.get(user_phone_id=user_phone_id)
        serializer = UserphoneSerializer(userphone_obj, data=request.data,partial=True)
        if (serializer.is_valid()):
            serializer.save()
            return Response(serializer.data)
        return Response({'errors': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)