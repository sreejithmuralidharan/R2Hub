from django.shortcuts import render
import json
from django.core.serializers.json import DjangoJSONEncoder
from collection.models import Collection, APIRequest
from organizations.models import Organization, Membership


def home_page(request):
    return render(request, 'r2hub/index.html', context={'title': 'R2HUB'})


def collection_page(request, organization_id):
    if request.method == 'GET':
        organization_user_obj = Membership.objects.filter(
            organization=organization_id, user=request.user)
        organization_obj = Organization.objects.filter(id=organization_id)
        print(Collection.objects.filter(organization=organization_id))
        if organization_user_obj.exists():
            context = {
                'collections': Collection.objects.filter(organization=organization_id),
                'title': organization_obj[0].name,
                'organization': organization_obj[0]
            }
            return render(request, 'collection/collection.html', context=context)
    else:
        return render(request, 'collection/collection.html', context={'title': 'R2HUB'})


def api_request_page(request, organization_id, collection_id):
    if request.method == 'GET':
        organization_user_obj = Membership.objects.filter(
            organization=organization_id, user=request.user)
        if organization_user_obj.exists():
            collection_obj = Collection.objects.filter(
                id=collection_id, organization=organization_id)
            if collection_obj.exists():
                api_requests = APIRequest.objects.filter(
                    collection=collection_id)
                context = {
                    'title': collection_obj[0].name,
                    'collection': collection_obj,
                    'api_requests': api_requests,
                    'organization': Organization.objects.get(id=organization_id)
                }

                return render(request, 'collection/api_request.html', context=context)
            else:
                error = {'error': 'Collection not found'}
                return render(request, 'collection/api_request.html', context=error)
        else:
            error = {'error': 'You are not authorized to access this page'}
            return render(request, 'collection/api_request.html', context=error)
    else:
        error = {'error': 'Method not allowed'}
        return render(request, 'collection/api_request.html', context=error)
