from django.shortcuts import get_object_or_404, redirect
from django.views.generic import CreateView

from webapp.forms import ArticleCommentForm
from webapp.models import Comment, Article


class ArticleCommentCreateView(CreateView):
    model = Comment
    template_name = 'webapp/comment/create.html'
    form_class = ArticleCommentForm

    def form_valid(self, form):
        article = get_object_or_404(Article, pk=self.kwargs.get('pk'))
        comment = form.save(commit=False)
        comment.article = article
        comment.save()
        return redirect('article_view', pk=article.pk)
