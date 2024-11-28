from django.shortcuts import render, redirect
import calendar 
from datetime import datetime
from .models import Post
from django.contrib.auth.decorators import login_required
from .forms import PostForm

@login_required
def record_by_date(request, date):
    # URL에서 받은 날짜를 파싱
    date_obj = datetime.strptime(date, "%Y-%m-%d")
    date_year = date_obj.year
    date_month =  date_obj.month
    date_day = date_obj.day
    posts = Post.objects.filter(created_at__date=date_obj)

    return render(request, 'record_by_date.html', {'posts': posts, 'date': date_obj,'year':date_year, 'month':date_month, 'day':date_day})



@login_required
def calendar_view(request,year= None, month = None):
    today = datetime.today()
    posts = Post.objects.filter(created_at__year=today.year, created_at__month=today.month)
    year = year or today.year
    month = month or today.month

    # 달력 생성 (간단한 HTML 구조)
    cal = calendar.HTMLCalendar()
    cal.setfirstweekday(calendar.SUNDAY)
    calendar_html = cal.formatmonth(today.year, today.month)
    
    # 각 날짜 칸에 게시글 제목 추가
    for day in range(1, 32):  # 1일부터 31일까지 모든 날짜 처리
        search_date = f">{day}<" # 날짜 형식 맞추기
        calendar_html = calendar_html.replace(
            search_date,
            f"><a href='record/{today.year}-{today.month:02d}-{day:02d}/'>{day}</a><"
        )
    
    context = {
        'calendar_html': calendar_html,
        'year': year,
        'month': month,
    }

    return render(request, 'myrecord.html', context)


def record_write(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user  # 작성자를 현재 로그인한 사용자로 설정
            post.save()
            return redirect('myrecord')  # 게시글 목록으로 리디렉션
    else:
        form = PostForm()
    
    return render(request, 'create_record.html', {'form': form})