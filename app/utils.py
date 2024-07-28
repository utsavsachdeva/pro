from functools import wraps
from flask import abort, flash, redirect, url_for
from flask_login import current_user

def admin_required(func):
    """Decorator to restrict access to admin-only views."""
    @wraps(func)
    def decorated_view(*args, **kwargs):
        if not current_user.is_authenticated or current_user.role != 'admin':
            flash('You do not have permission to access this page.', 'danger')
            return redirect(url_for('auth.login'))  # Redirect to login page
        return func(*args, **kwargs)
    return decorated_view


def sponsor_required(func):
    """Decorator to restrict access to sponsor-only views."""
    @wraps(func)
    def decorated_view(*args, **kwargs):
        if not current_user.is_authenticated or current_user.role != 'sponsor':
            flash('You do not have permission to access this page.', 'danger')
            return redirect(url_for('auth.login'))  # Redirect to login page
        return func(*args, **kwargs)
    return decorated_view


# Other utility functions (optional)
def flash_errors(form):
    """Flashes form errors to the user."""
    for field, errors in form.errors.items():
        for error in errors:
            flash(f"Error in the {getattr(form, field).label.text} field - {error}", 'danger')
