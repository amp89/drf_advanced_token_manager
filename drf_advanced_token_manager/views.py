
from django.shortcuts import render
from django.shortcuts import redirect
from django.shortcuts import reverse
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin

from django_app_permissions.views import APIAppAuthView
from django_app_permissions.views import AppAuthView
from django.contrib import messages
from django.conf import settings
from django.contrib.auth.models import User, Group
# Create your views here.
from rest_framework.authtoken.models import Token
from django.conf import settings
from django.http import Http404, HttpResponse, HttpResponseForbidden
from django.core.exceptions import ObjectDoesNotExist
import uuid

class TokenView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        try:
            token = Token.objects.get(user=request.user)
        except ObjectDoesNotExist as odne:
            Token.objects.create(user=request.user, key=str(uuid.uuid4()))

        return render(request, "drf_token_management_view_token.html",
         {"token":token,"site_home":reverse(settings.SITE_HOME_URL_NAME)})
        

    def post(self, request, *args, **kwargs):
        raise NotImplementedError


class ChangeTokenView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        # are you sure page
        if hasattr(settings,"PREVENT_TOKEN_UI_CHANGE") and settings.PREVENT_TOKEN_UI_CHANGE:
            return render(request, "drf_token_management_change_token.html", 
              {"site_home":reverse(settings.SITE_HOME_URL_NAME)})
        else:
            return HttpResponseForbidden()

    def post(self, request, *args, **kwargs):
        token = Token.objects.get(user=user)
        token.key = str(uuid.uuid4())
        token.save()
        return redirect(reverse('drf_advanced_token_manager.view'))
        


