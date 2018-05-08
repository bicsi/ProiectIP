import uuid

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views import generic

from . import forms
from . import models


class ImageCreate(LoginRequiredMixin, generic.FormView):
    form_class = forms.ImageAddForm
    success_url = reverse_lazy('my_album')
    template_name = 'images/upload-image.html'

    def form_valid(self, form):
        original_image = form.cleaned_data['original_image']
        title = form.cleaned_data['title']

        bw, color = models.ImageConversion.convert(original_image)
        # Random names for conversions
        name = str(uuid.uuid4()) + '.jpg'

        model_image = models.ImageConversion()

        model_image.title = title
        model_image.author = self.request.user
        model_image.original_image.save(name, original_image)
        model_image.bw_image.save(name, bw)
        model_image.color_image.save(name, color)

        model_image.save()

        return super().form_valid(form)


class ImageDelete(LoginRequiredMixin, generic.DeleteView):
    model = models.ImageConversion
    success_url = reverse_lazy('my_album')

    def get_queryset(self):
        return models.ImageConversion.objects.filter(author__exact=self.request.user)


class AlbumView(LoginRequiredMixin, generic.ListView):
    template_name = 'images/album.html'
    model = models.ImageConversion
    context_object_name = 'image_list'
    paginate_by = 20
    author = None

    def dispatch(self, request, *args, **kwargs):
        username = kwargs.get('username', request.user.username)
        self.author = get_object_or_404(User, username=username)

        return super(AlbumView, self).dispatch(request, *args, **kwargs)

    def get_queryset(self):
        return models.ImageConversion.objects.filter(author__exact=self.author)


class LatestView(generic.ListView):
    template_name = 'images/latest.html'
    model = models.ImageConversion
    context_object_name = 'image_list'

    def get_queryset(self):
        return models.ImageConversion.objects.order_by('-created')
