from django import forms
from .models import Post


class PostForm(forms.Form):

    def __init__(self, request, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.request = request
    
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
        },
        widget=forms.Textarea,
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

        
        self.error = ""
        if not img_url:
            self.add_error('img_url', '이미지 주소가 없습니다')
            self.error += '이미지 주소가 없습니다\n'
        if not description:
            self.add_error('description', '내용이 없습니다')
            self.error += '내용이 없습니다\n'
