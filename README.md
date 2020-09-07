# DRF Advanced Token Manager

https://pypi.org/project/drf-advanced-token-manager/

A UI for users to manage their own tokens with the DRF Advanced Token Package (https://github.com/amp89/drf_advanced_token)

# Install:
pip install --upgrade drf-advanced-token-manager

# Setup:
1. make sure the DRF Advanced Token Package is installed (https://github.com/amp89/drf_advanced_token)
2. Add `drf_advanced_token_manager` under `drf_advanced_token` in INSTALLED_APPS settings:
```
...
'drf_advanced_token',
'drf_advanced_token_manager',
...
```
3. Set `SITE_HOME_URL_NAME` in settings to the __name__ of the url that is the root / base site of your project
4. [OPTIONAL] If you don't want the user to be able to change their own token, add `PREVENT_TOKEN_UI_CHANGE=True`
5. Add `path('token_manager/', include('drf_advanced_token_manager.urls')),` to your base `urls.py` `urlpatterns`


The added urls are now:
View token: `token_manager/` (`name='drf_advanced_token_manager.view'`) (This is the UI where the user can manage their token.)
Change token: `token_manager/change/` (`name='drf_advanced_token_manager.change'`) (Note: There is a link to this in the view url above!)
