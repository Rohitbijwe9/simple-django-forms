# Django Form Validation & Calculator Project

A simple Django project demonstrating form handling with validation, session storage, redirection, and a calculator application using Django Forms.

---

## Features

- **Form Validation**
  - Clean and validated user input using Django Forms
  - Form submission with GET and POST methods
  - Session-based data handling
  - Page redirection after successful form submission
  - Basic HTML styling for better user experience

- **Calculator (Calcy App)**
  - Simple calculator built with Django Forms
  - Supports operations: Addition, Subtraction, Multiplication, Division
  - Displays the result instantly on the same page
  - Input validation with error handling (e.g., divide by zero)

---

## Project Flow

### 1. Form Validation App (`userform`)
1. User visits the form page at `/userform/`
2. User fills the form with:
   - First Name
   - Last Name
   - Email
   - Mobile Number
3. On form submission (POST):
   - Django validates the input
   - If valid, data is stored in the session
   - User is redirected to `/showuser/`
4. At `/showuser/`, the submitted data is displayed
5. Session data is cleared after display to prevent resubmission

---

### 2. Calculator App (`calcy`)
1. User visits the calculator page at `/calcy/`
2. User enters two numbers and selects an operation:
   - `+` Addition
   - `-` Subtraction
   - `*` Multiplication
   - `/` Division
3. On submission:
   - Inputs are validated
   - The selected operation is performed
   - Result is shown on the same page
4. Handles invalid operations and zero division gracefully

---

## Setup Instructions

1. Clone the repository:
   ```bash
   git clone https://github.com/Rohitbijwe9/Django-Form-validation.git
