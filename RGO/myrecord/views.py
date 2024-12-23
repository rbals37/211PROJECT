from django.shortcuts import render, redirect
import calendar 
from datetime import datetime
from .models import Post
from django.contrib.auth.decorators import login_required
from .forms import PostForm

# 한글화된 HTMLCalendar 클래스 추가
class KoreanHTMLCalendar(calendar.HTMLCalendar):
    KOREAN_WEEKDAYS = ['월', '화', '수', '목', '금', '토', '일']
    KOREAN_MONTHS = ['1월', '2월', '3월', '4월', '5월', '6월',
                     '7월', '8월', '9월', '10월', '11월', '12월']

    def formatweekday(self, day):
        # 요일을 한글로 표시
        return f'<th class="{self.cssclasses[day]}">{self.KOREAN_WEEKDAYS[day]}</th>'

    def formatmonthname(self, year, month, withyear=True):
        # 월 이름을 한글로 표시
        month_name = self.KOREAN_MONTHS[month - 1]
        if withyear:
            return f'<tr><th colspan="7" class="month">{year}년 {month_name}</th></tr>'
        return f'<tr><th colspan="7" class="month">{month_name}</th></tr>'


@login_required
def record_by_date(request, date):
    # URL에서 받은 날짜를 파싱
    date_obj = datetime.strptime(date, "%Y-%m-%d")
    date_year = date_obj.year
    date_month = date_obj.month
    date_day = date_obj.day
    posts = Post.objects.filter(created_at__date=date_obj, author=request.user)

    return render(request, 'record_by_date.html', {
        'posts': posts,
        'date': date_obj,
        'year': date_year,
        'month': date_month,
        'day': date_day
    })

def calendar_view(request, year=None, month=None):
    today = datetime.today()
    posts = Post.objects.filter(created_at__year=today.year, created_at__month=today.month)
    year = year or today.year
    month = month or today.month

    # 한글화된 캘린더 생성
    cal = KoreanHTMLCalendar()
    cal.setfirstweekday(calendar.SUNDAY)
    calendar_html = cal.formatmonth(year, month)
    
    # 각 날짜 칸에 게시글 링크 추가
    for day in range(1, 32):  # 1일부터 31일까지 모든 날짜 처리
        search_date = f">{day}<"  # 날짜 형식 맞추기
        calendar_html = calendar_html.replace(
            search_date,
            f"><a href='record/{year}-{month:02d}-{day:02d}/'>{day}</a><"
        )

    context = {
        'calendar_html': calendar_html,
        'year': year,
        'month': month,
        'posts':posts,
    }

    return render(request, 'myrecord.html', context)


@login_required
def record_write(request, date):
    # URL에서 받은 날짜를 파싱
    initial_date = None
    try:
        initial_date = datetime.strptime(date, '%Y-%m-%d').date()
    except ValueError:
        return redirect('myrecord')  # 잘못된 날짜 형식이라면 캘린더로 이동

    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user  # 작성자 설정
            post.created_at = initial_date  # 글 작성 날짜 설정
            post.save()
            return redirect('record_by_date', date=initial_date)
    else:
        # 폼 초기값 설정
        form = PostForm(initial={'created_at': initial_date})

    return render(request, 'create_record.html', {'form': form, 'date': initial_date})

