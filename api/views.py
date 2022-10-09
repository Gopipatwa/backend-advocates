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



# Get All Company data and ID based Data ID must be integer format
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
        if query:
            resp = serializers.CompanySerializer(query,many=True)
            advocatedata = Advocates.objects.filter(company = resp.data[0]['name'])
            resp_advocate = serializers.AdvocatesSerializer(advocatedata,many=True)
            resp.data[0]['advocates'] = resp_advocate.data
            return Response(resp.data)
        return Response(f"Not found id {id}")


# Get All Advocate data and ID based Data ID must be integer format
@api_view(['GET'])
def advocates(request,id:int=None):
    if id==None:
        data = serializers.AdvocatesSerializer(Advocates.objects.all(),many=True)
        for per in data.data:
            sociallink = SocialLink.objects.filter(advocate_id = per['id'])
            find_company = Company.objects.filter(name=per['company'])
            company = serializers.CompanySerializer(find_company,many=True)
            company.data[0]['href'] = f"companies/{company.data[0]['id']}"
            per['company'] = company.data[0]
            if sociallink:
                social_resp = serializers.SocialSkillSerializer(sociallink,many=True)
                per['links'] = {i['platform_name']:i['link'] for i in social_resp.data}
            else:
                per['links']=[]
        return Response(data.data)
    else:
        query = Advocates.objects.filter(id=id)
        if query:
            resp = serializers.AdvocatesSerializer(query,many=True)
            
            find_company = Company.objects.filter(name=resp.data[0]['company'])
            company = serializers.CompanySerializer(find_company,many=True)
            company.data[0]['href'] = f"companies/{company.data[0]['id']}"
            resp.data[0]['company'] = company.data[0]


            sociallink = SocialLink.objects.filter(advocate_id = resp.data[0]['id'])
            if sociallink:
                social_resp = serializers.SocialSkillSerializer(sociallink,many=True)
                resp.data[0]['links'] = {i['platform_name']:i['link'] for i in social_resp.data}
            else:
                resp.data[0]['links'] = []
            return Response(resp.data)
        return Response(f"Not found id {id}")