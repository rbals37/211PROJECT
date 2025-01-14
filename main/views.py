from django.shortcuts import render


def main(quest):
    return render(quest,'main.html')