from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from api import serializers
from api.models import *



class home(APIView):
    def get(self,request):
        api_urls = {
        'get all advocates':'/advocates/',
        'advocates':'/advocates/<int:id>',
        'get all Companies':'/companies/',
        'company':'/companies/<int:id>'
        }
        return Response(api_urls)


@api_view(['GET'])
def companies(request,id:int=None):
    if id==None:
        resp = serializers.CompanySerializer(Company.objects.all(),many=True)
        for data in resp.data:
            advocatedata = Advocates.objects.filter(company = data['name'])
            resp_advocate = serializers.AdvocatesSerializer(advocatedata,many=True)
            data['total_advocates'] = len(resp_advocate.data)
        return Response(resp.data)
    else:
        query = Company.objects.filter(id=id)
        print(query)
        if query:
            resp = serializers.CompanySerializer(query,many=True)
            advocatedata = Advocates.objects.filter(company = resp.data[0]['name'])
            resp_advocate = serializers.AdvocatesSerializer(advocatedata,many=True)
            resp.data[0]['advocates'] = resp_advocate.data
            return Response(resp.data)
        return Response(f"Not found id {id}")

@api_view(['GET'])
def advocates(request,id:int=None):
    if id==None:
        data = serializers.AdvocatesSerializer(Advocates.objects.all(),many=True)
        return Response(data.data)
    else:
        query = Advocates.objects.filter(id=id)
        print(query)
        if query:
            resp = serializers.AdvocatesSerializer(query,many=True)
            sociallink = SocialLink.objects.filter(advocate_id = resp.data[0]['id'])
            if sociallink:
                social_resp = serializers.SocialSkillSerializer(sociallink,many=True)
                resp.data[0]['links'] = social_resp.data[0]
            resp.data[0]['links'] = []
            return Response(resp.data)
        return Response(f"Not found id {id}")