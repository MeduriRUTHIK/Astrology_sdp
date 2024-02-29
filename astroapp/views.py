from calendar import month

from django.contrib.auth.models import User
from django.db.models import Q

from .forms import FeedbackForm
from .models import registration, horoscopedb, zodiacdb, contactdb
from .models import contact
import random
from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth import login


def login(request):
    return render(request, 'login.html')


def register(request):
    if request.method == 'POST':
        rname = request.POST['username']
        gender = request.POST['gender']
        email = request.POST['email']
        mobile = request.POST['mobile']
        password = request.POST['password']

        # Check if a registration with the provided email already exists
        if registration.objects.filter(email=email).exists():
            msg = "Email already exists."
        else:
            registersave = registration(name=rname, gender=gender, email=email, mobile=mobile, password=password)
            registration.save(registersave)
            msg = "Registered Successfully!!"

        return render(request, 'register.html', {'msg': msg})
    else:
        return render(request, 'register.html')


def index(request):
    return render(request, 'index.html')


def aboutpage(request):
    return render(request, 'aboutpage.html')


def home(request):
    return render(request, 'home.html')


def logout():
    return redirect('home')


def checklogin(request):
    if request.method == 'POST':
        uname = request.POST['uname']
        upassword = request.POST['pwd']
        flag = registration.objects.filter(Q(name=uname) & Q(password=upassword))
        print(flag)
        if (flag):
            request.session['uname'] = uname
            message = "Login Success!!!"
            return render(request, 'index2.html', {'message': message, 'uname': uname})
        else:
            message = "Login Failed!!"
            return render(request, 'login.html', {'message': message})
    return render(request, 'login.html')


def zodiac(request):
    if request.method == 'POST':
        uname = request.session['uname']
        place = request.POST.get('place', '')
        month = request.POST.get('month', '')
        day = int(request.POST.get('day', 0))

        if month == 'december':
            astro_sign = 'Sagittarius' if day < 22 else 'Capricorn'
        elif month == 'january':
            astro_sign = 'Capricorn' if day < 20 else 'Aquarius'
        elif month == 'february':
            astro_sign = 'Aquarius' if day < 19 else 'Pisces'
        elif month == 'march':
            astro_sign = 'Pisces' if day < 21 else 'Aries'
        elif month == 'april':
            astro_sign = 'Aries' if day < 20 else 'Taurus'
        elif month == 'may':
            astro_sign = 'Gemini' if day < 21 else 'Gemini'
        elif month == 'june':
            astro_sign = 'Gemini' if day < 21 else 'Cancer'
        elif month == 'july':
            astro_sign = 'Cancer' if day < 23 else 'Leo'
        elif month == 'august':
            astro_sign = 'Leo' if day < 23 else 'Virgo'
        elif month == 'september':
            astro_sign = 'Virgo' if day < 23 else 'Libra'
        elif month == 'october':
            astro_sign = 'Libra' if day < 23 else 'Scorpio'
        elif month == 'november':
            astro_sign = 'Scorpio' if day < 22 else 'Sagittarius'
        else:
            astro_sign = 'Invalid Month'
        if astro_sign != 'Invalid Month':
            zodiacsign = astro_sign
            zodiacsave = zodiacdb(birth_month=month, birth_day=day, place_of_birth=place, astro_sign=zodiacsign)
            zodiacdb.save(zodiacsave)
        return render(request, 'zodiac.html', {'astro_sign': astro_sign, 'uname': uname})

    return render(request, 'zodiac.html')


# Dictionary of horoscopes for all 12 zodiac signs
horoscopes = {
    'Aries': "In the realm of the Ram, the stars tell of new beginnings. It's a time to seize opportunities with "
             "unwavering enthusiasm and boundless energy. Prepare for exciting changes on the horizon, and embrace "
             "them with open arms.",
    'Taurus': "As a Taurus, your financial sensibilities may come into play. You might face important decisions about "
              "money. Don't rush, take your time to evaluate your options. Trust in your practicality and sound "
              "judgment to make the right choice.",
    'Gemini': "Communication is your forte now. With your gift of gab, it's the perfect time to build and strengthen "
              "your relationships. Express yourself and connect with others on a deeper level. Your words hold great "
              "power.",
    'Cancer': "Your intuition is like a guiding light. Listen to your inner wisdom; it knows the way. Trust your gut "
              "instincts when making decisions, especially the big ones. You have a natural knack for knowing what's "
              "right for you.",
    'Leo': "The spotlight is yours, dear Leo. Your charisma is shining brightly, and you're captivating those around "
           "you. Use your magnetic charm to make a lasting impression and achieve your aspirations. This is your time "
           "to roar.",
    'Virgo': "Prioritize self-care and well-being. Balance your work life with personal life to optimize your health "
             "and happiness. A focus on detail and organization will lead to remarkable results.",
    'Libra': "It's all about harmony and balance in the world of the Scales. Seek compromise in your relationships to "
             "keep the peace. You're the diplomat of the zodiac, and your ability to find common ground will lead to "
             "smoother sailing.",
    'Scorpio': "Your intensity knows no bounds. Embrace your passionate nature, but use your energy wisely. Avoid "
               "unnecessary conflicts and focus on what truly matters. Your determination will take you far.",
    'Sagittarius': "Adventure calls to you, Sagittarius. It's a fantastic time to plan a thrilling trip or embark on "
                   "new experiences. Your sense of wonder and curiosity is your guide; follow it, and you'll be in "
                   "for an unforgettable journey.",
    'Capricorn': "The Goat signifies discipline and focus. Set clear, achievable goals, and then work diligently to "
                 "attain them. Your unwavering commitment to your ambitions will pave the path to success.",
    'Aquarius': "Your inventive mind is in overdrive. Use your creative genius to solve problems and make progress. "
                "Think outside the box, and let your uniqueness shine through. Your unconventional ideas may just "
                "change the world.",
    'Pisces': "Dive deep into your inner world, Pisces. Trust your intuition and connect with your spiritual side. "
              "It's a time for reflection, meditation, and inner growth. Your empathy and sensitivity will guide you "
              "on a profound journey within."
}


def calculate_zodiac_sign(month, day):
    if month == 'march' and 21 <= day <= 31 or month == 'april' and 1 <= day <= 19:
        return 'Aries'
    elif month == 'april' and 20 <= day <= 30 or month == 'may' and 1 <= day <= 20:
        return 'Gemini'
    elif month == 'may' and 21 <= day <= 31 or month == 'june' and 1 <= day <= 20:
        return 'Gemini'
    elif month == 'june' and 21 <= day <= 30 or month == 'july' and 1 <= day <= 22:
        return 'Cancer'
    elif month == 'july' and 23 <= day <= 31 or month == 'august' and 1 <= day <= 22:
        return 'Leo'
    elif month == 'august' and 23 <= day <= 31 or month == 'september' and 1 <= day <= 22:
        return 'Virgo'
    elif month == 'september' and 23 <= day <= 30 or month == 'october' and 1 <= day <= 22:
        return 'Libra'
    elif month == 'october' and 23 <= day <= 31 or month == 'november' and 1 <= day <= 21:
        return 'Scorpio'
    elif month == 'november' and 22 <= day <= 30 or month == 'december' and 1 <= day <= 21:
        return 'Sagittarius'
    elif month == 'december' and 22 <= day <= 31 or month == 'january' and 1 <= day <= 19:
        return 'Capricorn'
    elif month == 'january' and 20 <= day <= 31 or month == 'february' and 1 <= day <= 18:
        return 'Aquarius'
    else:
        return 'Pisces'


def horoscope(request):
    uname = request.session['uname']
    horoscope = None
    if request.method == 'POST':
        month = request.POST.get('month', '').lower()
        day = int(request.POST.get('day', 0))

        if month and day:
            astro_sign = calculate_zodiac_sign(month, day)
            horoscope = horoscopes.get(astro_sign)
            horoscopic = horoscopedb(month=month, day=day, horoscope=horoscope)
            horoscopedb.save(horoscopic)
    return render(request, 'horoscope.html', {'horoscope': horoscope, 'uname': uname})


def feedback(request):
    auname = request.session["uname"]
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('feedback')

    form = FeedbackForm()
    return render(request, 'feedback.html', {'form': form, 'uname': auname})


def changepassword(request):
    auname = request.session["uname"]
    return render(request, 'changepassword.html', {'uname': auname})


def updatepwd(request):
    opwd = request.POST['opwd']
    npwd = request.POST['npwd']
    print(opwd, npwd)

    flag = registration.objects.filter(Q(password=opwd))

    if flag:
        registration.objects.filter(password=opwd).update(password=npwd)
        msg = "Password Updated Sucessfully"
    else:
        msg = "Old password is incorrect"

    return render(request, 'changepassword.html', {"message": msg})


def contact(request):
    if request.method == 'POST':
        firstname = request.POST.get('first_name')
        lastname = request.POST.get('last_name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        contactdetails = contactdb(firstname=firstname, lastname=lastname, email=email, message=message)
        contactdb.save(contactdetails)

    return render(request, 'contactpage.html')


def help(request):
    uname = request.session["uname"]
    return render(request, 'help.html', {'uname': uname})
