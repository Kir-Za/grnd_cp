from django.views.generic.edit import UpdateView, FormView
from django.views.generic import ListView, DeleteView
from django.shortcuts import redirect, reverse
from .models import Quest
from .forms import AddForm
from django.core.urlresolvers import reverse_lazy
from django.db.utils import IntegrityError


class QuestList(ListView, FormView):
    form_class = AddForm
    template_name = "index.html"
    model = Quest
    success_url = reverse_lazy('main')

    def form_valid(self, form):
        form.instance.title = self.request.POST['title']
        form.instance.abstract = self.request.POST['abstract']
        Quest.objects.create(title=self.request.POST['title'], abstract=self.request.POST['abstract'])
        return super(QuestList, self).form_valid(form)


class DelQuestAPI(DeleteView):

    def get(self, request, *args, **kwargs):
        pk = kwargs['pk']
        elem = Quest.objects.get(id=pk)
        elem.delete()
        return redirect(reverse_lazy('main'))