from django.shortcuts import render

# Create your views here.


def form1(request):
    if request.method=='POST':
        #print(request.POST)
        #print(request.POST['username'])
        print(request.POST.get('username'))
    return render(request,'form1.html')



'''
example to insert the data
Topic.objects.get_or_create(topic_name=request.POST.get('username'))[0]
'''