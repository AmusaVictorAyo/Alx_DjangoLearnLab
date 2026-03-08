# Permissions and Groups Setup

This project uses custom permissions on the Book model in the bookshelf app.

## Custom Permissions
The Book model defines these permissions:
- can_view
- can_create
- can_edit
- can_delete

## Groups
Suggested groups:
- Viewers: can_view
- Editors: can_view, can_create, can_edit
- Admins: can_view, can_create, can_edit, can_delete

## Views
The views in `bookshelf/views.py` use Django's `@permission_required` decorator to restrict access:
- `book_list`
- `book_create`
- `book_edit`
- `book_delete`

## Testing
Create users, assign them to groups in Django admin, and verify access to the protected views.