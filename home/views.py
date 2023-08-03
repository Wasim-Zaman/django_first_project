from django.shortcuts import render
from home.models import *

# Create your views here.

def upload_user(request):
    
    '''
        A function that will store the recipe name, description, and image into 
        the database
    '''

    if request.method == "POST":
        
        data = request.POST
        file_data = request.FILES

        name = data.get('name')
        description = data.get('description')
        image = file_data.get('image')

        User.objects.create(
            name = name,
            description = description,
            image = image,
        )

        print('User added to the database')

        # store data into the database

    return render(request, "home.html")