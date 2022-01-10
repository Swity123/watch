



from django.shortcuts import redirect, render,get_object_or_404
from .models import *
from .form import watchform

# Create your views here.
def watch_list(req):
    obj=watches.objects.all()
    return render(req,'index.html',{'a':obj})

def view_watch(req , pk):
    display = get_object_or_404(watches,pk = pk)
    return render(req,'viewdetail.html',{'display':display})



def edit_watch(req,pk):
    edit = get_object_or_404(watches,pk=pk)
    object = watchform (req.POST or  None, instance = edit)
    if object.is_valid():
        object.save()
        return redirect('main')
    return render(req,'edit.html',{'obj':object})




def delete_watch(req,pk):
    obj = get_object_or_404(watches,pk=pk)
    if req.method == 'POST':
        obj.delete()
        return redirect('main')
    return render(req,'delete.html',{'obj':obj})
