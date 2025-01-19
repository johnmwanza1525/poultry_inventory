# Chirpy Chooks

This a Django based (fictional!) e-commerce application which is the last of 5 required [Code Institute](https://codeinstitute.net/ie/) portfolio projects.

Chirpy Chooks is the online store of a small business based in the West of Ireland, specialising in live poultry. The store offers a variety of laying hens, broiler chickens and laying ducks. Currently the business offers in-store collection of orders only with a limited range of hoome delivery planned for the future.
On their site, Chirpy Chooks also host a forum about all things poultry. Articles published by the business itself are posted on a regular basis, offering helpful advice about poultry keeping, interesting facts about different breeds or the latest recommendations on feeds, bedding, pest control, etc.

![responsive mockup](/media/readme/mockup.png)

[Link to live site](https://chirpy-chooks.herokuapp.com/) 

## Table of Contents

- [UI/UX](#uiux)
    - [Agile](#agile)
    - [Wireframes](#wireframes)
    - [Site Goals](#site-goals)
    - [5 Planes of UX](#5-planes-of-ux)
    - [Visual Design Choices](#visual-design-choices)

- [SEO and Marketing](#seo-and-marketing)

- [Features](#features)
    - [Existing Features](#existing-features)
    - [Future Features](#possible-future-features)

- [Database Design](#database-design)
    - [Database Model](#database-model)
    - [Custom Model](#custom-model)
    - [CRUD](#crud)

- [Technologies Used](#technologies-used)
    - [Work Environments and Hosting](#work-environments-and-hosting)
    - [Python Libraries](#python-libraries)
    - [Django Libraries](#django-libraries)
    - [Payment processing](#payment-processing)
    - [Emails/Newsletter](#emailsnewsletter)
    - [SEO/Marketing](#seomarketing)

- [Testing](#testing)
    - [Test Guide](#test-guide)
    - [Validator Testing](#validator-testing)
    - [Browser Testing](#browser-testing)
    - [Fixed Bugs](#fixed-bugs)
    - [Unfixed Bugs](#unfixed-bugs)

- [Deployment](#deployment)

- [Development](#development)
    - [Fork](#fork)
    - [Clone](#clone)
    - [Download ZIP](#download-as-zip)

- [Source Credits](#source-credits)
    - [References/Documentation/Tutorials](#referencesdocumentationtutorials)
    - [Media and Styling](#media-and-styling)
    - [Content/Data](#contentdata)


## UI/UX

The overall design of the site follows a simplistic, earthy style. This reflects the product and their usage themselves, as well as the kind of lifestyle potential customers would potentially aspire to. 

As this business is not dealing in novelty products but livestock, flashy website features are currently not implemented. This is down to the fact that most expected customers will be based in rural Ireland where internet connection is often very limited. Therefore the site should not be bloated with features that serve no purpose other than being showy.

### Agile

This project was designed and built using the agile approach. Right from the initial planning through to final development. To help visualise the process I created a [GitHub project](https://github.com/users/Kathrin-ddggxh/projects/8) and utilised the provided Kanban board method to split project elements into user stories and manageable tasks.

To view all user stories including their required acceptance criterias and tasks, refer to the project linked to above.
Each story also has been tagged with a label to signify how crucial a particular feature is to the overall workings and acceptability of the site.

### Wireframes

The initial [wireframes in Figma](https://www.figma.com/file/nwqbwNDvflu8tDjm4krxMq/Chirpy-Chooks?node-id=0%3A1&t=hiKzdsdeGZce4shs-1) are an overly simplified version of the finished product and merely served the purpose of listing most of the site's essential features.

Not all features and functions are covered by these first drafts. For a full list of existing features see [Features](#features)

<details>
    <summary>
        Wireframe images
    </summary>
    <img src="media/readme/wireframes/homepage.png" alt="home-wireframe">
    <img src="media/readme/wireframes/login.png" alt="login-wireframe">
    <img src="media/readme/wireframes/signup.png" alt="signup-wireframe">
    <img src="media/readme/wireframes/contact.png" alt="contact-wireframe">
    <img src="media/readme/wireframes/profile.png" alt="profile-wireframe">
    <img src="media/readme/wireframes/products.png" alt="products-wireframe">
    <img src="media/readme/wireframes/product-detail.png" alt="product-detail-wireframe">
    <img src="media/readme/wireframes/basket.png" alt="basket-wireframe">
    <img src="media/readme/wireframes/checkout.png" alt="checkout-wireframe">
    <img src="media/readme/wireframes/forum.png" alt="forum-wireframe">
    <img src="media/readme/wireframes/forum-entry.png" alt="forum-entry-wireframe">
</details>

### Site Goals

This site is the online shop of the fictional supplier of live poultry "Chirpy Chooks". This business is based in county Clare, Ireland and is aiming to cover a customer base in the whole mid-western region of Ireland. Mainly counties Limerick, Clare and Galway.

On the site, customers can view different types of poultry the business breeds and offers. Poultry can be ordered and paid for via an intuitive, straight forward process. As the products are livestock, this business can not offer shipping. The customers are informed that orders must be collected from the business farm.

"Chirpy Chooks" is very keen as a business to provide past and future customers with useful advise and support about poultry keeping. As well as general contact details, the shop's site also features a forum maintained by the business itself, where all visitors of the site can find helpful articles on various subjects related to poultry keeping.

### 5 Planes of UX

#### Strategy

Addresses user's needs and product objectives.
The user here has been identified as a person residing in the mid-western region of Ireland who is interested in or already is keeping poultry.
Their needs are therefore a selection of different types of poultry (with different purposes), an easy way of making a selection from those and a simple payment method along with the selection process. 
Outside of the purchasing needs, the user might also require advise and information on the products offered by the business. This is addressed in the site's forum page.

*Site owner user:*

The owner of the site (or business employee) wants to be able to maintain the site without effort and via an appealing UI.

#### Scope

Addresses what functions and features are within the scope of the project.
Basic and essential e-commerce functionality was key to this project. This means that most features included are a basic requirement. Features like user sign up and login, user profile creation, checkout functionality and secure online payment had to be implemented, as well as basic CRUD funtionality for authorised users. For detailed explanation of all existing features see [Existing Features](#existing-features).
Features discussed under [Future Features](#possible-future-features), while still within the possible scope of this project, were deemed unnecessary at this point in time.

*Site owner user:*

To meet the site owners basic needs, each product can be easily updated or deleted via the front-end interface. New products can also be added via the front-end. Forum posts are handled the same way. All these features are only accessible to authorised users.

#### Structure

Defines how users can navigate the site and utilise all existing features.
The structure of the site is modelled on a basic e-commerce application with an additional forum page.
The structure allows users to browse products and make purchases as well as visit the forum to find information about poultry. Authenticated users can store their personal information in a user profile for the purpose of faster order handling.

*Site owner user:*

All CRUD functionality is placed intuitively with the relevant features of the site (individual products, forum posts). A super-user can avail of the same navigation options as as any authenticated users. However, these include additional features limited to authorised users.

#### Skeleton

Puts features defined in structure into navigational elements.
For a first outline of the project skeleton see [Wireframes](#wireframes).
To guarantee intuitive navigation of the site, both the navbar and the main content follow a standard layout pattern that should be familiar to most users.
The navbar provides links to the main features and functions of the site, varying based on whether a user is authenticated or not. On small to medium screen sizes a drop-down burger menu takes the place of the full navbar. A second-option home button is in place as a small logo, opposite all other nav links. According to research, this is also common practice.
The shopping basket link in the navbar is being updated everytime a user adds an item (of a differnt type!) to the basket.
Products and categories, as well as forum posts are listed in a card-style display.
All forms are cleary labelled an inform the user of invalid fields. User feedback is represented throughout the whole site via alert pop-ups.
Buttons and links are appropriately named.
A footer with social media links (currently merely serve as placeholders) completes the "framing" effect of the site.

#### Surface

Addresses visual design and how to convey desired emotions and achieve desired effects.
For more detail on the planning of the surface plane, see [Visual Design Choices](#visual-design-choices).


### Visual Design Choices

**Colour Scheme:**

The site utilises one accent colour (``primary-color: #FED049``) and a slightly darker gradient of the same colour (``primary-color-dark: #ffbf00``) for the purpose of focusing in on elements. The colour was chosen for its warm, earthy quality, somewhat reminiscent of egg yolk. It also offer high enough colour contrast when used with a font colour of black and is therefore in keeping with accessibility standards.

![primary colour](media/readme/primary-colour.png)

![primary colour dark](media/readme/primary-colour-dark.png)

**Fonts:**

One extravagant font ("Pacifico") was chosen solely for the shops logo and can be found throughout the site where name branding is used.
The main font ("Varela Round") combines ease or readability with friendly appearance. 
For full despcription of font names and their sources see [Media and Styling](#media-and-styling)

**Images and Icons:**

All images of this site are purely related to the products offered in the store or relevant to the individual forum post. Apart from the banner image on the home page, the site refrains from using too many decorative elements.
Icons used for the purpose of navigation are standards symbols which should be familiar to most users.
For full despcription of all images and their sources see [Media and Styling](#media-and-styling).


## SEO and Marketing

For an extensive overview of the marketing research for this project, please refer to this [SEO and Marketing documentation](MARKETING.md)


## Features

### Existing Features

#### Global and Home

**Navigation**

- Responsive navbar with burger dropdown menu
- Shop logo as default home link
- Navigation options dependant of user authentication/authorisation

![navbar desktop](/media/readme/features/nav.png)
![navbar mobile](/media/readme/features/nav-mobile.png)


**Footer**

- Footer element with social media links
- Contains link to privacy policy
- Newsletter sign up option

![footer desktop](/media/readme/features/footer.png)
![footer mobile](/media/readme/features/footer-mobile.png)

**Home page**

- Home page with banner image and introduction
- Shop Now button ("Buy Live Poultry")

![home page](/media/readme/features/home.png)

**About page**

- General info about store operations and pick-up
- Contact info incl. address, phone number and email
- Shop opening hours

![about page](/media/readme/features/about.png)

**Privacy policy**

- Standard GDPR compliant privacy policy page 
- Linked to in footer

![privacy policy](/media/readme/features/privacy.png)

Image does not contain entire policy document. Visit site to view full policy.

**404 Error page**

- Customised 404 error page with comic chicken and witty message
- Informs user of invalid URL
- Back button redirects user back to home page

![404 page](/media/readme/features/404.png)

**User feedback**

- Alert messages inform user of:

    - Actions about to be performed
    - Actions successfully completed
    - Actions failed to complete


#### Authentication

**Sign Up**

- Allows new users to create account
- Sign up process includes confirmation email with confirmation link

![sign up](/media/readme/features/signup.png)

![confirm email](/media/readme/features/confirm-email.png)

**Login**

- Allows existing users to log into their account
- Includes Remember me checkbox and Forgot Password option

![login](/media/readme/features/login.png)

**Logout**

- Allows authenticated users to securely log out of their account

![logout](/media/readme/features/logout.png)

#### Products

**All Products page**

- Lists all categories of products
- Links to forum and contact info

![categories](/media/readme/features/categories.png)

**Products page (of same category)**

- Lists all products of the same category
- Quick link to All Products page

![products](/media/readme/features/products-layers.png)

**Product details page**

- Product image, description and price
- Quick link to respective category
- Quantity input
- Continue Shopping button ("Browse more")
- Add to basket button
- Edit and delete option for authorised users for each product

![product details](/media/readme/features/products-details.png)

**Add Product page**

- Authorised admin users only!
- Complete product form with image upload option
- Cancel button
- Add product button to add product to database

![add product](/media/readme/features/add-product.png)

**Edit Product page**

- Authorised admin users only!
- Complete product form with image upload option
- Form is pre-populated with existing product's details
- Cancel button
- Update product button to update existing product in database

![edit product](/media/readme/features/edit-product.png)

**Delete Product option**

- Authorised admin users only!
- Option on product details page
- Request for user confirmation before deleting product
- Cancel button
- Delete button to delete existing product from database

![delete product](/media/readme/features/delete-product.png)


#### Forum

**Forum page**

- Lists all forum entries in tile format
- Tiles show title, excerpt, image, create-date and category
- Category button filters all entries by respective category (see below)

![forum page](/media/readme/features/forum.png)

**Filter option**

- Category tag in each entry tile acts as filter button
- When clicked, Clear Filter button is displayed above fitler result

![filter option](/media/readme/features/filter.png)

**Entry detail**

- Shows complete content of forum post
- Edit and delete option for authorised users for each entry

![forum entry](/media/readme/features/forum-entry.png)

**Add Entry**

- Authorised admin users only!
- Complete forum entry form with image upload option
- Cancel button
- Add entry button to add entry to database

![add entry](/media/readme/features/add-entry.png)

**Edit Entry page**

- Authorised admin users only!
- Complete forum entry form with image upload option
- Form is pre-populated with existing entry's details
- Cancel button
- Update entry button to update existing entry in database

![edit entry](/media/readme/features/edit-entry.png)

**Delete Entry option**

- Authorised admin users only!
- Option on forum entry page
- Request for user confirmation before deleting entry
- Cancel button
- Delete button to delete existing entry from database

![delete product](/media/readme/features/delete-entry.png)

**Response form and display**

- Post response: authenticated users only!
- Response form under entry content
- All submitted responses need admin approval (user alert after form submit about wait for approval)
- Approved responses listed below response form, including author, post-date and content

![forum responses](/media/readme/features/forum-response.png)


#### Shopping Basket

**Basket items in nav**

- Live update of basket status in navbar
- Counter in nav element displays only the number of different products, not the total of all products. The reason for this is, that in case of live poultry customers are quite likely to order larger numbers of each product (example: 50 Blackrock, 50 Leghorn, 30 Broilers). These figures would get too large too quickly. This is why I opted for the current option.

![basket nav](/media/readme/features/basket-nav.png)

**Shopping Basket**

- Tabular view of currently selected products and their quantity
- Quantity adjustment option
- Product removal option
- Display of subtotal, delivery cost (currently always 0) and grand total
- Continue shopping button
- Proceed to checkout option

![basket](/media/readme/features/basket.png)


#### Checkout

**Checkout page**

- Checkout form, including sections for personal info, contact details and card details
- Option to save details to profile for authenticated users
- Current order summery
- Edit Basket button
- Pay now button

![checkout page](/media/readme/features/checkout.png)

**Checkout Success page**

- Confirms successfull order and informs user that email was sent to the address specified
- Displays order details, contact and billing info
- Continue Shopping button ("Back to products")

![checkout success](/media/readme/features/checkout-success.png)


#### Profile

**User Profile page**

- Contact address form (pre-populated if user has previously saved his info)
- Update Info button
- Listing of past orders in order history

![user profile](/media/readme/features/profile.png)


### Possible Future Features

**Extended product range**

The shop has the potential to extend its product range to non-livestock products, such as bird coops, feed, bedding and miscellaneous.
For the purpose of this project however, it was unnecessary to implement such a broad product database.

**Search option**

A search bar could be included in the header or be accessible throughout all products related pages of the site. Currently the product selection is so small that a search bar was deemed unnecessary but would make sense to implement along with an extended product range.

**Automated pick-up date selection**

Currently, the arrangment of a date for product collection is handled manually by shop employees via email or phone contact directly with the customer after order completion.
This could be automated by including calendar element with date picker option to be used after an order is complete.

**Delivery depending on customer location**

Initially I had planned to offer conditional delivery, provided a customer was resident in either County Galway, Clare or Limerick. This is due to the nature of the products. Live animals can not be shipped via postal service or courier. Delivery would need to be done by a shop employee with special transport crates, on an arranged day and as direct as possible. As this is supposed to be a small business, offering a nationwide delivery would seem unrealistic.

I've tried implementing this feature. However, due to time limitations I decided to make the shop pick-up only. This is not unusual for a business selling this type of product and is within the logic of a small scale poultry breeder.

The implentation of the conditional delivery logic was supposed to be achieved like this:

Inside the ``update_total`` helper method in the Order model of the Checkout app, an if statement was to determine which County field a customer had selected in the checkout form (see image below). In 3 specific cases, this would add an additional delivery cost to the grand total of the order.
The issue with this was, that the additional cost did not display to the user until the order and payment was completed and would only show up in the checkout_success page in the order summery. Thus creating an unpleasant surprise for the user.

![add delivery charge logic](/media/readme/future_features/update_total_method.png)

In order to handle the additional charge on the shopping basket level and before completing the order, I tried manipulating both the basket template and re-display the order summery in the checkout template with JavaScript (Thank you Jason, CodeInstitute tutor, for your dedication, patience and relentless support on this one!).

For this, I added "phony" extra-fields in both shopping basket and checkout form. Those fields were set to ``dislpay: none`` and would display a hard-coded value of the delivery charge and updated grand total if the display was changed to ``block`` depending on the selected county field in checkout.

![phony fields on basket and checkout](/media/readme/future_features/extra_fields.png)

Additionally, 2 new variables had to be created in contexts.py in basket app: ``extra_delivery`` and ``extra_delivery_grand_total`` in order to access the new values in the templates.

![new context variables](/media/readme/future_features/context_variables.png)

I also tried adding a checkbox form in the shopping basket which would determine whether the customer was going to be charged delivery or not on the basket level. The JavaScript logic to handle the display of the extra template elements was included in the same file below the form (see image below).

![basket delivery checkbox](/media/readme/future_features/basket_checkbox.png)

The JavaScript to handle the updated display of the extra checkout elements, was included in the checkout template. The image below shows an altered "in progress"-version of the original JS function due to the attempt of ironing out some bugs that came along with it.

![checkout JS](/media/readme/future_features/checkout_js.png)

The reasons for not implementing the feature in the end was this. As the additional delivery charge was being handled on the back-end independantly from the front-end, information was not stored correctly when proceeding from basket to checkout and vice versa.
Unfortunately, the time restrictions and submission deadline made me decide to not currently implement the feature. 
This might make the business a little less competitive but does not impede on the business logic as a whole.


**Forum response approval via front-end**

Currently the approval of user responses to forum entries by admin users is happening solely via the Django admin dashboard. 
There was a valiant attempt at moving this functionality to the front-end for authorised superusers. However, 12 hours later and even with the support of 4 different CodeInstitute tutors the task could not be achieved. Due to time restrictions at this point, the feature will have to be put on hold and find itself in this section of the documentation.

The image below gives an idea of what the feature would look like on the front-end interface.

![Admin response approval on front-end](/media/readme/future_features/frontend-approval.png)


## Database Design

### Database Model

The database model diagram was designed using [Lucidchart](https://lucid.app/lucidchart/dbaa86b5-9b37-4a80-a6f2-ed5048ab2100/edit?viewport_loc=-239%2C119%2C2609%2C1105%2C0_0&invitationId=inv_4bfac1de-d676-4e14-8e5d-9513944644e4).
The first draft of the entity relationship diagram does not include all models used in the final database.

![ERD](media/readme/erd.png)


### Custom Model

As required by the assessment criteria for this project, three custom models were added which were not covered by the Code Institute tutorial this project is based on. These models are ``EntryType``, ``Entry`` and ``Response``, all of the forum app (forum/models.py).

I have also customised models covered the Boutique Ado walkthrough project (see [References](#referencesdocumentationtutorials)) by adding or removing fields and implementing new helper methods. These models are ``Order`` of checkout app (checkout/models.py), ``Category`` and ``Product`` of products app (products/models.py) and ``UserProfile`` of profiles app (profiles/models.py).

### CRUD

Full CRUD functionality via the front-end UI is implemented for admin users in the Forum app and the Products app. 

**Create:**

*Forum:* Create new forum entry. 
*Products:* Add new product. 

**Read:**

*Forum:* Read all existing forum entries. 
*Products:* View all existing products. 

**Update:**

*Forum:* Edit existing forum entries. 
*Products:* Edit existing products. 

**Delete:**

*Forum:* Delete existing forum entries. 
*Products:* Delete existing products. 

For a detailed description of all CRUD features see [Features](#features)

## Technologies Used

### Work Environments and Hosting

- [Figma](https://www.figma.com/) (Wireframes)
- [Lucid](https://lucid.app/) (ERD diagrams)
- [GitHub](https://github.com/) (Version control)
- [GitPod](https://gitpod.io/) (IDE)
- [Heroku](https://heroku.com/) (Site hosting)
- [AWS - Amazon Web servises (S3)](https://aws.amazon.com/) (Hosting static and media files)


### Python Libraries

- [Gunicorn](https://docs.djangoproject.com/en/4.1/howto/deployment/wsgi/gunicorn/) (Python HTTP server for WSGI applications)
- [pyscopg2](https://pypi.org/project/psycopg2/) (PostgreSQL Database adapter)
- [Pillow](https://pypi.org/project/Pillow/) (Python Imaging Library)
- [boto3](https://boto3.amazonaws.com/v1/documentation/api/latest/index.html) (integrates python libraries with AWS services)
- [django-storages](https://django-storages.readthedocs.io/en/latest/) (collection of custom storage backends for Django)
- [Flake8](https://flake8.pycqa.org/en/latest/) (Python linter used for python code validation)

### Django Libraries

- [django-allauth](https://django-allauth.readthedocs.io/en/latest/) (User authentication)
- [django-crispy-forms](https://django-crispy-forms.readthedocs.io/en/latest/) (Control rendering behaviour of Django forms)
- [Bootstrap5 template pack for django-crispy-forms](https://pypi.org/project/crispy-bootstrap5/)
- [django-summernote](https://github.com/summernote/django-summernote) (WYSIWYG HTML editor)

### Payment processing

- [Stripe](https://stripe.com/) (Online payment platform)

### Emails/Newsletter

- [Gmail](https://mail.google.com/) (Real email sending)
- [Mailchimp](https://mailchimp.com/) (Automated newsletter subscription service)


### SEO/Marketing

- [XML Sitemaps](https://www.xml-sitemaps.com/) (Sitemap generator)
- [Privacy Policy Generator](https://www.privacypolicygenerator.info/)

## Testing

### Test Guide

For extensive instructions on how to manually test this site and it's user stories, please refer to these [Manual Testing Instructions](TESTING.md)


### Validator Testing

#### HTML [W3C validator](https://validator.w3.org/)

As this is a Django project, the HTML couldn't be tested via the site's URL, due to Django tags and Jinja templating language in HTML files. Instead, the source code of each page was pasted into the validator directly.

**Error page**

*Result:*

![error result](/media/readme/validation/html-noerrors.png)

**SignUp/Login/Logout page**

*Result:*

![error result](/media/readme/validation/html-noerrors.png)

**Base/Home page**

*Result:*

![base result](/media/readme/validation/html-base.png)

*Fix:*

- 1. (Error): Remove ``p`` element from inside ``button`` element
- 2.-5.(Warnings): Remove ``type`` attributes from ``script`` elements

**About page**

*Result:*

![about result](/media/readme/validation/html-about.png)

*Fix:*

- 1. (Warning): Add ``h2`` to first ``section`` element
- 2. (Error): Move ``h3`` outside ``address`` element
- 3. (Warning): Remove ``aria-label`` attribute from ``div`` element and add it ``h3`` instead

**Privacy page**

*Result:*

![privacy result](/media/readme/validation/html-noerrors.png)


**All Products page**

*Result:*

![all products result](/media/readme/validation/html-noerrors.png)


**Products page**

*Result:*

![products result](/media/readme/validation/html-products.png)

*Fix:*

- 1. (Warning): Remove ``type`` attributes from ``script`` element

**Product details page**

*Result:*

![products details result](/media/readme/validation/html-noerrors.png)


**Add product page**

*Result:*

![](/media/readme/validation/html-noerrors.png)


**Edit product page**

*Result:*

![](/media/readme/validation/html-noerrors.png)

*Fix:*


**Forum page**

*Result:*

![forum results](/media/readme/validation/html-forum.png)

*Fix:*

- 1., 3., 4., 6., 7., 9. (Errors): Move ``a`` element with filter functionality outside ``a`` element linking to entry detail

- 2., 5,. 8. (Errors): Add "friendly_name" field to EntryType model in forum app. Include helper method ``get_friendly_name`` and ``save`` method to auto-generate name from friendly name. Adjust link in forum template and entry_details template accordingly.

Also added method in EntryForm to render friendly name as select option (source: [Boutique Ado walkthrough](https://github.com/Kathrin-ddggxh/CI_boutique-ado/blob/main/products/forms.py#:~:text=def%20__init__(,choices%20%3D%20friendly_names)))

**Forum entry details page**

*Result:*

![entry details result](/media/readme/validation/html-entry-detail.png)

*Fix:*

- 1. (Error): Remove ``p`` tags from around rendered entry content

- 2. (Error): Add placeholder value (#) to action attribute 

**Add forum entry page**

*Result:*

![add entry result](/media/readme/validation/html-add-entry.png)

*Fix:*

No fix required. All errors listed by W3Validator are related to Summernote and not any code written by myself.
Research within the CodeInstitute community has shown that is a common occurance and should be noted but is not necessary to action over.

**Edit forum entry page**

*Result:*

![edit entry result](/media/readme/validation/html-add-entry.png)

*Fix:*

No fix required. All errors listed by W3Validator are related to Summernote and not any code written by myself.
Research within the CodeInstitute community has shown that is a common occurance and should be noted but is not necessary to action over.

**Profile page**

*Result:*

![profile result](/media/readme/validation/html-profile.png)

*Fix:*

- Remove "PLACEHOLDER" value from COUNTIES list in profile/models.py. Adjust UserProfileForm rendering to display default labels

**Shopping Basket page**

*Result:*

![basket result](/media/readme/validation/html-noerrors.png)


**Checkout page**

*Result:*

![checkout result](/media/readme/validation/html-checkout.png)

*Fix:*

- Change ``h1`` element to ``div`` element


**Checkout Success page**

*Result:*

![checkout success result](/media/readme/validation/html-noerrors.png)


**Order History page**

*Result:*

![order history result](/media/readme/validation/html-noerrors.png)


#### CSS [Jigsaw](https://jigsaw.w3.org/css-validator/)

No errors found.

![jigsaw results](/media/readme/validation/css-results.png)


#### JavaScript [JSHint](https://jshint.com/) 

**Basket app**

*quantity_input_script.html*: 

No errors or warnings

*basket.html (line 88-104)*: 

2 warnings: Missing semicolons

Fix: Add semicolons

**Checkout app**

*stripe_elements.js*: 

1 warning: Missing semicolon

Fix: Add semicolon

1 undefined variable ``Stripe``, line 11

Fix: No fix required, variable is inherent in Stripe functionality 

**Forum app**

*entry_detail.html*:

2 warnings: Missing semicolons

Fix: Add semicolons

**Products app**

*quantity_input_script.html*:

No errors or warnings

*product_details.html*:

No errors or warnings

**Global**

*base.html*:

![base js result](/media/readme/validation/js-base.png)

All error and warnings in the above result refer to the default script that comes with the MailChimp newsletter functionality. Therefore no fix is required. 


#### Python [Flake8](https://flake8.pycqa.org/en/latest/user/invocation.html)

As there are a multitude of python files throughout this project, rather than testing each file individually in an external validator (huge time investment!), I opted for running the python linter Flake8 in editor via the CLI with ``python3.8 -m flake8``.

Any files auto-generated by Django or not written by myself were ignored in terminal output.

I also decided that (unused) imports in Django files that are inherent to those types of files and automatically imported by Django were safe to ignore.

Only unused variables and imports that I deemed truely unnecessary were removed in the end.

![flake8 results](/media/readme/validation/flake8-result1.png)
![flake8 results](/media/readme/validation/flake8-result2.png)
![flake8 results](/media/readme/validation/flake8-result3.png)
![flake8 results](/media/readme/validation/flake8-result4.png)
![flake8 results](/media/readme/validation/flake8-result5.png)


#### Performance, Accessibility, SEO, Best Practices (Lighthouse Chrome DevTools)

**Desktop results**

![lighthouse results desktop](/media/readme/lighthouse-desktop.png)

The yellow scores in Performance and Best Practices are due to referencing external libraries and technologies such as Bootstrap, JQuery and Stripe that the project depend on and cannot be removed.

**Mobile results**

![lighthouse results mobile](/media/readme/light-mobile.png)

The yellow score in Performance is due to referencing external libraries and technologies such as Bootstrap, JQuery and Stripe that the project depend on and cannot be removed.

### Browser Testing

**Layout:** 

Testing layout and appearance of site for consistency across browsers.

**Functionality:** 

Testing complete functionality of the site as specified in the [Manual Testing Instructions](TESTING.md) accross browsers.

| Browser     | Layout      | Functionality |
| :---------: | :----------:| :-----------: |
| Chrome      | ✔          | ✔             |
| Edge        | ✔          | ✔             |
| Firefox     | ✔          | ✔             |
| Safari      | ✔          | ✔             |
| IE          |deprecated by Microsoft, not tested|

### Fixed bugs

- **Placeholder for County dropdown list in checkout form**:

    Placeholder "County *" for the dropdown menu in checkout form is not displaying in muted colour.

    **Fix**:

    Remove Boutique Ado inspired styling. This styling overwrote the original form styling and was not necessary or in keeping with other forms found on the site.

    Also, make County field a non-required field. This was possible due to the removal of the conditional delivery charge functionality, for which the County field needed to be required (see [Future Features](#possible-future-features)).


- **Verbose name in "Entry" model not working**:

    In forum app, the model ``Entry`` has an added Meta class to set the verbose name in the admin interface to the correct plural "Entries". The name in the admin panel however shows "Entrys".

    **Fix**:

    Oversight! I had created 2 Meta classes in the Entry model. The first specifying ``verbose_name_plural``, the second specifying ``ordering``. Due the presence of a second Meta class, the first one was being ignored. Condensing both specifications into the one Meta class fixed the problem.

- **``alt`` attribute on forum post image**:

    The value for the ``alt`` attribute on images attached to forum posts needs to be descriptive to adhere to accessibility standards.

    **Fix**:

    Create ``get_img_alt_value`` helper function in ``Entry`` model of forum app.

- **Response in not specific to entry**:

    An approved user response would show underneath every forum entry, as oppose to only the one the user actually commented on.

    **Fix**: 

    Change ``response = Response.objects.all()`` to ``response = Response.objects.filter(entry=entry)`` in entry_detail view in forum app (line 39).
    
    Reference: https://stackoverflow.com/questions/62195043/how-to-get-comment-for-the-particular-blog-post-in-django


### Unfixed bugs

There are currently no known bugs 😀


## Deployment

This project was deployed using [Heroku](https://heroku.com/), [ElephantSQL](https://www.elephantsql.com/) and [AWS](https://aws.amazon.com/). For a full list of libraries refer to [Technologies Used](#technologies-used).

#### Installing libraries

The following steps outline all libraries needed for successful deployment on Heroku. All necessary requirements and settings updates will not be discussed in this section as they are assumed as logical follow-up steps to installments. For full explanation on how to install these libraries, refer to the links provided in [Technologies Used](#technologies-used).

- Install **pyscopg2** (connects to PostgreSQL): ``pip 3 install dj_database_url pyscopg2``
- Install **Gunicorn** (server used to run Django on Heroku): ``pip3 install django gunicorn``

#### Creating the Heroku App

- Log into Heroku and go to the Dashboard
- Click **New** and select **Create new app** from the drop-down
- Name app appropriately and choose relevant region, then click **Create App**

#### Create PostgreSQL database using ElephantSQL

This is necessary to create a database that can be accessed by Heroku. The database provided by Django can not be accessed by the deployed Heroku app.

- Log into ElephantSQL and go to Dashboard
- Click **Create New Instance**
- Set up a plan by providing a Name (project name) and select a Plan (for this project the free plan "Tiny Turtle" was chosen). Tags are optional.
- Click **Select Region** and choose appropriate Data center
- Click **Review**, check all details and click **Create Instance**
- Return to Dashboard on click on the name of the newly created instance
- Copy the database URL from the details section

#### Hiding sensitive information

- Create ``env.py`` file and ensure it is included in the ``.gitignore`` file
- Add ``import os`` to env.py file and set environment variable **DATABASE_URL** to the URL copied from ElephantSQL (``os.environ["DATABASE_URL"]="<copiedURL>"``)
- Below, set **SECRET_KEY** variable (``os.environ["SECRET_KEY"]="mysecretkey"``, but be more inventive about the key string!)

#### Update Settings

- Add the following code at the top of ``settings.py`` to connect Django project to env.py:
    ````
      import os
      import dj_database_url
      if os.path.isfile('env.py'):
          import env
    ````
- Remove insecure secret key provide by Django in settings.py and refer to variable in env.py instead (``SECRET_KEY = os.environ.get('SECRET_KEY')``)

- To connect to new database, replace provided **DATABASE** variable with 
    ````
    DATABASES = {
        'default': dj_database_url.parse(os.environ.get("DATABASE_URL"))
    }
    ````
- Save and migrate all changes made and load in fixtures

#### Preparing for Heroku

- Create Procfile (tells Heroku to create web dyno which will run gunicorn and serve Django app)

- Temporarily disable collectstatic (prevent Heroku from collecting static files when deploying)

- Allow Heroku as host:

    In ``settings.py`` add
        ````
        ALLOWED_HOSTS = ['app-name.herokuapp.com', 'localhost']
        ````

#### Connecting Heroku to Database

- In Heroku dashboard, go to **Settings** tab
- Add three new config vars **DATABASE_URL** (value is database URL), **SECRET_KEY** (value is secret key string) and **PORT** (value "8000")


#### Deyploying with Heroku

- In Heroku dashboard, go to **Deploy** tab
- Select "GitHub" as Deployment method and choose correct repo
- Enable Automatic Deploys
- Click "Deploy Branch" button


#### Hosting images and static file with AWS

- Create AWS account and go to AWS Management Console in the My Account dropdown
- Find and access S3 as a service and create a new bucket:

    Under Object Ownership, check "ACLs enabled"

    Uncheck "Block all public access" and acknowledge (required for public access to static files)

- Configur bucket settings:

    Under **Properties**, enable Static Website Hosting

    Under **Permissions**, copy the following code into CORS section:

    ```
    [
        {
            "AllowedHeaders": [
                "Authorization"
            ],
            "AllowedMethods": [
                "GET"
            ],
            "AllowedOrigins": [
                "*"
            ],
            "ExposeHeaders": []
        }
    ]
    ```
    This is required to set up the access between the Heroku app and the S3 bucket.

    Under **Bucket policy**, go to Policy generator.

    Bucket Type = S3 Bucket Policy

    Principal = * (allows all principles)

    Actions = GetObject

    Paste in ARN from bucket settings tab.

    Click Add Statement, then Generate Policy.

    Copy policy in paste into bucket policy editor. Also add ``/*`` onto the end of the resource key.

    Click Save.

    Under **Access control list (ACL)**, check "List" checkbox for "Everyone (public access)"

- Create user to access bucket with IAM (Identity and Access Management)

    In IAM, got to User Groups (sidebar left).

    There create a group for a user, create an access policy giving the group access to the S3 bucket and assign the user to the group so it can use the policy to access all files. 

- Connect Django to S3

    Install packages "boto3" and "django-storages" and add ``'storages'`` to INSTALLED_APPS  in settings.py

    Configure settings.py accordingly, including necessary AWS variables.

    Add new config vars in Heroku app settings, including user credentials from AWS.

    Create ``custom_storages.py`` file.

- Upload static files and media files to S3


#### Add Stripe keys to Heroku

From Stripe account, under Developers > API keys copy Public Key and Secret Key and set as config vars in Heroku app settings.

Create new Webhook endpoint for deployed site and enable all events. Then add Signing Secret to Heroku app config vars.


## Development

The following options are available to work with this code or run in a local environment.

### Fork

Any changes made to a forked repository do not affect the original repository.

- Log into GitHub and click on repository to download ([chirpy_chooks](https://github.com/Kathrin-ddggxh/chirpy_chooks))
- Click the **Fork** buttonin the top right-hand corner
- Select a different owner if necessary
- Click **Create Fork**
- The repo is now in your chosen account and can be cloned or changed

### Clone

Changes made to a cloned repository will affect the original one.

- Navigate to the main page of the repostitory (this could be a forked instance)
- Click on the **Code** dropdown menu above the list of files
- Choose a method to copy the URL for the repository: either via **HTTPS**, by using an **SSH key**, or by using **GitHub CLI**
- In your work environment, open Git Bash and change current directory to target location for cloned repository
- Type ``git clone`` followed by the copied URL and press enter **Enter**

### Download as ZIP

- Log into GitHub and click on repository to download ([chirpy_chooks](https://github.com/Kathrin-ddggxh/chirpy_chooks))
- Select **Code** and click "Download Zip" file
- Once download is completed, extract ZIP file and use in your local environment

## Source Credits

### References/Documentation/Tutorials

**General**:

The official [Django Documentation](https://docs.djangoproject.com/en/4.1/) was used throughout creating this project.
The skeleton of this project is based on the [Code Institute](https://codeinstitute.net/ie/) tutorial ["Boutique Ado"](https://github.com/Code-Institute-Solutions/boutique_ado_v1/tree/250e2c2b8e43cccb56b4721cd8a8bd4de6686546).

**Basket tools**:

[Django Docs on creating custom template tags](https://docs.djangoproject.com/en/4.1/howto/custom-template-tags/)

**Basket items count display in navbar**:

The syntax for displaying the amount of items currently in the shopping basket was taken from this [FeelFreeToCode tutorial](https://www.youtube.com/watch?v=3xQRJqxdgK4&ab_channel=FeelFreeToCode)

**User alerts (toasts/messages)**:

The live feedback messages to alert user actions were implemented using the [Django message framework](https://docs.djangoproject.com/en/4.1/ref/contrib/messages/) and the respective [message levels](https://docs.djangoproject.com/en/4.1/ref/contrib/messages/).

The alert pop-up frames were rendered using [Bootstrap 5 toasts](https://getbootstrap.com/docs/5.0/components/toasts/).

**Custom error pages**:

To implement custom error pages in Django I followed this [Cryce Truly tutorial](https://www.youtube.com/watch?v=3SKjPppM_DU&ab_channel=CryceTruly)

**Forum response form submission**:

There were issues submitting the response form in forum/views.py initially. This was resolved referring to the following [StackOverflow article](https://stackoverflow.com/questions/60497516/django-add-comment-section-on-posts-feed)


### Media and Styling

**Images:**

*freerange-hens.jpg*: Me! (Kay Welfare)

*rhode-island-red.jpg:* https://poultrypaddock.co.uk/wp-content/uploads/2017/11/blacktail1-1.jpg

*bluebell.jpg:* https://poultrypaddock.co.uk/wp-content/uploads/2017/11/Bluebell3_1.jpg

*light-sussex.jpg:* https://poultrypaddock.co.uk/wp-content/uploads/2017/11/sussex3.jpg

*blackrock.jpg:* https://poultrypaddock.co.uk/wp-content/uploads/2017/11/blackrock4.jpg

*copper-black-maran.jpg:* https://poultrypaddock.co.uk/wp-content/uploads/2017/11/maran.jpg

*white-leghorn.jpg:* https://poultrypaddock.co.uk/wp-content/uploads/2017/11/Leghorn1_1.jpg

*broiler-chicken.png:* https://thefewellhomestead.com/broiler-chicken-breeds-16-of-the-best-meat-chickens/

*aylesbury-duck.jpg:* https://www.thehappychickencoop.com/aylesbury-duck/

*khaki-campbell.jpg:* https://livestockconservancy.org/wp-content/uploads/2022/08/Campbell-Pair.jpg

*ancona-duck.jpg:* https://www.breedslist.com/wp-content/uploads/2016/10/Ancona-Duck.jpg

*laying-hen.jpg:* https://learnpoultry.com/best-egg-laying-chickens/

*broiler.jpg:* https://vegsoc.org/info-hub/why-go-veggie/animals/broiler-chickens/

*laying-duck.jpg:* https://www.thehappychickencoop.com/raising-ducks-for-eggs/

*noimage.png:* https://upload.wikimedia.org/wikipedia/commons/thumb/4/42/Chicken_cartoon_04.svg/300px-Chicken_cartoon_04.svg.png 

*chicken-question.jpg:* https://www.dreamstime.com/stock-photography-cartoon-chicken-doubt-yellow-little-bird-speech-bubble-question-mark-image30411162


All images used in the **Facebook mock-up business page** are my own, taken by myself of my own chickens!

**Fonts:**

All fonts were taken from [Google Fonts](https://fonts.google.com/).

*Pacifico*: Designed by Vernon Adams, Jacques Le Bailly, Botjo Nikoltchev, Ani Petrova

*Varela Round*: Designed by Joe Prince

**Icons:**

All icons were taken from [Iconify](https://icon-sets.iconify.design/). Included in this is the animated loading spinner icon of the checkout page.


### Content/Data

#### Products

All fixtures for the products app were manually compiled with data gathered from various online resources.

**All layer breeds**: https://www.freewaypoultry.ie/product-category/live-poultry/point-of-lay-pullets/

**Broiler (Cornish Cross)**: https://thefewellhomestead.com/broiler-chicken-breeds-16-of-the-best-meat-chickens/

**All duck breeds**: https://petkeen.com/best-egg-laying-duck-breeds/

#### Forum

Content for the few example forum entries came from the following sources.

**A look at Lohman Brown**: https://www.thehappychickencoop.com/lohmann-brown-chicken/

    Image: Me! (Kay Welfare)

**Natural mite control**: https://www.freedomrangerhatchery.com/blog/how-to-get-rid-of-chicken-mites-and-lice-naturally/

    Image: Me! (Kay Welfare)

**Reviewing Pedigree Organic Layers Pellets**: https://www.pets.ie/c/organic-layers-pellets/476?gtagrefurl=https%3a%2f%2fwww.google.com%2f

    Image: https://totaldiy.ie/wp-content/uploads/Pedigree-Organic-Layers-Pellets-20Kg.png

