from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.views.generic import View
from django.template.loader import get_template
from proyecto.models import Autor, Proyecto

from .utils import render_to_pdf 

class GeneratePdf(View):
    def get(self, request, project_id, *args, **kwargs):
        template = get_template('proyecto.html')
        project =  get_object_or_404(Proyecto, pk=project_id)
        context = {
            "project_id": project.id,
            "project_img": project.img, 
            "project_name": project.name,
            "project_desc": project.desc,
            "project_autor": project.autor,
        }
        html = template.render(context)
        pdf = render_to_pdf('proyecto.html', context)
        if pdf:
            response = HttpResponse(pdf, content_type='application/pdf')
            filename = "Project_%s.pdf" %("12341231")
            content = "inline; filname=%s" %(filename)
            download = request.GET.get("download")
            if download:
                content = "attachment; filename=%s" %(filename)
            response['Content-Disposition'] = content
            return response
        return HttpResponse("Not Found")
    

def index(request):
    authors = Autor.objects.all()
    projects = Proyecto.objects.all()
    return render(request,'index.html',{'authors':authors,'projects':projects})