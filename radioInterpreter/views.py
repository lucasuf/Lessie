from django.http import HttpResponse


def index(request):
    '''

    :param request:
    :return:
    '''
    return HttpResponse("This is the page for radio log interpretation")

