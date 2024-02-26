from django.core.exceptions import PermissionDenied


def superuser_only(function):
    """Только для администраторов"""

    def _inner(request, *args, **kwargs):
        if not request.user.is_superuser:
            raise PermissionDenied
        return function(request, *args, **kwargs)
    return _inner
