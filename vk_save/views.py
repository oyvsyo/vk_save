from django.shortcuts import render, redirect
from django.template import Template, Context
from django.http import HttpResponse
import json
import os
import settings
import vk_save.vkapi as vkapi


def index(request):

    context = {}
    return render(request, 'index.html', context)


def get_photos(request):
    if request.method == 'POST':

        url = request.POST['url']
        photos_list = vkapi.get_photos(url)

        content = Context({
            "photos_list": photos_list,
        })


        path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))+'/templates/photos.html'
        with open(path, 'r') as template_file:
            template = Template(template_file.read())
            template_file.close()

        ren_template = template.render(content)

        # print ren_template
        return HttpResponse(
            json.dumps({"html": ren_template}),
            content_type="application/json"
        )
    else:
        return HttpResponse(
            json.dumps({"nothing to see": "go home"}),
            content_type="application/json"
        )