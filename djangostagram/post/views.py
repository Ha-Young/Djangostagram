from django.shortcuts import render, redirect
from django.views.generic import ListView
from django.views.generic.edit import FormView
from django.db import transaction
from django.core.paginator import Paginator

from .models import Post
from .forms import PostForm
from dsuser.models import Dsuser
from tag.models import Tag
# Create your views here.


def timeline(request):
    all_post = Post.objects.all().order_by('-registered_dttm')
    page = request.GET.get('p', 1)
    paginator = Paginator(all_post, 4)
    post_list = paginator.get_page(page)
    
    user_id = request.session.get('user')
    if user_id:
        dsuser = Dsuser.objects.get(pk=request.session.get('user'))
        if dsuser:
            return render(request, 'timeline.html', {'user_id': dsuser.user_id, 'post_list':post_list})

    return render(request, 'timeline.html', {'post_list':post_list})

    

class UploadPost(FormView):
    model = Post
    template_name = 'upload_post.html'
    form_class = PostForm
    success_url = '/'

    def form_valid(self, form):
        with transaction.atomic():
            tags = form.data.get('tags').split(',')
            
            print('request session user', self.request.session.get('user'))         
            new_post = Post(
                writer=Dsuser.objects.get(pk=self.request.session.get('user')),
                img_url=form.data.get('img_url'),
                description=form.data.get('description'),
            )
            new_post.save()

            for tag in tags:
                if not tag:
                    continue
            
                _tag, _ = Tag.objects.get_or_create(name=tag)
                new_post.tags.add(_tag)

        return super().form_valid(form)

    def get_form_kwargs(self, **kwargs):
        kw = super().get_form_kwargs(**kwargs)
        kw.update({
            'request':self.request
        })
        return kw