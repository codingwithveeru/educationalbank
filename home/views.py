from django.shortcuts import redirect, render
import google.generativeai as genai
from django.conf import settings
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json


from django.contrib import messages
from django.core.mail import send_mail

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.shortcuts import render, redirect
from django.contrib import messages


from django.contrib import messages

from django.contrib.auth import logout
from django.shortcuts import redirect

def user_logout(request):
    logout(request)
    return redirect('home')

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Auto login after register
            messages.success(request, 'Account ban gaya! Welcome 🎉')
            return redirect('home')
    else:
        form = UserCreationForm()
    
    return render(request, 'register.html', {'form': form})

# Gemini configure kar
genai.configure(api_key=settings.GEMINI_API_KEY)

def practice(request):
    context = {
        'total_mock_tests': 156,
        'total_orals': 89,
        'total_written': 234,
        'students_attempted': 8540,
    }
    return render(request, 'practice.html', context)

# Naya view - AI Doubt Solver
@csrf_exempt
def ask_gemini(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        question = data.get('question', '')
        
        try:
            model = genai.GenerativeModel('gemini-1.5-flash')  # Ya gemini-1.5-pro
            response = model.generate_content(f"""
            Tu ek helpful Indian teacher hai. Student ka doubt solve kar Hinglish me.
            Simple bhasha me samjha, example de.
            
            Student ka sawal: {question}
            """)
            
            return JsonResponse({
                'success': True,
                'answer': response.text
            })
        except Exception as e:
            return JsonResponse({
                'success': False,
                'error': str(e)
            })
    
    return JsonResponse({'success': False, 'error': 'Only POST allowed'})

def home(request):
    
    return render(request, "index.html")
def home(request):
    courses = [
        {
            'name': 'Python', 'icon': 'fab fa-python', 'desc': 'Web dev, AI/ML, Automation sab kuch',
            'lessons': 40, 'hours': 12, 'slug': 'python', 'color': 'python'
        },
        {
            'name': 'Java', 'icon': 'fab fa-java', 'desc': 'Android, Backend, DSA mastery',
            'lessons': 50, 'hours': 15, 'slug': 'java', 'color': 'java'
        },
        {
            'name': 'HTML + CSS', 'icon': 'fab fa-html5', 'desc': 'Web design ki pehli seedhi',
            'lessons': 25, 'hours': 8, 'slug': 'html', 'color': 'html'
        },
        {
            'name': 'C Language', 'icon': 'fas fa-code', 'desc': 'Programming ki foundation',
            'lessons': 35, 'hours': 10, 'slug': 'c', 'color': 'c'
        },
    ]
    return render(request, 'index.html', {'courses': courses})

def courses(request):
    return render(request, 'includes/courses.html')  # includes/ add kiya

def notes(request):
    return render(request, 'notes.html')

def dashboard(request):
    context = {
        'total_courses': 42,
        'free_courses': 28,
        'paid_courses': 14,
        'students_registered': 12450,
    }
    return render(request, 'dashboard.html', context)
def practice(request):
    context = {
        'total_mock_tests': 156,
        'total_orals': 89,
        'total_written': 234,
        'students_attempted': 8540,
    }
    return render(request, 'practice.html', context)

def ai_doubt(request):
    context = {
        'total_questions': 5420,
        'answered_today': 234,
    }
    return render(request, 'ai_doubt.html', context)



def certificate_demo(request):  # ← 'g' hata de
    context = {'student_name': 'Raftaar'}  # Default naam
    
    if request.method == 'POST':
        student_name = request.POST.get('student_name')
        print(student_name)  # Terminal me check ke liye
        context['student_name'] = student_name
    
    # GET request pe bhi certificate_demo.html render karna hai
    return render(request, 'certificate_demo.html', context)

from .models import ContactMessage
from django.contrib import messages

def contact(request):
    if request.method == 'POST':
        ContactMessage.objects.create(
            name=request.POST.get('name'),
            email=request.POST.get('email'),
            subject=request.POST.get('subject'),
            message=request.POST.get('message')
        )
        messages.success(request, 'Message bhej diya! Jaldi reply karenge')
        return redirect('contact')
    
    return render(request, 'contact.html')