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

## Posts and Comments Endpoints

### Posts
- `GET /posts/` - List all posts
- `POST /posts/` - Create a new post
- `GET /posts/<id>/` - Retrieve a single post
- `PUT /posts/<id>/` - Update a post
- `PATCH /posts/<id>/` - Partially update a post
- `DELETE /posts/<id>/` - Delete a post

### Comments
- `GET /comments/` - List all comments
- `POST /comments/` - Create a new comment
- `GET /comments/<id>/` - Retrieve a single comment
- `PUT /comments/<id>/` - Update a comment
- `PATCH /comments/<id>/` - Partially update a comment
- `DELETE /comments/<id>/` - Delete a comment

## Permissions
Users can create posts and comments when authenticated.
Users can only edit or delete their own posts and comments.

## Search
Posts can be searched by title or content using query parameters:

```bash
/posts/?search=django