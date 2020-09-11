
from django.shortcuts import render
from django.shortcuts import redirect
from django.shortcuts import reverse
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin

from django.contrib import messages
from django.conf import settings
from django.contrib.auth.models import User, Group
# Create your views here.
from rest_framework.authtoken.models import Token
from django.conf import settings
from django.http import Http404, HttpResponse, HttpResponseForbidden
from django.core.exceptions import ObjectDoesNotExist
import uuid
from drf_advanced_token_manager.models import UserUIKeyLock

class TokenView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        try:
            token = Token.objects.get(user=request.user)
        except ObjectDoesNotExist as odne:
            token = Token.objects.create(user=request.user, key=str(uuid.uuid4()))

        home_url = reverse(settings.SITE_HOME_URL_NAME) if hasattr(settings,"SITE_HOME_URL_NAME") else "/"

        if (hasattr(settings,"PREVENT_TOKEN_UI_CHANGE") and settings.PREVENT_TOKEN_UI_CHANGE) or UserUIKeyLock.objects.filter(user=request.user).exists():
            change_lock = True
        else:
            change_lock = False

        return render(request, "drf_token_management_view_token.html",
         {"token":token,"site_home":home_url, "change_lock":change_lock})
        

    def post(self, request, *args, **kwargs):
        raise NotImplementedError


class ChangeTokenView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        # are you sure page
        if UserUIKeyLock.objects.filter(user=request.user).exists():
            print("locked")
            return HttpResponseForbidden("You are not allowed to change your token :P")
        if hasattr(settings,"PREVENT_TOKEN_UI_CHANGE") and settings.PREVENT_TOKEN_UI_CHANGE:
            print("token change locked")
            return HttpResponseForbidden("You are not allowed to change your token :P")
        home_url = reverse(settings.SITE_HOME_URL_NAME) if hasattr(settings,"SITE_HOME_URL_NAME") else "/"
        return render(request, "drf_token_management_change_token.html", 
        {"site_home":home_url})

    def post(self, request, *args, **kwargs):
        if UserUIKeyLock.objects.filter(user=request.user).exists():
            return HttpResponseForbidden("You are not allowed to change your token :P")
        token = Token.objects.get(user=request.user)
        token.delete()
        token = Token.objects.create(user=request.user, key=str(uuid.uuid4()))
        return redirect(reverse('drf_advanced_token_manager.view'))
        


