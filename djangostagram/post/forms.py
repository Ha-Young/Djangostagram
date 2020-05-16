from django import forms
from .models import Post


class PostForm(forms.Form):
    img_url = forms.CharField(
        label="이미지 주소",
        required=True, 
        error_messages={
            'required': '이미지 주소를 입력하십시오'
        }
    )

    description = forms.TextField(
        label="내용",
        required=True, 
        error_messages={
            'required': '내용을 입력하십시오'
        }
    )

    tag = forms.CharField(
        label="태그",
        required=False,
    )

    def clean(self):
        cleaned_data = super().clean()
        
        img_url = cleaned_data.get('img_url')
        description = cleaned_data.get('description')
        tag = cleaned_data.get('tag')

        if not img_url:
            self.add_error('img_url', '이미지 주소가 없습니다.')
        if not description:
            self.add_error('description', '내용이 없습니다.')