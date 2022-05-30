from django.shortcuts import render

# Create your views here.
def test1(request):
    return render(request, 'test1.html')

def table(request):
    return render(request, 'table.html')     

def grid(request):
    return render(request, 'grid.html')  

def department(request):
    return render(request, 'department.html')  