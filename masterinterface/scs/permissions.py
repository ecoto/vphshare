
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator as guard

from functools import wraps

def check_sample_permission(f):
    """ Function decorator mock up
    """
    @wraps(f)
    def decorated(*args, **kwargs):
        return f(*args, **kwargs)
    return decorated
