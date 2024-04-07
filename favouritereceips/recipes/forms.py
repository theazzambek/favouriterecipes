from allauth.account.forms import SignupForm, LoginForm
from django import forms


class CustomSignUpForm(SignupForm):
    first_name = forms.CharField(max_length=30, label='Имя')
    last_name = forms.CharField(max_length=30, label='Фамилия')

    def __init__(self, *args, **kwargs):
        super(CustomSignUpForm, self).__init__(*args, **kwargs)

        del self.fields['username']

    def save(self, request):
        user = super(CustomSignUpForm, self).save(request)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.save()
        return user


# class CustomLoginForm(LoginForm):
#     def __init__(self, *args, **kwargs):
#         super(CustomLoginForm, self).__init__(*args, **kwargs)
#         # Удаляем поле имени пользователя
#         del self.fields['login']
#         # Заменяем его на поле электронной почты
#         self.fields['email'] = forms.EmailField(label=("Email"))
#
#     def user_credentials(self):
#         """
#         Provides the credentials required to authenticate the user for
#         login.
#         """
#         credentials = {}
#         login = self.cleaned_data["email"]  # Заменяем "login" на "email"
#         credentials["email"] = login  # Используем "email" вместо "username" или "email"
#         credentials["password"] = self.cleaned_data["password"]
#         return credentials
