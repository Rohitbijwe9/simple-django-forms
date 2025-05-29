# Django Form Validation Project

A simple Django project demonstrating form handling with validation, session storage, and user-friendly redirection.

##  Features

- Clean and validated user input using Django Forms  
- Form submission with GET and POST methods  
- Session-based data handling  
- Page redirection after successful form submission  
- Basic HTML styling for a better user experience  

##  Project Flow

1. User visits the form page at `/userform/`.  
2. User fills the form with **first name**, **last name**, **email**, and **mobile number**.  
3. On form submission (POST):  
   - Django validates the form data.  
   - If valid, the data is stored in the session.  
   - User is redirected to `/showuser/`.  
4. At `/showuser/`, the submitted data is displayed to the user.  
5. The session data is cleared after displaying to avoid resubmission on page refresh.  
