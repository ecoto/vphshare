# Create your views here.
from django.contrib.auth.decorators import login_required
from django.template import RequestContext
from django.shortcuts import render_to_response
from masterinterface import settings


def index(request):
    return render_to_response("cyfronet/index.html",
            {},
        RequestContext(request)
    )

@login_required
def cloudmanager(request):
    return render_to_response("cyfronet/cloudmanager.html",
            {'source': settings.CLOUD_PORTLET_LOGIN_URL_TEMPLATE.format(request.user.username, request.COOKIES.get('vph-tkt','No ticket'), 'cloud')},
        RequestContext(request))

@login_required
def datamanager(request):
    return render_to_response("cyfronet/datamanager.html",
            {'source': settings.CLOUD_PORTLET_LOGIN_URL_TEMPLATE.format(request.user.username, request.COOKIES.get('vph-tkt','No ticket'), 'data')},
        RequestContext(request))