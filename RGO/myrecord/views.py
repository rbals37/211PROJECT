from django.shortcuts import render
import calendar
from datetime import datetime
from .models import Post



def record_by_date(request, date):
    # URL에서 받은 날짜를 파싱
    date_obj = datetime.strptime(date, "%Y-%m-%d")
    date_year = date_obj.year
    date_month =  date_obj.month
    date_day = date_obj.day
    posts = Post.objects.filter(created_at__date=date_obj)

    return render(request, 'record_by_date.html', {'posts': posts, 'date': date_obj,'year':date_year, 'month':date_month, 'day':date_day})




def calendar_view(request,year= None, month = None):
    today = datetime.today()
    posts = Post.objects.filter(created_at__year=today.year, created_at__month=today.month)
    year = year or today.year
    month = month or today.month

    # 달력 생성 (간단한 HTML 구조)
    cal = calendar.HTMLCalendar()
    calendar_html = cal.formatmonth(today.year, today.month)
    
    # 각 날짜 칸에 게시글 제목 추가
    for post in posts:
        post_date = post.created_at.day  # 날짜 (1~31)
        # HTML에서 특정 날짜를 <a> 링크로 감싸기
        calendar_html = calendar_html.replace(
            f">{post_date}<",
            f"><a href='/posts/{today.year}-{today.month:02d}-{post_date:02d}/'>{post_date}</a><br>{post.title}<"
        )
    
    context = {
        'calendar_html': calendar_html,
        'year': year,
        'month': month,
    }

    return render(request, 'myrecord.html', context)


