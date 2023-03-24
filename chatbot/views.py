from django.shortcuts import render
from .models import Chat
from .chatgpt import get_bot_response
from django.http import JsonResponse

def index(request):
    if request.method == 'POST':
        user_input = request.POST['user_input']
        bot_response = get_bot_response(user_input)
        context = {'user_input': user_input, 'bot_response': bot_response}
        print(context)
        #return render(request, 'chatbot/index.html', context)
        return JsonResponse(context)
    else:
        return render(request, 'chatbot/index.html')