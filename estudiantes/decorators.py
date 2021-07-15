from django.contrib.auth.decorators import user_passes_test


def admin_required(func=None, redirect_field_name='next', login_url=None):
    actual_decorator = user_passes_test(
        lambda u: u.is_admin,
        login_url=login_url,
        redirect_field_name=redirect_field_name
    )
    if func:
        return actual_decorator(func)
    return actual_decorator


def profesor_required(func=None, redirect_field_name='next', login_url=None):
    actual_decorator = user_passes_test(
        lambda u: u.is_teacher,
        login_url=login_url,
        redirect_field_name=redirect_field_name
    )
    if func:
        return actual_decorator(func)
    return actual_decorator
