from django.shortcuts import render
import calendar
from datetime import date
from .models import Post



def calendar_view(request, year= None, month = None):
    today = date.today()
    year = year or today.year
    month = month or today.month

    cal = calendar.HTMLCalendar(firstweekday=6)  # 일요일이 시작
    calendar_html = cal.formatmonth(year, month)
    posts = None
    posts_by_date = {}
    posts = Post.objects.filter(created_at__year=year, created_at__month=month, author=request.user)
    for post in posts:
        day = post.created_at.day
        if day not in posts_by_date:
            posts_by_date[day] = []
        posts_by_date[day].append(post)

    context = {
        'calendar_html': calendar_html,
        'posts_by_date': posts_by_date,
        'year': year,
        'month': month,
    }
    return render(request, 'myrecord.html', context)





