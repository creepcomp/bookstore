# Bookstore API

Welcome to the Bookstore API project! This is a Django REST Framework application that provides endpoints for managing books, user login, and book reviews.

## Endpoints

### User Authentication

#### GET /api/login/

**Description:** Endpoint for user login. This endpoint handles user authentication.

**Response:**
- **200 OK:** Successful login, returns user details and authentication token.
- **401 Unauthorized:** Invalid login credentials.

### Books

#### GET /api/book/

**Description:** Retrieve a list of all books available in the bookstore.

**Response:**
- **200 OK:** Returns a list of books with their details.
- **403 Forbidden:** You are not logged in.

#### GET /api/book/suggest/

**Description:** Retrieve a list of suggested books. The suggestion algorithm is based on user preferences and book popularity.

**Response:**
- **200 OK:** Returns a list of suggested books.
- **404 Not Found:** There is not enough data about you.
- **403 Forbidden:** You are not logged in.

### Reviews

#### GET /api/review/

**Description:** Retrieve a list of all reviews for books.

**Response:**
- **200 OK:** Returns a list of reviews with their details.
- **403 Forbidden:** You are not logged in.

#### POST /api/review/

**Description:** Create a new review for a book.

**Request:**
- **Body:** JSON object containing the review details.

**Response:**
- **201 Created:** Review successfully created.
- **400 Bad Request:** Invalid review data.
- **403 Forbidden:** You are not logged in.

#### PUT /api/review/<review_id>/

**Description:** Update an existing review.

**Request:**
- **Body:** JSON object containing the updated review details.

**Response:**
- **200 OK:** Review successfully updated.
- **404 Not Found:** Review not found.
- **400 Bad Request:** Invalid review data.
- **403 Forbidden:** You are not logged in.

#### DELETE /api/review/<review_id>/

**Description:** Delete an existing review.

**Response:**
- **204 No Content:** Review successfully deleted.
- **404 Not Found:** Review not found.
- **403 Forbidden:** You are not logged in.

## Installation

1. Clone the repository:
   ```sh
   git clone https://github.com/creepcomp/bookstore.git
2. Install required packages:
   ```sh
   pip3 install -r requirements.txt
3. Setup PostgreSQL connection (settings.py):
   ```
   DATABASES = {
      'default': {
         'ENGINE': 'django.db.backends.postgresql',
         'HOST': 'localhost',
         'PORT': '5432',
         'NAME': 'bookstore',
         'USER': 'postgres',
         'PASSWORD': '',
      }
   }
4. Migrate Database:
   ```sh
   python3 manage.py makemigration
   python3 manage.py migrate
5. Insert FakeData (Optional):
   ```sh
   python3 insert_fakedata.py
6. Run the application:
   ```sh
   python3 manage.py runserver
