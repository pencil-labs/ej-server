"""
All views in one file :P

This should obviously be refactored for later use.
"""
from django.conf.urls import url
from django.forms import ModelForm
from django.shortcuts import render
from django.views.generic import RedirectView, TemplateView

from pushtogether.conversations.models import User

patterns = []


def route(path, template_name=None, **kwargs):
    if template_name is not None:
        return route(path, **kwargs)(TemplateView.as_view(template_name=template_name))

    def decorator(func):
        patterns.append(url(path, func, **kwargs))
        return func

    return decorator


#
# Views
#

# Dummy routes
route(r'^$', name='index')(RedirectView.as_view(pattern_name='conversation-list'))
route(r'about/$', name='about', template_name='pages/about.jinja2')
route(r'faq/$', name='faq', template_name='pages/faq.jinja2')
route(r'usage/$', name='usage', template_name='pages/usage.jinja2')

# Routes
route(r'comments/$', name='comments', template_name='pages/comments.jinja2')
route(r'conversations/$', name='conversation-list', template_name='pages/conversation-list.jinja2')
route(r'conversations/(?P<slug>id)/$', name='conversation-detail', template_name='pages/conversation-detail.jinja2')
route(r'notifications/$', name='notifications', template_name='pages/notifications.jinja2')


class ProfileForm(ModelForm):
    """
    User profile form
    """

    class Meta:
        model = User
        fields = [
            'name', 'email',
            'city', 'state', 'country',
            'gender', 'race',
            'political_movement', 'biography',
            'age', 'occupation',
        ]


class ProfileImageForm(ModelForm):
    class Meta:
        model = User
        fields = ['image']


@route(r'profile/$', name='profile')
def profile_view(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = ProfileForm()

    ctx = dict(
        profile_form=form,
    )
    return render(request, 'pages/profile.jinja2', ctx)
