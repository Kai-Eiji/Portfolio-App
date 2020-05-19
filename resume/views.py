from django.shortcuts import render
from resume.models import Resume

# Create your views here.
def resume_view(request):
    files = Resume.objects.order_by('-date')
    new_file = files[0]
    other_files = files[1:]
    context = {
        'new_file':new_file,
        'other_files':other_files,
    }
    return render(request,'resume/resume_view.html', context)

