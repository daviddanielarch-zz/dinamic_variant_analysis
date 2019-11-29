from django.shortcuts import render

from variant.models import TestModel


def buggy_template(request):
    data = TestModel.objects.all()  # This might return 2**32 elements
    return render(request, 'buggy.html', locals())


def good_template(request):
    data = [':)'] * 100
    return render(request, 'good.html', locals())
