from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, PasswordChangeForm
from django.contrib.auth import get_user_model
from django import forms
from django.core.exceptions import ValidationError


class LoginUserForm(AuthenticationForm):
    username = forms.CharField(
        label="Логин",
        widget=forms.TextInput(
            attrs={"class": "form-input"}
        )
    )
    password = forms.CharField(
        label="Пароль",
        widget=forms.PasswordInput(
            attrs={"class": "form-input"}
        )
    )
    
    class Meta:
        model = get_user_model()
        

class RegisterUserForm(UserCreationForm):
    username = forms.CharField(
        label="Логин",
        widget=forms.TextInput(
            attrs={"class": "form-input"}
        )
    )
    password1 = forms.CharField(
        label="Пароль",
        widget=forms.TextInput(
            attrs={"class": "form-input"}
        )
    )
    password2 = forms.CharField(
        label="Повтор пароля",
        widget=forms.TextInput(
            attrs={"class": "form-input"}
        )
    )
    
    class Meta:
        model = get_user_model()
        fields = ["username", "email", "first_name", "last_name", "password1", "password2"]
        labels = {
            "email": "E-mail",
            "first_name": "Имя",
            "last_name": "Фамилия"
        }
        widgets = {
            "email": forms.EmailInput(
                attrs={"class": "form-input"}
            ),
            "first_name": forms.TextInput(
                attrs={"class": "form-input"}
            ),
            "last_name": forms.TextInput(
                attrs={"class": "form-input"}
            ),
        }
        
    def clean_email(self):
        email = self.cleaned_data["email"]
        
        if get_user_model().objects.filter(email=email).exists():
            raise ValidationError("Почта уже существует")
        return email
    

class ProfileUserForm(forms.ModelForm):
    username = forms.CharField(
        disabled=True,
        label="Логин",
        widget=forms.TextInput(
            attrs={
                "class": "form-input"
            }
        )
    )
    
    email = forms.EmailField(
        disabled=True,
        label="E-mail",
        widget=forms.EmailInput(
            attrs={
                "class": "form-input"
            }
        )
    )
    
    class Meta:
        model = get_user_model()
        fields = ["username", "email", "first_name", "last_name"]
        labels = {
            "first_name": "Имя",
            "last_name": "Фамилия",
        }
        widgets = {
            "first_name": forms.TextInput(
                attrs={
                    "class": "form-input"
                }
            ),
            "last_name": forms.TextInput(
                attrs={
                    "class": "form-input"
                }
            )
        }
        

class UserPasswordChangeForm(PasswordChangeForm):
    old_password = forms.CharField(
        label="Старый пароль",
        widget=forms.PasswordInput(
            attrs={
                "class": "form-input"
            }
        )
    )
    new_password1 = forms.CharField(
        label="Новый пароль",
        widget=forms.PasswordInput(
            attrs={
                "class": "form-input"
            }
        )
    )
    new_password2 = forms.CharField(
        label="Подтверждение пароля",
        widget=forms.PasswordInput(
            attrs={
                "class": "form-input"
            }
        )
    )