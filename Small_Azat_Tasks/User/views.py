from django.shortcuts import render, redirect, HttpResponseRedirect
from django.contrib import messages
from .models import *
from django.http import JsonResponse, HttpResponseForbidden
from django.template.loader import render_to_string
from .forms import *
from django.urls import reverse
from Requests.models import *
from Requests.forms import *
from django.utils import timezone


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            name = form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created!. Now able to log in')
            return redirect('login_url')
    else:
        form = UserRegisterForm()
    return render(request, 'user/register.html', context={'form': form})


def profiles(request):
    profile = Profile.objects.get_or_create(user=request.user)
    requests = Requests.objects.filter(user=request.user).order_by('id')

    if request.method == 'POST':
        request_form = RequestForm(request.POST, request.FILES)

        if request_form.is_valid():
            content = request.POST.get('content')
            yesterday = timezone.now() - timezone.timedelta(days=1)
            if Requests.objects.filter(user=request.user, wrote_date__gt=yesterday).exists():
                return HttpResponseForbidden()

            comment = Requests.objects.create(user=request.user, content=content)
            comment.save()
            return HttpResponseRedirect(reverse('profile_url'))

    else:
        request_form = RequestForm()

    context = {
        'comments': requests,
        'comment_form': request_form,
    }

    if request.is_ajax():
        html = render_to_string('user/requests.html', context, request=request)
        return JsonResponse({'form':html})

    return render(request, 'user/profile.html', context)


def message_delete(request, id):
    comment = Requests.objects.get(id=id)
    comment.delete()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))