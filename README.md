# Crowd-Funding
Crowdfunding is the practice of funding a project or venture by raising small
amounts of money from a large number of people, typically via the Internet.
Crowdfunding is a form of crowdsourcing and alternative finance. In 2015,
over US$34 billion was raised worldwide by crowdfunding.
## Installation
#### 1- activate env 
In Linux/Mac, go to the project folder (in which, there should be env folder created).
```bash
source env/bin/activate
```
In Windows, go to the project folder (in which, there should be env folder created).
```bash
env\Scripts\activate
```
#### 2-Use the package manager [pip](https://pip.pypa.io/en/stable/) to install
```bash
Pip install pillow
Pip install Django-allauth
```
#### 3-runserver 
```bash
python manage.py runserver
```
# Deployment 
[Http://127.0.0.1:8000/](http://127.0.0.1:8000/)
### 1- Home page 
- A Navbar and Footer
- A slider to show the highest five rated running projects to encourage
users to donate
- List of the latest 5 projects
- List of latest 5 featured projects (which are selected by the admin)
- A list of the categories. User can open each category to view its
projects
- Search bar that enables users to search projects by title or tag
### 2- Authentication System
- Registration
  - First name
  - Last name
  - Email
  - Password
  - Confirm password
  - Mobile phone [validated against Egyptian phone numbers]
  - Profile Picture
  - Activation Email after registration
  - Once the user register he should receive an email with the
  activation link. The user shouldn’t be able to login without
  activation. The activation link should expire after 24 hours.

- Login
  - The user should be able to login after activation using his email
  and password
  - Bonus: Allow users to login with facebook account
  - Forgot Password (Bonus)
  - The user should have an option to reset his password if he
  forgot it to receive a password reset link to his email
- User Profile, The user can view his profile which:
  - He can view his profile
  - He can view his projects
  - He can view his donations
  - He can  verify his email
  - He can edit all his data except for the email
  - He can have extra optional info other than the info he added
  while registration (Birthdate, facebook profile, country)
  - User can delete his account (Note that there must be a
  confirmation message before deleting)
  - Bonus: User must enter his password to delete his account  

### 3 - Projects:
  - The user can create a project fund raise campaign which contains:
  - Title
  - Details
  - Category (from list of categories added previously by admins)
  - Multiple pictures
  - Total target (i.e 250000 EGP)
  - Multiple Tags
  - Set start/end time for the campaign
  - Users can view any project and donate to the total target
  - Users can add comments on the projects
  - Bonus: Comments can have replies
  - Users can report inappropriate projects
  - Users can report inappropriate comments
  - Users can rate the projects
  - Project creator can cancel the project if the donations are less than
  25% of the target
  - Project page should show the overall average rating of the project
  - Project page should show the project pictures in a slider
  - Project page should show 4 other similar projects based on project
  tags

## Support
you can contact us using social media icon or email or phone number that found in footer


