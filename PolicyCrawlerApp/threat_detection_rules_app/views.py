from .utils import *
# Create your views here.
@csrf_exempt
def export_threat_detection_rules_xls(request):
    return export_data(request)

def SearchEngine(request):
    template = 'thread_detection_rules.html'
    return search(request, template)

@csrf_exempt
def Index(request):
    template = 'thread_detection_rules.html'

    if request.method == "GET":
        rules = Tblpolicies.objects.all().filter(policytype__icontains='detection')
        return render(request, template, {'rules': rules})
    if request.method == "POST":
        serializer = ThreatDetectionRuleSerializer(data=request.POST)
        if serializer.is_valid():
            serializer.save()
        print(serializer.errors)
        rules = Tblpolicies.objects.all().filter(policytype__icontains='detection')
        return render(request, template, {'rules': rules})
    if request.method == "PUT":
        return update_data(request, template)

    if request.method == "DELETE":
        return delete_data(request, template)



