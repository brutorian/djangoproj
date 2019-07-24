# Unicorn Attractor Website
 
## Overview
 
### What is this website for?
This a site to showcase the an app and the features it'll receive in any upcoming updates. 

### What does it do?
The site allows users to learn about unicorn attractor and what is upcoming in updates. The site allows the user to interact with various parts of it such as creating a login, completing questions, looking at blogs and filling out a contact form. 
The site also allows users to make single payments to the site in the form of donation which allow the developers to continue to create updates for free.

### How does it work
The site works by allowing users access to all of the features the site has, but in some areas it does require the user to login. This way it encourages the user to make an account with the site to access these parts of it.
Once unlocked the user can access the polls, payment and blog detail, but if they don't login they can only view the information pages until they're signed up. 
The other features are meant to allow the user to interact with the site such as polls and the contact form all the while show casing unicode.

This has:
• Polls
• Blogs
• Comment section 
• Contact form
• Stripe payment
• Login/Signup/Logout
• Info pages

## Features
 
### Existing Features
• Navbar allowing user to navigate round the site
• D3 graphs showing data about the business

### New Features
• Various information pages such as an index, about and support page.
• New media image in the blog detail.
• Django registration form, allowing users to create an account on the site, which redirected to the login page.
• Django login form, allowing users to log into the account they created in the registration form. Once logged in they're redirected to the home page.
• Logout function to let user logout once logged in if they decide to.
• A Stripe payment system allowing user to make donations to the site for £19.99.
• Blog app which documents the new upcoming features for the product, which the users can look at.
• Poll app to allow the users to vote on what they like the look of then look at the results of each one.
• Login required, meaning users will have to login to view or use certain pages.
• Contact form submits the users content and name returning a confirmation message if and once it has been submitted by the user.#
• Stripe payment is a single form of payment which allows the user to make a one off donation to the site of just £19.99. The successful payment returns a confirmation page of the payment if successful.


### Features Left to Implement
• Move the comment section to the main blog_detail page instead of having to go to another page to make it.
• Add replies to the comments made in the blog details page. 
• Hide the login and signup page when user is already logged in.

## Tech Used

### Some the tech used includes:
• HTML (Hyper Text Markup Language)
• CSS (Cascading style sheets)
• Javascript (programming language)
• d3 (JavaScript library for interpreting data)
• Python (programming language)
• Django (An open-source python web framework )
• Jinja (A template engine)
• Stripe (A payment processing platform)
• Pycharm (A code editor recommended by the course)
• Sublime (A code editor recommended by the course)

## Testing
All test were carried manually to ensure all components of the site worked.

Login/Signup/Logout:
1. Once app created went to signup page, if it worked the page would be redirected to homepage as logged in, if it failed it would remain on signup page.
2. If I had successfully made the signup then user should be automatically logged in. When logging in on login page and is correct user should be directed home.
3. Once logged in should be redirected to homepage where the users details are present in the top corner.
4. Logout is also present in the top and once it was clicked, user should be logged out.
5. Once logged out should see the option to login back up in the corner where clicked redirects back to login page.

Blog:
1.Went into admin in the search bar at top of the page like this (http://127.0.0.1:8000/admin/)
2. Once in admin went into blogs tab where the option was given to make a blog post which included:
   •title
   •slug for unique url names
   •main text
3.Made the blog post in the admin, which should've appeared in the blog app which it did but if it did'nt then blog app would've remained empty, then click on the blog title which should open the blog detail page. 
4. Comments when created should appear on the blog detail page if not it should remain on the comment page.

Poll:
1.Just like blog go into the admin in the search bar at top of the page like this (http://127.0.0.1:8000/admin/)
2. Once in admin to the polls tab, should appear with two choices, one being Questions and the other being Choices. Once clicked on Questions make a question.
3. Then head into the Choices to create the choice answers for that question.
4. The user should then see in the polls app a list of questions in order of recent upload, when they click on the title it should redirect them to the polls detail page with the option answers on it.
5. If the user tries to submit the page without choosing an option then it should tell them to pick an option.
6. Once an option is picked and submitted then the user is redirected to the results page of that question., but also has the option to go and vote on another question at the bottom.
7. If no polls are made then the page should say indicate there are'nt any yet.

Payment/Stripe:
1.Went into the support page and clicked the donate button at the bottom of the page.
2.Once clicked page is redirected to the card payment, once card payment is filled the page should redirect to the success page indicating the successful payment.
3.Once payment completed, the stripe dashboard showed the money was added to the account.
4. If payment fails payment page will indicate so, also indicating if user has missed any details or given the wrong information with errorElement appearing on screen.

Contact:
1.Once on contact page fill out the form, which if completed correctly should lead to confirmation page.
2.If information has been missed such the content box then form should indicate so.

Navbar:
1.Click on the hamburger icon, this leads to nav bar sliding out to reveal the links to all the pages.
2.Once a link to a page is clicked it'll redirect to that page.
3.If it does'nt redirect then page has'nt been linked it correctly.


## Contributing
 
### Getting the code up and running
Get code running:
Pycharm/Sublime:
1.Enter into the terminal and enter "python manage.py runserver",
2. Open the link in the terminal and you'll be directed to the page.

Github:
Follow the github deployment process also you can see it here(https://github.com/brutorian/djangoproj).

Heroku:
Follow the heroku deployment process also you can see it here(https://djangounit.herokuapp.com/).

### Deployment
Github:
1. First, you will need to clone the repository by running the "git clone "" "command
2. Copy the files from the original folder into the new github one.
3. Once files added go to the terminal and run "git add ." .
4. As soon as it has finished compiling the files, then run in terminal "git commit -m "first push"".
5. Then Finally type in the terminal "git push origin master"
6. Go to your github repository and see it's all there.

Heroku:
1. Create a heroku account and log in, to log in you'll be required to type in "heroku login" in your terminal. Once the login has been verified you'll be logged in.
2. Go to the heroku dashboard, click on create new app, give it a name, select eu region then click create app from there you can also connect your github repository.
3. Add postgresql to the add on link in the resources tab
4. Go to settings and comment out the sqlite database like so:
"""DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}"""

then replace it the postgres one like so:
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'postgres.name',
        'USER': 'postgres.user',
        'PASSWORD': 'postgres.password',
        'HOST': 'postgres.host',
        'PORT': 'postgres.port',
    }
}
This'll link your database up to the postgres one. 
6. pip install django-heroku, this'll allow you to connect your django to the heroku app, which also in my case installed whitenoise==4.1.2 which is a simplified static file.
7. Go to settings.py add import django_heroku to the top of the page and django_heroku.settings(locals()) to the bottom.
8. Within the Procfile add release: python manage.py migrate to migrate the local db to the app and web: gunicorn Project3.wsgi to get the app running.
9. Go to deploy and connect github account, select the repository and click deploy. Wait for it upload the files and then your site should be up and running.
10. Once it's up and running you can also create a superuser allowing you to make more blog posts or other things to the site.
11. Also add all media files if you have them to the Amazon AWS S3 site to ensure all media is shown on django as django won't show them otherwise.



## Credits

### Media
The photos used in this site were obtained from :
• Google Images
• image (https://steemit.com/steemit/@tochai/learning-to-code-for-free)


### Information
The information used to create this site was from a number of sources
    • Django blog (https://stackoverflow.com/questions/6370659/django-blog-apps?rq=1
    • Django blog (https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/django_assessment_blog)
    • Django blog (https://codereview.stackexchange.com/questions/162366/django-blog-application-views-urls-models-forms)
    • Django Blog (https://www.youtube.com/watch?v=lgqaMJNHSLk),
    • Django Blog (https://scotch.io/@CleverProgrammer/how-to-make-a-django-blog-app),
    • Django Blog (https://buttercms.com/django-blog-engine/),
    • Django Signup/Login(https://wsvincent.com/django-user-authentication-tutorial-signup/),
    • Django Signup/Login(https://docs.djangoproject.com/en/2.1/topics/auth/default/),
    • Online Shop(https://www.youtube.com/watch?v=jZ3DhppbUnM),
    • Online Shop(https://django-shop.readthedocs.io/en/latest/tutorial/intro.html),
    • Online Shop(https://www.youtube.com/watch?v=vccUP3jdpBg&t=246s),
    • Jinja(https://docs.djangoproject.com/en/2.1/topics/templates/),
    • CSS bar-chart(https://speckyboy.com/code-snippets-css3-bar-graphs/),
    • Stripe payment(https://stripe.com/docs/stripe-js),
    • Stripe payment (https://www.youtube.com/watch?v=9Wbfk16jEOk&list=LLl9momzsEset1SYpMVdnycA&index=2&t=11672s),
    • Stripe payment (https://www.youtube.com/watch?v=zu2PBUHMEew&t=1231s),
    • Stripe payment (https://testdriven.io/blog/django-stripe-tutorial/),
    • Url slug (https://www.codingforentrepreneurs.com/blog/common-regular-expressions-for-django-urls/),
    • Github (https://www.youtube.com/watch?v=iyFjdmzcpws&list=LLl9momzsEset1SYpMVdnycA&index=5&t=0s),
    • Heroku (https://www.youtube.com/watch?v=6DI_7Zja8Zc&t=2848s),
    • Heroku (https://www.youtube.com/watch?v=MoX36izzEWY),
    • Polls (https://docs.djangoproject.com/en/2.2/intro/tutorial01/),
    • Polls (https://www.youtube.com/watch?v=8XqvqTAbYEQ),
    • Polls (https://stackoverflow.com/questions/2811075/model-django-poll),
    • urls (https://docs.djangoproject.com/en/2.2/topics/http/urls/),
    • upload heroku (https://stackoverflow.com/questions/48128419/heroku-django-app-not-loading-static-files-404-not-found),
    • upload heroku (https://www.youtube.com/watch?v=6DI_7Zja8Zc),
    • upload heroku (https://stackoverflow.com/questions/30413294/css-is-not-showing-on-heroku-django-app),
    • upload heroku (https://stackoverflow.com/questions/53691783/deploying-a-django-project-through-git-to-heroku-no-module-named-failure),
    • upload heroku (https://www.youtube.com/watch?v=DAYgBmXBqIk),
    • url (https://stackoverflow.com/questions/43139081/importerror-no-module-named-django-core-urlresolvers),
    • Django official site documentation (https://docs.djangoproject.com/en/2.2/),
    • heroku superuser (https://stackoverflow.com/questions/22081556/heroku-django-app-createsuperuser),
    • logout(https://stackoverflow.com/questions/21837422/login-page-displayed-even-if-the-user-is-already-logged-in), 
    • logout(https://stackoverflow.com/questions/55062157/how-to-prevent-user-to-access-login-page-in-django-when-already-logged-in),
    • accounts(https://docs.djangoproject.com/en/2.2/topics/auth/default/),
    • blog comments(https://docs.djangoproject.com/en/1.7/ref/contrib/comments/),
    • blog comments(https://www.youtube.com/watch?v=zgF-KtQPqxQ),
    • logout(https://overiq.com/django-1-10/django-logging-users-in-and-out/),
    •Code Institute Course
