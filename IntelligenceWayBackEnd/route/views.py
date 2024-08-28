from django.shortcuts import render
import json

# Create your views here.
def index(request):
    return render(request, 'index.html')

def profile(request):
    user = request.user
    auth_0user = user.social_auth.get(provider='auth0')
    

    user_data = {
        'user_id': auth_0user.uid,
        'name': user.first_name,
        'picture': auth_0user.extra_data['picture']
    }


    context = {
        'user_data' : json.dumps(user_data, indent=4),
        'auth_0user' : auth_0user
    }





    return render(request, 'profile.html', context)