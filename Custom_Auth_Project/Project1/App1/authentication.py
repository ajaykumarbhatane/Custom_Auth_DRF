from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import AuthenticationFailed
from django.contrib.auth.models import User

from django.contrib.auth import authenticate,get_user_model

class CustomAuthentication(BaseAuthentication):
    def authenticate(self, request):
        username=request.GET.get('username')
        print('username=',username)
        password=request.GET.get('password')
        print('password=',password)
        if not username or not password:
            raise AuthenticationFailed('Not valid ')
        credentials={get_user_model().USERNAME_FIELD:username,'password':password}
        user=authenticate(**credentials)
        if user is None:
            raise AuthenticationFailed('User is None')
        if not user.is_active:
            raise AuthenticationFailed('user is Inactive')
        return (user,None)


        # try:
        #     user=User.objects.filter(username=username)
        #     mpw=make_password(password)
        #     print('mpw=',mpw)
        #     for u in user:
        #         print('db pass=',u.password)
        #     pw=User.objects.get(password=mpw)
        # except User.DoesNotExist:
        #     raise AuthenticationFailed('No such Type of User')
        # return (user,pw,None)


