from django.http import JsonResponse
from django.shortcuts import render, HttpResponseRedirect
from django.template.loader import render_to_string

from .forms import *
from django.urls import reverse


def report_detail(request, id):
    requests = Requests.objects.all().order_by('-id')

    if request.method == 'POST':
        request_form = RequestForm(request.POST or None)
        if request_form.is_valid():
            content = request.POST.get('content')
            # reply_id = request.POST.get('comment_id')
            comment_qs=None
            # if reply_id:
            #     comment_qs = Comment.objects.get(id=reply_id)
            comment = Requests.objects.create(user=request.user, content=content,)
            comment.save()
            return HttpResponseRedirect(reverse('report_detail_url', kwargs={'id': report.id}))

    else:
        comment_form = RequestForm()

    context = {
        'comments': requests,
        'comment_form': request_form,
    }

    if request.is_ajax():
        html = render_to_string('obrazovanie/comments.html', context, request=request)
        return JsonResponse({'form':html})

    return render(request, 'obrazovanie/report_detail.html', context)
