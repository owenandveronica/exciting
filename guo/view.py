from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render


def router(request, templates):
    # user_cookie = request.COOKIES.get('username')
    url = request.path
    # if not user_cookie:
    #   if url != '/index/' and (url != '/signin/'):
    #     return HttpResponseRedirect('/index/')
    # if user_cookie:
    if request == '':
        return render(request, 'index.html')
    if request.user.is_authenticated():
        if url != '/homepage/':
            return HttpResponseRedirect('/homepage/')
    if not request.user.is_authenticated():
        if url != '/index/' and (url != '/signin/'):
            return HttpResponseRedirect('/index/')
    return render(request, '' + templates + '.html')
