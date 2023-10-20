import openai
import csv
from django.shortcuts import render,redirect
from django.http import JsonResponse, HttpResponseRedirect  # Add this import for JSON responses
from .models import *
from myapp.forms import CallBackForm,LoginForm
from django.http import HttpResponse
from django.utils import timezone
from django.views.generic import FormView
from django.contrib.auth import authenticate,login
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm


# Create your views here.
def index(request):
    return render(request,'index.html')

def about_us(request):
    return render(request,'about_us.html')



# Replace 'YOUR_OPENAI_API_KEY' with your actual OpenAI API key
openai.api_key = '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'

def Ai(request):
    messages = ChatMessage.objects.all()  # Retrieve existing chat messages

    if request.method == 'POST':
        text = request.POST.get('user_input')
        print("User input:", text)

        # Perform OpenAI chat completion
        output = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": f"{text} in 50 words"}],
        )
        response = output['choices'][0]['message']['content']
        print("Response:", response)

        # Save user input and bot response to the database
        ChatMessage.objects.create(role="user", content=text)
        ChatMessage.objects.create(role="bot", content=response)

        # return JsonResponse({"response": response})  # Return JSON response

    return render(request, 'Ai_Teacher.html', {'messages': messages})
def clear_chat_history(request):
    ChatMessage.objects.all().delete()  # Delete all ChatMessage objects
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
def request_callback(request):
    if request.method == 'POST':
        form = CallBackForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = CallBackForm()

    return render(request, 'contact.html', {'form': form})



# def download_csv(request):
#     if request.method == 'POST':
#         # Create the HttpResponse object with appropriate headers.
#         response = HttpResponse(content_type='text/csv')
#         response['Content-Disposition'] = f'attachment; filename="callbacks_{timezone.now().strftime("%Y-%m-%d")}.csv"'

#         writer = csv.writer(response)
#         # Write the header
#         writer.writerow(['Name', 'Email', 'Message', 'Created At'])

#         # Filter the records based on whether they have been exported
#         callbacks = CallBackRequest.objects.filter(exported=False)

#         for callback in callbacks:
#             writer.writerow([callback.name, callback.email, callback.message, callback.created_at])

#             # Mark the record as exported
#             callback.exported = True
#             callback.save(update_fields=['exported'])

#         return response
#     else:
#         # If the request is not a POST request, you can render a login page or any other page as needed.
#         return render(request, 'login.html')


def download_csv(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            # Authenticate the user
            user = form.get_user()
            login(request, user)
            # Create the HttpResponse object with appropriate headers.
            response = HttpResponse(content_type='text/csv')
            response['Content-Disposition'] = f'attachment; filename="callbacks_{timezone.now().strftime("%Y-%m-%d")}.csv"'

            writer = csv.writer(response)
            # Write the header
            writer.writerow(['Name', 'Email', 'Message', 'Contact No', 'Created At'])

            # Filter the records based on whether they have been exported
            callbacks = CallBackRequest.objects.filter(exported=False)

            for callback in callbacks:
                writer.writerow([callback.name, callback.email, callback.message, callback.mobile_no, callback.created_at])

                # Mark the record as exported
                callback.exported = True
                callback.save(update_fields=['exported'])

            return response
        
    else:
        form = AuthenticationForm()

    return render(request, 'login.html', {'form': form})


def trial(request):
    return render(request, 'trial.html')

def team_view(request):
    teams = Team.objects.all()
    return render(request, 'team.html', {'teams': teams})

# def add_member(request):
#     if request.method == "POST":
#         # Get the data from the request
#         image = request.FILES.get('image')
#         name = request.POST.get('name')
#         description = request.POST.get('description')

#         if image and name and description:
#             # Create a new Member instance and save it to the database
#             member = Members(image=image, name=name, description=description)
#             member.save()

#             return redirect('add-member')  # Redirect to a view that lists all members
#         else:
#             return HttpResponse("All fields are required")

#     return render(request, 'add-member.html')