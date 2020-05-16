from django import forms
from .models import Dsuser
from django.contrib.auth.hashers import check_password, make_password


class RegisterForm(forms.Form):
    user_id = forms.CharField(
        label="아이디",
        required=True, 
        error_messages={
            'required': '아이디를 입력하십시오'
        }
    )

    email = forms.EmailField(
        label="이메일",
        required=True, 
        error_messages={
            'required': '이메일을 입력하십시오'
        }
    )

    password = forms.CharField(
        label="비밀번호",
        required=True, 
        error_messages={
            'required': '비밀번호를 입력하십시오'
        },
        widget=forms.PasswordInput
    )

    re_password = forms.CharField(
        label="비밀번호 확인",
        required=True, 
        error_messages={
            'required': '비밀번호를 입력하십시오'
        },
        widget=forms.PasswordInput
    )

    def clean(self):
        cleaned_data = super().clean()
        
        user_id = cleaned_data.get('user_id')
        email = cleaned_data.get('email')
        password = cleaned_data.get('password')
        re_password = cleaned_data.get('re_password')

        print(password, re_password)

        if user_id and email and password and re_password:
            if password != re_password:
                print("password not same")
                self.add_error('password', '비밀번호가 서로 다릅니다')
                self.add_error('re_password', '비밀번호가 서로 다릅니다')
                self.error = "비밀번호가 서로 다릅니다"
                return
        else:
            self.error = "모든 값을 입력해야합니다"

class LoginForm(forms.Form):
    user_id = forms.CharField(
        label="아이디",
        required=True, 
        error_messages={
            'required': '아이디를 입력하십시오'
        }
    )

    password = forms.CharField(
        label="비밀번호",
        required=True, 
        error_messages={
            'required': '비밀번호를 입력하십시오'
        },
        widget=forms.PasswordInput
    )

    def clean(self):
        cleaned_data = super().clean()
        
        user_id = cleaned_data.get('user_id')
        password = cleaned_data.get('password')

        if user_id and password:
            try:
                login_dsuser = Dsuser.objects.get(user_id=user_id)
            except Dsuser.DoseNotExist as e:
                print(e)
                self.add_error('user_id', '아이디가 없습니다')
                self.error = "아이디가 없습니다"
                return
            except Exception as e:
                print(e)
                self.add_error('user_id', '알수없는 오류')
                self.error("알수없는 오류 발생")
                return

            if not check_password(password, login_dsuser.password):
                self.add_error('password', '비밀번호를 틀렸습니다')
                self.error("비밀번호를 틀렸습니다")
            else:
                self.pk = login_dsuser.pk
        else:
            self.error = "모든 값을 입력해야합니다"