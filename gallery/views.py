from django.shortcuts import render,redirect
from django.http  import HttpResponse,Http404
import datetime as dt
from .models import Image

# Create your views here.
def welcome(request):
    
    return render(request, 'welcome.html')



def uploads(request):
    date = dt.date.today()
    uploads = Image.uploads()
    # category_id = Image.objects.filter(category_id='category_id')

    return render(request, 'posts/current-post.html', {"date": date,"uploads": uploads})

def convert_dates(dates):

    # Function that gets the weekday number for the date.
    day_number = dt.date.weekday(dates)

    days = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday',"Sunday"]

    # Returning the actual day of the week
    day = days[day_number]
    return day    








def past_uploads(request, past_date):

    try:
        # Converts data from the string Url
        date = dt.datetime.strptime(past_date, '%Y-%m-%d').date()

    except ValueError:
        # Raise 404 error when ValueError is thrown
        raise Http404()
        assert False

    if date == dt.date.today():
        return redirect(uploads)
    uploads = Image.all_uploads(date)
    return render(request, 'posts/post-history.html', {"date": date,"uploads": uploads})







def search_results(request):

    if 'image' in request.GET and request.GET["image"]:
        search_term = request.GET.get("image")
        searched_images = Image.search_image(search_term)
        message = f"{search_term}"

        return render(request, 'posts/search.html',{"message":message,"images": searched_images})

    else:
        message = "Please search for a valid item"
        return render(request, 'posts/search.html',{"message":message})




def image(request,image_id):
   
    image = Image.objects.filter(id = image_id)
    for x in image:
        print(x)
    return render(request,"posts/image.html", {"image":image})


def all(request):
   
    al = Image.objects.all()

    return render(request,"posts/all.html", {"al":al})

