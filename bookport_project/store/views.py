from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
import json
from django.http import JsonResponse


from .models import *


def index(request):
    # books = Book.objects.all()
    c = Grade.objects.all()

    return render(request, "store/store.html", {
        "categories": c
    })

def register(request):
    if request.method == 'GET':
        return render(request, "store/register.html")
    else:
        username = request.POST["username"]
        email = request.POST["email"]
        password = request.POST["password"]
        confirm_pass = request.POST["confirm"]

        if len(password) < 8:
            return render(request, "store/register.html",{
                          "passerror": "Password must be at least 8 character"
                          })
        if password != confirm_pass:
            return render(request, "store/register.html",{
                          "confirmerror": "confirmation does not match password"
                          })
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "store/register.html", {
                "usernameerror": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))

def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))

def login_view(request):
    if request.method == "GET":
        return render(request, "store/login.html")
    else:
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "store/login.html", {
                "message": "Invalid username and/or password."
            })

def book(request, id):
    if request.method == "GET":
        book = Book.objects.get(pk=id)

        return render(request, "store/book.html", {
            "book": book
        })

@login_required
@csrf_exempt
def cart(request):
    if request.method == "GET":
        try:
            cart3 = Cart.objects.get(user=request.user)
            cart3.update()
            # cart3.check_all()
            cart3.save()
            items = cart3.items.all()
        except:
            items = Cart.objects.create(user=request.user)
            items.save()
            return render(request, "store/cart.html", {
                "message": "Cart is empty"
            })
        else:

            return render(request, "store/cart.html", {
                "items": items,
                "total": cart3.total
            })
    else:
        data = json.loads(request.body)
        bookid = data.get("book")
        state = data.get("state")
        book1 = Book.objects.get(pk=bookid)


        try:
            cart1 = Cart.objects.get(user=request.user)
        except:
            cart1 = Cart.objects.create(user=request.user)


        try:
            quantity1 = Quantity.objects.get(user=request.user, book=book1)
        except:
            quantity1 = Quantity.objects.create(user=request.user, book=book1)
            quantity1.save()
            cart1.items.add(quantity1)
            cart1.update()
            cart1.save()
            return JsonResponse("sucess")
        else:
            if state == "minus":
                quantity1.quantity -= 1
                # quantity1.save()
                # x = quantity1.check()
                # cart1.update()
                # return JsonResponse("remove")
            else:
                quantity1.quantity += 1

            quantity1.save()
            x = quantity1.checkq()
            cart1.update()
            if x == 'remove':
                return JsonResponse({
                    "remove": "remove",
                    "total": cart1.total
                    })
            elif x == 'solved':
                quantity1.save()
                return JsonResponse({
                    "quantity" : quantity1.quantity,
                    "price": book1.stock * book1.price,
                    "error": 'there are not enought book in stock',
                    "total": cart1.total
                    })
            else:
                return JsonResponse({
                    "quantity" : quantity1.quantity,
                    "price": quantity1.quantity * book1.price,
                    "total": cart1.total
                    })


def checkout(request):
    if request.method == "GET":
        cart1 = Cart.objects.get(user=request.user)
        cart1.update()
        cart1.save()
        return render(request, "store/checkout.html", {
            "items": cart1.items.all(),
            "total": cart1.total
        })

def grade_url(request, grade):
    if request.method == "GET":
        # grades = Grade.objects.all()
        # g_name = []
        # for x in grades:
        #     g_name.append(x.grade)
        # # grades = ["first","second", "third", "other"]
        # if grade not in g_name:
        #     return HttpResponseRedirect(reverse("index"))
        # # grade = f"{grade} secondry"
        # g = Grade.objects.get(grade=grade)

        try:
            g = Grade.objects.get(grade=grade)
        except:
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "store/grade.html", {
                "books": g.books.all(),
                "grade": grade
            })
