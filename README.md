### Disclaimer: This is a dummy application and only intended to demonstrate coding and programming. 

# django-mycar
Mycar is an online marketplace for car shoppers and sellers. For the sake of simplicity, there is no user profile and authentication implemented.

# Objective & features:
* Mycar (http://127.0.0.1:8000/mycar/) home page where users can see all the listing, cars for sale page and sale your car     option to create new list. 
* A dynamic search engine which used optimized querysets “Q() object” to search car by make, model or keyword. If no match found, it will display a message "Sorry, you have entered an invalid search, please try again."
* Django messaging framework to display custom messages.
* Custom navbar to stay visible on scrolldown.
* Bootstarp carousel is being used to animate the welcome images.
* Scalable pagination which only display three or six post at a homepage. If number of post exceeds six, than it will show a navigation bar to go to next page.
* Custom "make/model" and "Type" dropdown option which display the number of make/model and type of vehicle available at real-time database synchronization.
* Search price range modal which is a dialog popup window that displayed on top of the current page with max and min price choices. Javascript is being used to disable the search button until both options are filled.
* Zoom out list images on hover with CSS.
* Key features modal dialog popup window displays key information for that particular post.
* Full detail page option for individual post.
* Jquery is being used to display related content when click on "Buying" or "Selling" buttons without refreshing the page.
* Select_related & Prefetch_related is being used to improve our queries performance.
* Populate options in create post form.
* Dynamic urls.
* Responsive design for any screen size.

# Javascript & JQuery animations.
* Ajax calls to populate results real-time without refreshing the page.
* Navbar stays at the top as we scroll down.
* Flashing effects for success & error messages.
* Disable submit buttons for blank submission.

# Steps to run:

### Step 1:
Create a folder.

$ mkdir django_mycar

Create a virtual enviroment.

$pip install virtualenv

$ cd django_mycar

$ virtualenv env

$ source env/bin/activate

### Step 2:
Install requirements.txt

$pip install -r requirements.txt

### Step 3:
Edit settings.py with database credentials.

<p align="center">
  <img src="screenshots/db_conn.png" width="600px" height="200px">
</p>

### Step 4:
Database migrations.

$ python manage.py makemigrations

$ python manage.py migrate

### Step 5:
Run project.

$ python manage.py runserver

### Car-listing table in database:
<p align="center">
  <img src="screenshots/db-car-listing.png" width="600px" height="200px">
</p>

### Category table in database:
<p align="center">
  <img src="screenshots/db-cat.png" width="600px" height="200px">
</p>

### Images table in database:
<p align="center">
  <img src="screenshots/db-img.png" width="600px" height="200px">
</p>

### Make table in database:
<p align="center">
  <img src="screenshots/db-make.png" width="600px" height="200px">
</p>

### Model table in database:
<p align="center">
  <img src="screenshots/db-model.png" width="600px" height="200px">
</p>

# -------------- Demo -------------
### Homepage:
<p align="center">
  <img src="screenshots/home.png" width="600px" height="400px">
</p>
<p align="center">
  <img src="screenshots/home-2.png" width="600px" height="400px">
</p>

### Responsive Navbar.
On scroll down, navbar will change its position and moves down along with the page.
<p align="center">
  <img src="screenshots/nav-bar-effect.jpg" width="600px" height="600px">
</p>

### Post image enlarge on hover.
<p align="center">
  <img src="screenshots/home-hover.jpg" width="600px" height="500px">
</p>

### Search bar & result.
<p align="center">
  <img src="screenshots/search-bar.png" width="600px" height="100px">
</p>

### Search Result.
<p align="center">
  <img src="screenshots/search-res.png" width="600px" height="300px">
</p>

### Make/Model dropdown.
<p align="center">
  <img src="screenshots/make-model-op.png" width="600px" height="200px">
</p>
Onclick any option, it will open the model box and real-time piece count. If you select any of them, will takes you to that particular model's detail page.
<p align="center">
  <img src="screenshots/model-detail-drop-click.png" width="600px" height="200px">
</p>

### Type dropdown.
This will show the number of car types available.
<p align="center">
  <img src="screenshots/type-op.png" width="600px" height="200px">
</p>

### Price option.
This will popup a price range modal which is a dialog popup window that displayed on top of the current page with max and min price choices. Javascript is being used to disable the search button until both options are filled.
<p align="center">
  <img src="screenshots/price-modal.png" width="600px" height="200px">
</p>

### Cars for sale button.
Cars for sale button will divert your another page where we can only see the current listing.
<p align="center">
  <img src="screenshots/car-for-sale-btn.png" width="600px" height="300px">
</p>

### List detail page.
<p align="center">
  <img src="screenshots/detail-page.jpg" width="600px" height="300px">
</p>

Image enlarge on hover.
<p align="center">
  <img src="screenshots/detail-page-hover.jpg" width="600px" height="200px">
</p>

### Finance section slide up and down.
<p align="center">
  <img src="screenshots/finace-up-down-eff.jpg" width="600px" height="300px">
</p>

### Buy and sale section.
Buying and selling section change without refreshing the page.
<p align="center">
  <img src="screenshots/buy-sell.jpg" width="600px" height="300px">
</p>

### Key features modal popup.
Key features button popup a model with related information of particular list.
<p align="center">
  <img src="screenshots/key-feature-model.png" width="600px" height="200px">
</p>

### Sale your car option.
This with open a create new post form.
<p align="center">
  <img src="screenshots/sale-form-1.png" width="600px" height="400px">
</p>

Category section populate available categories.
<p align="center">
  <img src="screenshots/sale-form-pop-cat-2.png" width="600px" height="200px">
</p>

Make section populate available makes.
<p align="center">
  <img src="screenshots/sale-form-pop-make-3.png" width="600px" height="200px">
</p>

Model section populate available model.
<p align="center">
  <img src="screenshots/sale-form-pop-model-4.png" width="600px" height="300px">
</p>

Years section populate available Years.
<p align="center">
  <img src="screenshots/sale-form-pop-years-6.png" width="600px" height="200px">
</p>

States section populate available states.
<p align="center">
  <img src="screenshots/sale-form-pop-state-7.png" width="600px" height="300px">
</p>

Select images will open up a search box to find and upload desired images.
<p align="center">
  <img src="screenshots/sale-form-sel-img-8.png" width="600px" height="300px">
</p>
