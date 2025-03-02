import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
django.setup()

from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from api.models import Book, Review

def insert_users():
    users = [
        ('user1', 'password1'),
        ('user2', 'password2'),
        ('user3', 'password3'),
        ('user4', 'password4'),
        ('user5', 'password5'),
    ]

    for username, password in users:
        user = User.objects.create_user(username, password)
        user.save()

def insert_books():
    books = [
        ('Book A1', 'Author 1', 'Adventure'),
        ('Book A2', 'Author 1', 'Mystery'),
        ('Book A3', 'Author 1', 'Science Fiction'),
        ('Book B1', 'Author 2', 'History'),
        ('Book B2', 'Author 2', 'Romance'),
        ('Book B3', 'Author 2', 'Science'),
        ('Book C1', 'Author 3', 'Cooking'),
        ('Book C2', 'Author 3', 'Gardening'),
        ('Book C3', 'Author 3', 'Travel'),
        ('Book D1', 'Author 4', 'Adventure'),
        ('Book D2', 'Author 4', 'Adventure'),
        ('Book D3', 'Author 4', 'Adventure'),
        ('Book E1', 'Author 5', 'Mystery'),
        ('Book E2', 'Author 5', 'Mystery'),
        ('Book E3', 'Author 5', 'Mystery'),
        ('Book F1', 'Author 6', 'Science'),
        ('Book F2', 'Author 7', 'History'),
        ('Book F3', 'Author 8', 'Romance'),
        ('Book F4', 'Author 9', 'Science Fiction'),
        ('Book F5', 'Author 10', 'Cooking'),
        ('Book F6', 'Author 11', 'Gardening'),
        ('Book F7', 'Author 12', 'Travel'),
        ('Book F8', 'Author 13', 'Education'),
        ('Book F9', 'Author 14', 'Horror'),
        ('Book F10', 'Author 15', 'Adventure'),
        ('Book F11', 'Author 16', 'Mystery'),
        ('Book F12', 'Author 17', 'Science'),
        ('Book F13', 'Author 18', 'History'),
        ('Book F14', 'Author 19', 'Romance'),
        ('Book F15', 'Author 20', 'Science Fiction'),
        ('Book F16', 'Author 21', 'Cooking'),
        ('Book F17', 'Author 22', 'Gardening'),
        ('Book F18', 'Author 23', 'Travel'),
        ('Book F19', 'Author 24', 'Education'),
        ('Book F20', 'Author 25', 'Horror'),
        ('Book F21', 'Author 6', 'Romance'),
        ('Book F22', 'Author 7', 'Adventure'),
        ('Book F23', 'Author 8', 'Mystery'),
        ('Book F24', 'Author 9', 'Science'),
        ('Book F25', 'Author 10', 'History'),
        ('Book F26', 'Author 11', 'Romance'),
        ('Book F27', 'Author 12', 'Science Fiction'),
        ('Book F28', 'Author 13', 'Cooking'),
        ('Book F29', 'Author 14', 'Gardening'),
        ('Book F30', 'Author 15', 'Travel'),
        ('Book F31', 'Author 16', 'Education'),
        ('Book F32', 'Author 17', 'Horror'),
        ('Book F33', 'Author 18', 'Adventure'),
        ('Book F34', 'Author 19', 'Mystery'),
        ('Book F35', 'Author 20', 'Science'),
        ('Book F36', 'Author 21', 'History'),
        ('Book F37', 'Author 22', 'Romance'),
        ('Book F38', 'Author 23', 'Science Fiction'),
        ('Book F39', 'Author 24', 'Cooking'),
        ('Book F40', 'Author 25', 'Gardening'),
        ('Book F41', 'Author 6', 'Travel'),
        ('Book F42', 'Author 7', 'Education'),
        ('Book F43', 'Author 8', 'Horror'),
        ('Book F44', 'Author 9', 'Adventure'),
        ('Book F45', 'Author 10', 'Mystery'),
        ('Book F46', 'Author 11', 'Science'),
        ('Book F47', 'Author 12', 'History'),
        ('Book F48', 'Author 13', 'Romance'),
        ('Book F49', 'Author 14', 'Science Fiction'),
        ('Book F50', 'Author 15', 'Cooking')
    ]

    for title, author, genre in books:
        Book.objects.create(title, author, genre)

def insert_reviews():
    reviews = [
        (1, 1, 5),
        (2, 1, 4),
        (3, 1, 3),
        (4, 1, 5),
        (5, 1, 2),
        (6, 1, 4),
        (7, 1, 5),
        (8, 1, 3),
        (9, 1, 4),
        (10, 1, 5),
        (11, 2, 3),
        (12, 2, 4),
        (13, 2, 5),
        (14, 2, 2),
        (15, 2, 4),
        (16, 2, 5),
        (17, 2, 3),
        (18, 2, 4),
        (19, 2, 5),
        (20, 2, 2),
        (21, 3, 4),
        (22, 3, 5),
        (23, 3, 3),
        (24, 3, 4),
        (25, 3, 5),
        (26, 3, 2),
        (27, 3, 4),
        (28, 3, 5),
        (29, 3, 3),
        (30, 3, 4),
        (31, 4, 5),
        (32, 4, 2),
        (33, 4, 4),
        (34, 4, 5),
        (35, 4, 3),
        (36, 4, 4),
        (37, 4, 5),
        (38, 4, 2),
        (39, 4, 4),
        (40, 4, 5),
        (41, 5, 3),
        (42, 5, 4),
        (43, 5, 5),
        (44, 5, 2),
        (45, 5, 4),
        (46, 5, 5),
        (47, 5, 3),
        (48, 5, 4),
        (49, 5, 5),
        (50, 5, 2),
        (1, 2, 4),
        (2, 3, 5),
        (3, 4, 3),
        (4, 5, 4),
        (5, 2, 5),
        (6, 3, 3),
        (7, 4, 4),
        (8, 5, 5),
        (9, 3, 2),
        (10, 2, 4),
        (11, 3, 5),
        (12, 4, 3),
        (13, 5, 4),
        (14, 3, 5),
        (15, 4, 3),
        (16, 5, 4),
        (17, 1, 5),
        (18, 4, 2),
        (19, 5, 4),
        (20, 1, 5)
    ]

    for book, user, rating in reviews:
        user = User.objects.get(id=user)
        book = Book.objects.get(id=book)
        Review.objects.create(user=user, book=book, rating=rating)

    print("All records inserted to database.")

if __name__ == "__main__":
    insert_users()
    insert_books()
    insert_reviews()
