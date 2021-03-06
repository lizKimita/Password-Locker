# Password-Locker Application

#### This is an application that provides a centralised place where users can store their login credentials for all their accounts in one place. 2019

#### By **Elizabeth Wanjiku Kimita**

## Description
The application makes it easy for users with many accounts to keep track of their login details; i.e the platform, the login username and the password to access their accounts. Users are able to store all these details in a centralised place and have access to them whenever they want. Users can save their details, display all their saved accounts with their individual details, delete unneccesary accounts and search for specific accounts among what has already been saved.

## Application Specifications
* A user first runs the application on the terminal using the command: python3.6 run.py
* They will receive a welcome message asking for their name.
* After the name they will be directed to a section where they need to choose whether they want to create an account, login or exit the application.
* depending on what they choose they will be directed to a new path.
* If they choose to create an account, they will be required to enter the neccesary details to create a new account.
* If they selected login, then they will be prompted to enter their username and password which will then be verified to determine if they already have an account. If they do have an account, they proceed to the page where they can create their account credentials.If they do not have an account then they will be required to create a new account.
* After successfully creating their accounts/ logging in, users are then able to create credentials for the accounts that they would like to save.
* One can view their saved accounts and even has the ability to search for a specific saved account by using the account platform name.
* When users are done saving their credentials they can then use a short-code and exit the application.


## Testing the Application
To test the credentials and user files I used: 
* User Class - python3.6 user-test.py
* Credentials Class - python3.6 credentials-test.py

## Known Bugs
There are currently no known bugs

## Technologies Used
Python3.6

## Support and contact details
For more information, questions, or help using the program, get in touch with me on +254 726 047102 or email: kimita.wanjiku@gmail.com.

### License
  
MIT License

Copyright (c) 2019 Elizabeth Kimita

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sub-license, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NON-INFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
