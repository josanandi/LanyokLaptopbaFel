from django.shortcuts import render, get_object_or_404
from .models import  Question, Post, Choice
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from django.utils import timezone


def index(request):
    hot_posts = Post.objects.filter(check_for_news=True).order_by('published_date')[:5]
    output = Question.objects.order_by('id')[:5]
    return render(request, 'index/home.html', {'hot_posts':hot_posts, 'output':output})


class DetailView(generic.DetailView):
    model = Question
    template_name = 'index/polls_detail.html'

class ResultsView(generic.DetailView):
    model = Question
    template_name = 'index/polls_results.html'

def vote(request, question_id ):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'index/polls_detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        if selected_choice.text_test:
            selected_choice.votes += 1
            selected_choice.votes_text += " " + request.POST.get("choice_input") + ","
            selected_choice.save()

        else:
            selected_choice.votes += 1
            selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
    return HttpResponseRedirect(reverse('index:polls_results', args=(question.id,)))

class PostList(generic.ListView):
    template_name = 'index/post_list.html'
    context_object_name = 'latest_posts'

    def get_queryset(self):
        """Return the last published posts"""
        return Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')


class PostDetail(generic.DetailView):
    model = Post
    template_name = 'index/post_detail.html'

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'index/post_detail.html', {'post': post})
