from .utils import *
# Create your views here.
@csrf_exempt
def export_policies_xls(request):
    return export_data(request)

def SearchEngine(request):
    template = 'policies.html'
    return search(request, template)

@csrf_exempt
def Index(request):
    template = 'policies.html'

    if request.method == "GET":
        policies = Tblpolicies.objects.all().filter(policytype__icontains='config')
        return render(request, template, {'policies': policies})
    if request.method == "POST":
        serializer = PolicySerializer(data=request.POST)
        if serializer.is_valid():
            serializer.save()
        print(serializer.errors)
        policies = Tblpolicies.objects.all().filter(policytype__icontains='config')
        return render(request, template, {'policies': policies})
    if request.method == "PUT":
        return update_data(request, template)

    if request.method == "DELETE":
        return delete_data(request, template)
