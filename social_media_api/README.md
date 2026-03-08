# Social Media API

A Django REST Framework based Social Media API with custom user authentication, token-based login, and user profile management.

## Project Overview

This project sets up the foundation for a social media backend API. It includes:

- A custom user model
- User registration
- User login
- Token authentication
- User profile management

## Custom User Model

The project uses a custom user model named `CustomUser` that extends Django’s `AbstractUser`.

### Extra fields added

- `bio`: stores a short user biography
- `profile_picture`: stores the user’s profile image
- `followers`: a self-referencing many-to-many relationship that allows users to follow other users

Example:

```python
class CustomUser(AbstractUser):
    bio = models.TextField(blank=True, null=True)
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True, null=True)
    followers = models.ManyToManyField('self', symmetrical=False, related_name='following', blank=True)