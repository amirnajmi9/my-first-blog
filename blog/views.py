from django.template import loader
from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse,Http404
from .models import post
from .forms import PostForm
from django.utils import timezone
from django.shortcuts import redirect
import random as rn
from kavenegar import *
from .kar import karn
from .forms import codeform

######################################################################################################

def index(request):
	latest_post_list=post.objects.order_by('-publish')
	request.session['member_id'] = 0
	context = {
	   'latest_post_list' : latest_post_list,

	}
	return render(request ,'index.html', context)









###########################################################################################################











def dste(request,daste):
    print(daste)
    latest_post_list=post.objects.filter(daste = daste).all()
    request.session['member_id'] = 0
    context = {
       'latest_post_list' : latest_post_list,

    }
    return render(request ,'index.html', context)

def detail(request,post_id):
	Post = get_object_or_404(post , pk = post_id)
	context = {

	   'post': Post,

	}
	return render(request ,'detail.html', context)










def kave(request):
    if request.method == 'POST':
        filled_form = codeform(request.POST)
        user = request.session["user"]
        post_id = request.session["post_id"]
        Post = get_object_or_404(post , pk = post_id + 86)
        if filled_form.is_valid():
            note = filled_form.cleaned_data['number']
            if Post.code == note:
                Post.vrf = '1'
                Post.save()
                return redirect('blog/')
    else:
        form = codeform()
        return render(request, 'code.html', {'codeform':form})



def post_new(request):
    ##item = karn()
    if request.method == "POST":
        form = PostForm(request.POST,request.FILES)
        if form.is_valid():
            post1 = form.save(commit=False)
            user = form.cleaned_data['user']
            post1.author = request.user
            post1.published_date = timezone.now()
            post1.save()
            post_id = post.objects.count()
            request.session["post_id"] = post_id 
            Post = get_object_or_404(post , pk = post_id + 86)
            kar = karn(user,Post.code)
            kar.ngar()
            print(Post.code)
            request.session["user"] = user
            #return HttpResponse(Post.code)
            return redirect('code/')
        else:
        	print('re')
    else:
        form = PostForm()
    return render(request, 'post_edit.html', {'form': form})
