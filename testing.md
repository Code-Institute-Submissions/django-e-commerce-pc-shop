- Go [Back to Readme](README.md).

## Testing

### Manual Testing
- Manual tests have been done throughout the development of the project.
  The following test scenarios confirms that the website is behaving accordingly.

### Browers used in testing

- Google Chrome
    - Used for testing site through all developing process and DevTools for    responsiveness and scaling issues on different screen sizes.

- Mozilla Firefox
    - Used for testing site and responsiveness and scaling.

- Opera Web Browser
    - Used for testing site and responsiveness and scaling.

- Microsoft Edge 
    - Used for testing site and responsiveness and scaling.

This was the primary method of testing throughout the development of the project.

### Validation

[**W3C CSS Validator**](https://jigsaw.w3.org/css-validator/) 
- This is online CSS code validator
- All css files pass testing


[**W3C HTML Validator**](https://validator.w3.org/)
- This is online HTML code validator
- Spotted few main errors and some are fixed some i choose to ignore and try to fixed later.
    

[**PEP8 Validator**](http://pep8online.com/)
- This is online Python validator
- Errors mosty come back complaining about "Too long lines"
- Code pass validation.

### User story testing

- As a shopper i want to be able to view a list of products so that i can select some to purchase.

    - If shooper click on Dropdown menu `All Products` and then `All product` he will get List of `All Products`.

- As a shopper i want to be able to change layout od displayed items so that i can get different view on products.

    - On `All Product` page if shooper click on `List icon` layout of displayed product will change.

- As a shopper i want to be able to visit the manufacturer website so that i can read more about product.

    - If shopper click on any `Manufacturer` logo, new window will open and user will be redirect to `Manufacturer` page.

- As a shopper i want to be able to quickly identify deals, special offers and promotions so that i can take advantage of special savings on products i'd like to purchase.

    - If shooper click on `Special Offers` then `Deals` he will be redirect to product page with all deals.

- As a shopper i want to be able to see product availability so I can make purchasing decisions.

    - All products have clean displayed of their availability.

- As a shopper i want to be able to sort a list of products so that i can easily indentify the best rated, best priced and categororically sorted products.

    - Shooper have option to sort and filter products by Category, Brand, Price, Rating and Name.

- As a shopper i want to be able to sort a specific category of products so that i can find the best priced or best rated product in a specific category, or sort products by brand.

    - Shooper have option to sort and filter products by Category, Brand, Price, Rating and Name.

- As a shopper i want to be able to search for a product by name or description so that i can find a specific product i'd like to purchase.

    - If shopper use `Search Bar` on top of page he will be able to search and filter product. 

- As a shopper i want to be able to subscribe to newsletter so that i can get lattest news and promotions.

    - On Home page if Shopper click on `Subscribe` he will be redirect to Newsletter form for registration.

- As a shopper i want to be able to easily see what i've searched for and the number of results so that i can quickly decide whether the product i want is available.

    - If shooper use search bar and enter matching results he will get information how much product application find.

- As a shopper i want to be able to read product specifications and detail so that i can deside if this product suit my needs.

    - On `Product detail` page shooper can read product description and specifications.

- As a shopper i want to be able to easily navigate to additional information about product so that i can read more about product.

    - On `Product detail` page if user click on `Additional Information` page will scroll down to additional information about product.

- As a shopper i want to be able to easily indentify product brand and supported hardware so that i can deside about purchase.

    - Shooper can easily indentify product brand and supported hardware by reading `Specifications` and product brand is on top of page and can be easily indentify by shooper.

- As a shopper i want to be able to indentify my current position on the page so that i can easily navigate through the page.

    - If user Search for product of click on All product he can easily indentify his current position on the page.

- As a shopper i want to be able to read about new market products so that i can be informed about product and make purchasing decisions.

    - If shooper click on `Blog` he can fint there all newer information about new market products.

- As a shopper i want to be able to easily view the total of my purchases at any time so that i can avoid spending too much.

    - Shooping bag and total amount of current spending is always visible to shooper on top right corner.

- As a shopper i want to be able to view items in my bag to be purchased so that i can identify the total cost of my purchase and all items i will receive.

    - If shooper click on `Shooping Bag` icon in right corner he will be redirect to shooping bag and get all information about his current shopping.

- As a shopper i want to be able to adjust the quantity of individual items in my bag so that i can easily make changes to my purchase before checkout.

    - When shooper is in `Shooping bag` before `Checkout` he can easily adjust quantity of items.

- As a shopper i want to be able to easily enter my payment information so that i can check out quickly without any problems.

    - Shooper before Checkout can easily enter his payment information and review then before he make final decision.

- As a shopper i want to be able to feel my personal and payment information is safe and secure so that i can verify that i havent't make any mistakes.

    - By using Stripe payment system all user information are safe and secure.

- As a shopper i want to be able to view an order confirmation after checking out so that i can keep the confirmation of what i've purchased for my records.

    - After shooper purchase desired items he will get order confirmation.

- As a shopper i want to be able to recive an email confirmation after checking out so that i can keep the confirmation of what i've purchased for my records.

    - After shooper purchase desired items he will get order confirmation on his email.

- As a shopper i want to be able to receive confirmation by email after subscribing to the newsletter so i can be sure that I will receive the latest news and promotions.

    - After subscribe on `Newsletter` he will get confirmation on his email.

#### User Stories

- As a user i want to be able to easily register for an account so that i can have a personal account and be able to view my profile.

    - If user press on `My Account` in top right corner an then on `Register` he can easily register for an account.

- As a user i want to be able to easily login or logout so that i can access my personal account information.

    -  If user press on `My Account` in top right corner an then on `Login` or `Logout` he can easily `Login/Logout` for an account.

- As a user i want to be able to easily recover my password in case i forget it so that i can recover access to my account.

    - If user press on `Forgoten Password` on Login page he can easily recover his password in case he forget password.

- As a user i want to be able to receive an email confirmation after registering so that i can verify that my account registration was successful.

    - If user successfuly register for account he will receive confirmation email.

- As a user i want to be able to have a personailzed user profile so that i can view my personal order history and order confirmations, and save my payment information.

    - If user click on `My Account` and then on `My Profile` he will see his personailzed user profile and personal order history and order confirmations.

- As a user i want to be able to read and comment about a product so that i can be informed and inform others about product.

    - If User click on `Blog` he will be able to read and comment about a product and be informed and inform others about product.

#### Bussines Stories

- As a business owner i want to be able to create new product so that i can add new item to my store.

    - If business owner click on `My Account` and then `Product Managment` he will be able to create and add new item to his store.

- As a business owner i want to be able to create and setup new product brand, category, key features, features, specifications and specs so that i can use them when adding product.

    - If business owner click on `My Account` and then `Product Managment` he will be offered to `Add` specific setup.

- As a business owner i want to be able to easily access to product managment so that i can modify products on different way.

    -  If business owner click on `Edit` under specific product he will be able to easily access to product managment and modify products on different way

- As a business owner i want to be able to change item availability so that i can start/stop sale of product.

    - If If business owner click on `Edit` under specific product and under `Available` click on `no` or `unknown` he will be able to start or stop sale of product

- As a business owner i want to be able to display special offers and promotions so that i can increase product sale.

    - If If business owner click on `Edit` under specific product and click on `Select Image` under `Promo Side Banner Left` or `Promo Side Banner right` he will be able to display special offers and promotions.

- As a business owner i want to be able to edit/update a product so that i can change product price, descriptions, image, and other product criteria.

    - If business owner click on `Edit` under specific product he will be able to easily edit/update a product.

- As a business owner i want to be able to delete a record so that i can remove item that are no longer for sale.

    -  If business owner click on `Delete` under specific product he will be able to delete a record or remove item from store.


- Go [Back to Readme](README.md).
