from django.shortcuts import render
from django.shortcuts import render , redirect
from .models import Post , Comment
from .forms import CommentForm



# Create your views here.

def post_list (request):

    data = Post.objects.all()

    context = {
        'object_list' : data
    }
    return render(request,'posts/post_list.html',context)



def post_detail (request,slug) :
    data = Post.objects.get(slug = slug)
    comments = Comment.objects.filter(post=data)
    if request.method == 'POST' :
        form = CommentForm(request.POST)
        if form.is_valid():
            myform = form.save(commit=False)
            myform.post = data
            myform.save()
    else :
        form = CommentForm()
    context = {
        'post' : data,
        'comments': comments,
        'form' : form,
    }
    return render (request , 'posts/post_detail.html' , context)



# def create_post(request):
#     if request.method == 'POST' :
#         form = PostForm(request.POST,request.FILES)
#         if form.is_valid() :
#             myform = form.save(commit=False)
#             myform.author = request.user
#             myform.save()
#             return redirect ('/posts/')
#     else :
#         form = PostForm()

#     return render (request,'posts/post_form.html',{'form':form})

# def edit_post(request,pk):
#     post = Post.objects.get(id=pk)

#     if request.method == 'POST' :
#         form = PostForm(request.POST,request.FILES,instance=post)
#         if form.is_valid() :
#             myform = form.save(commit=False)
#             myform.author = request.user
#             myform.save()
#             return redirect ('/posts/')
#     else :
#         form = PostForm(instance=post)

#     return render (request,'posts/edit.html',{'form':form})


# def delete_post(request,pk):
#     post = Post.objects.get(id=pk)
#     post.delete()
#     return redirect ('/posts/')