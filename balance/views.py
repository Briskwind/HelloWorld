import logging

import datetime
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView

logger = logging.getLogger('admin_log')

class Home(APIView):
    """ home page """

    view_name = 'home'
    # template_name = 'home/index.html'

    def get(self, request):
        context = dict()
        now = datetime.datetime.now()
        logger.info(now)
        return HttpResponse('this is ok')
