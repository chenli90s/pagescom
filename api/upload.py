from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import uuid

@csrf_exempt
def upload(request):
    files = request.FILES.get('upload_file')
    uu_name = ''
    if files:
        name = files.name
        uu_name = './static/files/'+str(uuid.uuid4())+"."+name.split('.')[1]
        with open(uu_name, 'wb') as f:
            for line in files.chunks():
                f.write(line)
        return JsonResponse(dict(success=True, msg='success', file_path=uu_name))
    return JsonResponse(dict(success=False, msg='filed', file_path=''))