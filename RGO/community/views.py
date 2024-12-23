from .forms import PostForm
from django.shortcuts import render, get_object_or_404, redirect
from .models import Post

# Create your views here.
def community(request):
    posts = Post.objects.all().order_by('-created_at')  # 최신 게시글이 위에 오도록 정렬
    return render(request, 'community.html', {'posts': posts})

def post_detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)  # 게시글이 존재하지 않으면 404 오류
    return render(request, 'post_detail.html', {'post': post})


def post_create(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user  # 작성자를 현재 로그인한 사용자로 설정
            post.save()
            return redirect('community')  # 게시글 목록으로 리디렉션
    else:
        form = PostForm()
    
    return render(request, 'post_create.html', {'form': form})