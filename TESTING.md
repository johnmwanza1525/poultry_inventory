# Testing Instructions

## Table of Contents

- [Manual Testing](#manual-testing-guide)
    - [Global](#global)
    - [Home](#home)
    - [About](#about)
    - [Products](#products)
    - [Forum](#forum)
    - [Profile](#profile-authenticated-users)
    - [Basket](#basket)
    - [Checkout](#checkout)
    - [User Feedback](#user-feedback)


## Manual Testing Guide

### Global

**Navigation**

| Feature | Action             | Expected Result                 |
| :-----: | :-----------------:| :------------------------------:|
| **Home Link Logo** | While not on homepage, click logo. | User is redirected back to homepage. |
| **"Home" Link** | While not on homepage, click "Home". | User is redirected back to homepage. |
| **"Live Poultry" dropdown** | Click dropdown in navbar | User is presented with a list of links (all categories, specific sub-categories) |
| **Poultry sub-categories** | From "Live Poultry" dropdown, select sub-link | User is directed to page listing all products of same category |
| **"Forum" link** | Click Forum link in navbar | User is directed to main forum page listing all entries |
| **"About Us" link** | Click About Us link in navbar | User is directed to about page with general business info |
| **"Profile" dropdown** | Click Profile dropdown | Authenticated user sees option to "Manage Profile". Admin user sees option to "Manage Profile", "Manage Products" and "Post in Forum". Dropdown is not visible to unregistered users. |
| **"Login" Link** | While not authenticated, click "Login". | User is directed to Login form. |
| **"Sign Up" Link** | While not authenticated, click "Sign Up". | User is directed to Sign Up form. |
| **"Logout" Link** | While authenticated, click "Logout". | User is directed to page with Sign Out button. |
| **"Basket" Link** | Click Basket link in navbar | User is directed to shopping basket page. |


**Authentication**

| Feature | Action             | Expected Result                 |
| :-----: | :-----------------:| :------------------------------:|
| **Login** | As already registered user, got to login page, complete login form and click login button. | Form validation is in effect. Remember me checkbox will store user information for next login. User is directed to homepage and success message informs of successful login as "username" |
| **Forgot Password function** | On Login page, click Forgot Password link. | User is directed to Reset Password page. Form validation is in effect. Reset link is sent to user email through which password can be reset. |
| **Sign Up** | As unregistered user, go to Sign Up page, complete form and submit | Form validation is in effect. User will receive confirmation email with link to verify registration (see below). After clicking link, user is directed to Login page. Success message informs of successful account registration. |
| **Logout** | As authenticated user, got to Logout page and click Sign out button | User is directed to homepage and success message informs user of successful sign out. |

**Real emails**

| Feature | Action             | Expected Result                 |
| :-----: | :-----------------:| :------------------------------:|
| **Account registration** | Recommended to test with temporary email address (example: [TempMail.org](https://temp-mail.org/en/)). Go through Sign up process via Sign Up page | New page and alert message informs user that email has been sent. User receives confirmation email with confirmation link. When clicked, link directs user success page with link to login page. |

**Social media links (located in footer)**

| Feature | Action                  | Expected Result                 |
| :-----: | :----------------------:| :------------------------------:|
| **Social media links** | Click on any of the social media icons | New tab opens with respective social media site |

**Newsletter**

No actual newsletter is set up to be sent out to subscribers. However, the infrastructure for subscription is in place as a form in the footer.

| Feature | Action                  | Expected Result                 |
| :-----: | :----------------------:| :------------------------------:|
| **Newsletter form** | Enter email address and click Subscribe | Users sees message "Thanks for subscribing!" |

**Privacy Policy**

| Feature | Action                  | Expected Result                 |
| :-----: | :----------------------:| :------------------------------:|
| **Privacy Policy page** | Click "Privacy Policy" link in footer | Users is directed to policy page where they can read the complete GDPR compliant document |

**404 error page**

| Feature | Action                  | Expected Result                 |
| :-----: | :----------------------:| :------------------------------:|
| **Custom 404 page** | Append faulty extension to home URL (or simply /404) | Users is directed to customised 404 error page, informing them of invalid URL with a Back to Homepage button |


### Home 

**Shop Now button**

| Feature | Action                  | Expected Result                 |
| :-----: | :----------------------:| :------------------------------:|
| **Buy Live Poultry button** | Click button located on homepage | Users is directed to all products page, listing all available categories |


### About

| Feature | Action                  | Expected Result                 |
| :-----: | :----------------------:| :------------------------------:|
| **Opening Hours link** | Click link in pick-up info section | Page scrolls down to opening hours section |
| **Forum link** | Click link in contact section | User is directed to main forum page |


### Products 

**All Products page**

| Feature | Action                  | Expected Result                 |
| :-----: | :----------------------:| :------------------------------:|
| **Forum link** | Click link in info paragraph | User is directed to main forum page |
| **Contact Us link** | Click contact us link in info paragraph | User is directed to Contact section on About Us page |
| **Category link** | Click on any category tile below info paragraph | User is directed to products page of respective category |


**Products page (of same category)**

| Feature | Action                  | Expected Result                 |
| :-----: | :----------------------:| :------------------------------:|
| **Forum link** | Click link in info paragraph | User is directed to main forum page |
| **Quick link (back to all products)** | Click link at the top of the page, just below navbar | User is directed back to the All Products page |
| **Product tile link** | Click on any product tile below info paragraph | User is directed to product details page of respective product |


**Product Details page**

| Feature | Action                  | Expected Result                 |
| :-----: | :----------------------:| :------------------------------:|
| **Quick link (back to category)** | Click link at the top of the page, just below navbar | User is directed back to the category page of this product's category |
| **Page content** | On products detail page | User can see product image (or placeholder in case of no image), read product specs and see price |
| **Quantity form** | Enter different value into quantity input. | Values outside the range of 1-99 will show form validation error when adding product to basket |
| **Quantity adjustment buttons** | Adjust quantity input value with - or + button | Value will not go below 1 or above 99. Buttons become pale when reaching top or bottom range |
| **Browse more button** | Click button | User is directed back to all products page |
| **Add to basket button** | Click button | Product is added to basket with specified quantity. Basket nav link updates to show current number of product types |


**Products admin user (CRUD)**

| Feature | Expect             | Action                   | Result                 |
| :-----: | :-----------------:| :-----------------------:| :---------------------:|
| **Adding products** | Add products form allows submission of new entry which displays on forum page | Complete add products form in Profile > Manage Products and submit form | Form validation is effective. User is redirected to detail page of newly submitted product. Success alert displays. |
| **Editing products** | Edit option on each product detail page allows admin user to edit existing product. | Click Edit below product image. Update pre-populated form and submit. | After clicking Edit, info alert tells user that post is being edited. Form validation is effective. Form submit redirects user to product detail page with updated content. Success alert displays. |
| **Deleting products** | Delete option on each product detail page allows admin user to delete existing product. | Click Delete at the bottom of forum entry. | User is requested to confirm deletion of product. "Yes, I'm sure" button deletes product and success alert confirms action. "No, I'm not" button cancels delete action. |


### Forum

**Unauthenticated Users**

| Feature | Expect             | Action                   | Result                 |
| :-----: | :-----------------:| :-----------------------:| :---------------------:|
| **Forum page** | Tiled list view of forum entries | Navigate to Forum via navlink | User sees all entries listed as linked tiles |
| **Entry Detail** | Full content of forum entry | Click on entry on forum page | User sees new page with entry content, and approved comments below |
| **Filter option** | Displays all entries of same type | Either on forum or on entry detail page, click on "type" button near entry title | User sees list of entries of same type |
| **Clear filter** | Displays all forum entries | After selecting an entry type, click "Clear Filter" button | User is brought back to forum page with all entries |

**Authenticated Users**

| Feature | Expect             | Action                   | Result                 |
| :-----: | :-----------------:| :-----------------------:| :---------------------:|
| **Responding** | Response form under forum entry with submit option | Fill out response form and submit | Alert message informs user that response is awaiting approval |
| **View Responses** | Approved responses to specifice entries listed below entry | Scroll below forum entry in entry detail page | User can read approved responses |

**Admin Users (CRUD)**

| Feature | Expect             | Action                   | Result                 |
| :-----: | :-----------------:| :-----------------------:| :---------------------:|
| **Adding entry** | Forum entry form allows submission of new entry which displays on forum page | Complete forum entry form in Profile > Post in Forum and submit form | Form validation is effective.User is redirected to detail page of newly submitted entry. Success alert displays. |
| **Editing entry** | Edit option on each entry detail page allows admin user to edit existing entry. | Click Edit at the bottom of forum entry. Update pre-populated form and submit. | After clicking Edit, info alert tells user that post is being edited. Form validation is effective. Form submit redirects user to entry detail page with updated content. Success alert displays. |
| **Deleting entry** | Delete option on each entry detail page allows admin user to delete existing entry. | Click Delete at the bottom of forum entry. | User is requested to confirm deletion of entry. "Yes, I'm sure" button deletes entry and success alert confirms action. "No, I'm not" button cancels delete action. |


### Profile (authenticated users)

| Feature | Action                  | Expected Result                 |
| :-----: | :----------------------:| :------------------------------:|
| **Profile page** | Go to My Profile via Manage Profile link in navbar | User sees update form for default contact info and tabular view of complete order history |
| **Contact Info form** | Fill out form and submit info/new changes. Add items to basket and proceed to checkout | Form validation is in effect. On Checkout page, contact info section of payment form is pre-populated with saved info from user profile. |
| **Review past order** | In order history, click order number link of any past order. | User is directed to new page displaying complete details of selected order. Alert message informs that info shown is of past order. Back to profile button links back to Profile page. |

### Basket

| Feature | Action                  | Expected Result                 |
| :-----: | :----------------------:| :------------------------------:|
| **Empty Basket** | Without adding items to basket, go to Basket page via navbar | Basket page displays "Basket is empty" message and Back to Products button, linking to All Products page |
| **Basket page** | Add item(s) to basket and go to Basket page via navbar | User sees tabular view of all items in basket, incl. subtotals for all items, delivery cost (currently default of 0) and grand total |
| **Basket page** | Add item(s) to basket and go to Basket page via navbar | User sees tabular view of all items in basket, incl. subtotals for all items, delivery cost (currently default of 0) and grand total |
| **Quantity adjustment buttons** | Adjust quantity input value with - or + button | Value will not go below 1 or above 99. Buttons become pale when reaching top or bottom range |
| **Update item** | Change quantity of selected item and click Update | Success message informs user that quantity for "product name" was updated to new value. Basket now displays new value, subtotal and grand total. |
| **Remove item** | Click Remove on any item in basket. | Success message informs user that "product name" was removed from basket. Basket now displays new grand total. |
| **Keep Shopping button** | Click Keep Shopping button on basket page. | User is directed to All Products page while basket information and contents are stored. |
| **Checkout button** | Click Go to Checkout button on basket page. | User is directed to Checkout page. |

### Checkout

| Feature | Action                  | Expected Result                 |
| :-----: | :----------------------:| :------------------------------:|
| **Checkout page** | On Basket page, click "Go to Checkout" button. | User sees complete payment form with sections for Personal Info, Contact Info and Payment details. Display of order summery.  |
| **Save Info to Profile** | As authenticated user, tick "Save contact info to profile checkbox and complete and submit form. Then go to My Profile page. | Form on Profile page is pre-populated with information specified during checkout process. |
| **Unregistered users** | As unauthenticated user, go to Checkout page. | Below Contact info section, "Create account" link and "login" link show, directing back to Sign Up/Login page. |
| **Edit Basket button** | Click Edit Basket button below form. | User is directed back to Basket page where they can edit order contents. |
| **Payment** | Fill out form and click Pay Now button. | Form validation is in effect. Loading spinner displays while payment is being processed. User is directed to Checkout Success page. Success message informs user of successful order placement with order number and email address. |
| **Checkout Success page** | Complete an order and get directed to Checkout Success page. | User can view complete summery of placed order, inlcuding order number, order contents, personal info and date of order. Back to Products button links back to All products page. |

**Checking for successful payment**

To verify that a payment was successful, I went to the Stripe website to confirm that both the event and webhook creation showed no errors.

![stripe event](/media/readme/stripe-event.png)
![stripe webhook](/media/readme/stripe-webhook.png)

### User Feedback

Small pop-up messages of the types *"Alert", "Success", "Warning" and "Error"* will display for the following user actions:

**Products**

- Unauthorised user trying to add new product
- Add new product (authorised users only)
- Submit invalid product form
- Unauthorised user trying to edit existing product
- Edit existing product (unauthorised users only)
- Submit invalid form when editing product (authorised users only)
- Accessing product edit page and form (authorised users only)
- Unauthorised user trying to delete existing product
- Delete existing product (authorised users only)

**Forum**

- Response submit (response awaiting approval)
- Submit invalid response form
- Unauthorised user trying to create forum entry
- Post forum entry (authorised users only)
- Submit invalid forum entry form
- Unauthorised user trying to edit existing forum entry
- Edit existing forum entry (authorised users only)
- Submit invalid form when editing forum entry
- Accessing entry edit page and form (authorised users only)
- Unauthorised user trying to delete existing forum entry
- Delete existing forum entry (authorised users only)

**Profile**

- Update profile
- Submit invalid form when updating profile
- Review past orders via profile page

**Basket**

- Update item quantity in shopping basket
- Add product to basket
- Remove item from basket
- Unable to remove item from basket

**Checkout**

- 400 error in payment processing
- Product in basket not found in database
- Submit invalid checkout form
- Accessing checkout with empty basket
- No Stripe public key present (payment process)
- Successful order completion


