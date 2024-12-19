from .models import EmployeePermission


def get_permission_context_by_permission(permission: EmployeePermission):
    """
    Return a dictionary containing the context for the permission.

    :param permission: The permission to get the context for.
    """
    manage_user_permission_list = [EmployeePermission.ADMIN]
    manage_room_permission_list = [
        EmployeePermission.ADMIN, EmployeePermission.CONTENT_MANAGER, EmployeePermission.EDITOR]
    manage_service_permission_list = [
        EmployeePermission.ADMIN, EmployeePermission.CONTENT_MANAGER, EmployeePermission.EDITOR]
    manage_voucher_permission_list = [
        EmployeePermission.ADMIN, EmployeePermission.CONTENT_MANAGER, EmployeePermission.EDITOR]
    approve_blog_permission_list = [
        EmployeePermission.ADMIN, EmployeePermission.CONTENT_MANAGER]
    edit_blog_permission_list = [
        EmployeePermission.ADMIN, EmployeePermission.CONTENT_MANAGER]
    manage_blog_permission_list = [
        EmployeePermission.ADMIN, EmployeePermission.CONTENT_MANAGER, EmployeePermission.EDITOR]

    context = {
        'can_manage_user_permission': permission in manage_user_permission_list,
        'can_manage_room_permission': permission in manage_room_permission_list,
        'can_manage_service_permission': permission in manage_service_permission_list,
        'can_manage_voucher_permission': permission in manage_voucher_permission_list,
        'can_approve_blog_permission': permission in approve_blog_permission_list,
        'can_edit_blog_permission': permission in edit_blog_permission_list,
        'can_manage_blog_permission': permission in manage_blog_permission_list,
    }

    return context
