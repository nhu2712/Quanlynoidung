from functools import wraps
from django.shortcuts import get_object_or_404
from django.http import Http404
from django.utils.translation import gettext_lazy as _
from .models import Employee


def check_employee_permission(required_permissions):
    """
    A decorator to check if the current employee's permission is in the required permissions list.

    :param required_permissions: A list of permissions to check against.
    """
    def decorator(view_func):
        @wraps(view_func)
        def _wrapped_view(request, *args, **kwargs):
            # Get the employee instance for the current user
            try:
                employee = get_object_or_404(Employee, user=request.user)
            except AttributeError:
                # If the user is not associated with an Employee, raise 404
                raise Http404(
                    _("Employee record not found for the current user."))

            # Check if the employee's permission is in the list of required permissions
            if employee.permission not in required_permissions:
                raise Http404(
                    _("You do not have permission to access this page."))

            # If permission is valid, proceed with the original view
            return view_func(request, *args, **kwargs)

        return _wrapped_view

    return decorator
