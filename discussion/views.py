from datetime import datetime
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect

from discussion.forms import ShareForm, ShareReplyForm, ShareRepliesForm
from discussion.models import Share, ShareReply


@login_required()
def share(request):
    shares = Share.objects.all()
    user_u = User.objects.all()
    return render(request, 'main_page.html',
                  {'user_u': user_u, 'shares': shares, })


@login_required()
def deleteshare(request, pk1):
    shares = Share.objects.filter(id=pk1)
    sharereply = ShareReply.objects.filter(share_id=pk1)
    sharereply.delete()
    shares.delete()
    return redirect('share:share')


@login_required()
def deletereply(request, pk2):
    shareply = ShareReply.objects.filter(id=pk2)
    sharepl = ShareReply.objects.get(id=pk2)
    id = sharepl.share_id
    shareply.delete()
    return redirect('share:replies', id)


@login_required()
def sharecomment(request):
    current_datetime = datetime.now()
    if request.method == 'POST':
        comment_form = ShareReplyForm(request.POST, initial={'user_id': request.user.id, 'timestamp': current_datetime})
        pk1 = request.POST['pk']
        if comment_form.is_valid():
            # pk1 = Thread.pk
            comment_form.cleaned_data['timestamp'] = datetime.now()
            com = comment_form.save(commit=False)
            com.timestamp = datetime.now()
            com.save()
            lists = ShareReply.objects.filter(share_id=pk1)
            questions = Share.objects.filter(id=pk1)
            user_u = User.objects.all()
            args = {'lists': lists, 'user_u': user_u, 'questions': questions}
            return redirect('share:replies', pk1)

        else:
            print(comment_form.errors)
            return HttpResponseRedirect(reverse('share:share'))

    else:
        comment_form = ShareReplyForm()
        return render(request, 'main_page.html', {'comment_form': comment_form})


@login_required()
def sharecomments(request, pk):
    current_datetime = datetime.now()
    lists = ShareReply.objects.filter(share_id=pk)
    user_u = User.objects.all()
    questions = Share.objects.filter(id=pk)
    if request.method == 'POST':
        reply_form = ShareRepliesForm(request.POST, initial={'user_id': request.user.id, 'share_id': pk,
                                                             'timestamp': current_datetime})
        if reply_form.is_valid():
            reply_form.cleaned_data['timestamp'] = datetime.now()
            new = reply_form.save(commit=False)
            new.user_id = request.user.id
            new.share_id = pk
            new.timestamp = datetime.now()
            new.save()
            return redirect('share:replies', pk)
    else:
        reply_form = ShareRepliesForm(
            initial={'user_id': request.user.id, 'share_id': pk, 'timestamp': current_datetime})
    return render(request, 'replies_per_share.html',
                  {'reply_form': reply_form, 'lists': lists, 'user_u': user_u, 'questions': questions})


@login_required()
def add_share(request):
    current_datetime = datetime.now()
    ques = Share.objects.all()
    if request.method == 'POST':
        q_form = ShareForm(request.POST, initial={'timestamp': current_datetime})
        if q_form.is_valid():
            q_question = q_form['question'].value()
            q_user = request.user
            t = Share.objects.create(question=q_question, user_id=request.user.id, timestamp=datetime.now())
            t.save()
            return redirect('share:share')

        else:
            return HttpResponseRedirect(reverse('mywebsite:student'))

    else:
        q_form = ShareForm(initial={'timestamp': current_datetime})
    return render(request, 'add_share.html', {'q_form': q_form, 'ques': ques})
