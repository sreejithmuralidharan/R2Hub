from django.http import HttpResponse
from django.contrib.auth.models import User
import json

# Django REST Framework
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import APIRequestSerializer
from rest_framework.exceptions import APIException

from collection.models import APIRequest, Collection
from organizations.models import Organization, OrganizationUser


@api_view(['GET', 'POST'])
def webhook_listener(request, collection_id):
    collection_obj = Collection.objects.get(id=collection_id)
    organization_obj = Organization.objects.get(
        id=collection_obj.organization.id)
    organization_user_obj = OrganizationUser.objects.filter(
        user=request.user, organization=organization_obj)
    if organization_user_obj.exists():
        if request.method == 'POST':
            try:
                api_request = APIRequest()
                api_request.collection = Collection.objects.get(
                    id=collection_id)
                api_request.request_header = dict(request.headers)
                api_request.request_body = json.loads(request.body)
                api_request.created_by = User.objects.get(
                    username=request.user)
                api_request.save()
                return Response(data=json.loads(request.body), status=201)
            except Exception as e:
                error = {
                    'error': str(e)
                }
                return Response(data=error, status=400)

        elif request.method == 'GET':
            qs = APIRequest.objects.filter(collection=collection_id)
            serializer = APIRequestSerializer(qs, many=True)
            return Response(serializer.data)

        else:
            return HttpResponse('Webhook listener works!')
    else:
        error = {
            'error': 'You are not authorized to perform this action'
        }
        return Response(data=error, status=401)
