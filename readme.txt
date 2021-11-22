
This app uses django version == 2.2
this application uses various users ie customer, seller and customer care agent
The Home page can be found at 127.0.0.1:8000 for the customer
registration for the customer is found at 127.0.0.1:8000/user_profiles/register-customer
registration for seller at 127.0.0.1:8000/seller/register-seller
registration for agent at 127.0.0.1:8000/user_profiles/register-agent
The payment gateway used is MTN-momo API but can be integrated with other like paypal, M-Pesa and others

Also the seller page is to be updated to show only products sold in a given period of time for example today for better statistics
This app uses redis-server and django channels to support the chat functionality and has been fully tested on linux 
for windows users 'try your luck'
Database configuration has been done with Mysql database 
TODO's 

Better Frontend
Adding credit cart payments like paypal

Requirements
Django channels 
pillow #To handle image uploads
django auth# for authentication
