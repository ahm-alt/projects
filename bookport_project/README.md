## HarvardX CS50W: Web Programming with Python and JavaScript



### Distinctiveness and Complexity

- my project is an e-commerce website for selling books called bookport
- it's very different from project 2 :
      it has a very unique design and style
      it contains cart, checkout, categories
      it database is complex and big
      a completely new HTML and CSS
- it's mobile responsive
- it contains 5 models
- it contains two js files cart and index and 8 HTML templates



### Demonstration on youtube
[My Final Project presentation](https://youtu.be/9E0JQW0ZLmo)



### What’s contained in each file you created

#### in urls.py
- `""` (name="index") - Maps to the `index` view and displays all books in the store.
- `"register"` (name="register") - Maps to the `register` view and displays a form for user registration.
- `"logout"` (name="logout") - Maps to the `logout_view` view and logs the user out.
- `"login"` (name="login") - Maps to the `login_view` view and displays a form for user login.
- `"book/<int:id>"` (name="book") - Maps to the `book` view and displays the details for a single book with the specified `id`.
- `"cart"` (name="cart") - Maps to the `cart` view and displays the user's shopping cart.
- `"checkout"` (name="checkout") - Maps to the `checkout` view and displays a form for checkout.


#### in views.py it contains 7 functions :
1. `index(request)` - Displays all books in the store.
2. `register(request)` - Registers a new user or displays an error message.
3. `logout_view(request)` - Logs out the user.
4. `login_view(request)` - Logs in the user or displays an error message.
5. `book(request, id)` - Displays a single book's details.
6. `cart(request)` - Manages the user's shopping cart and dynamically updates it.
7. `checkout(request)` - Handles the checkout process and calculates the total price.



#### in models.py contains 4 models:
1. `User` - Extends Django's built-in `User` model and has no additional fields.
2. `Book` - Defines fields for a book object, including title, author, description, price, stock, category, grade, image, and svg.
3. `Quantity` - Represents the quantity of a specific book in a user's shopping cart and has fields for the user, book, and quantity.
4. `Cart` - Represents a user's shopping cart and has fields for the user, items (a many-to-many relationship with Quantity), and total price.
5. `Order`represent order information

### in templates
layout.html(the main file)
login.html login to enter site
register.html register to enter site
cart.html it shows the cart
checkout.html it shows the checkout
store.html display main page
grade.html it display categories


### static contains :
bootstrap library
icons
sweetalert library
style.css
cart.js and index.js

### media contains images of products


### Installation
  - Install project dependencies by running `pip install -r requirements.txt`. Dependencies include Django
  - Make and apply migrations by running `python manage.py makemigrations` and `python manage.py migrate`.
  - Create superuser with `python manage.py createsuperuser`. This step is optional.
  - Go to website address and register an account.











