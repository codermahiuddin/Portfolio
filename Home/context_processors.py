from About.models import AuthorPeronal,CvUpload

def Author(request):
    try:
        authorPeronal = AuthorPeronal.objects.get(FullName='Md Mahiuddin')
        return {'authorPeronal':authorPeronal}
    except Exception:
        authorPeronal = ''
        return {'authorPeronal':authorPeronal}


def Cv(request):
    try:
        cv = CvUpload.objects.get(name='Md Mahiuddin')
        return {'cv':cv}
    except Exception:
        cv = ''
        return {'cv':cv}