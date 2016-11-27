try:
    from threading import local
except ImportError:
    from django.utils._threading_local import local

_thread_locals = local()

def get_current_user():
    return getattr(_thread_locals, 'user', None)

def get_current_session():
    return getattr(_thread_locals, 'session', None)

def is_admin_page():
    return getattr(_thread_locals, 'is_admin_page', False)

class ThreadLocals(object):
    """Middleware that gets various objects from the
    request object and saves them in thread local storage."""
    def process_request(self, request):
        _thread_locals.user = getattr(request, 'user', None)
        _thread_locals.session = getattr(request, 'session', None)
        _thread_locals.is_admin_page = \
            (request.path.find("/admin") == 0) # matches admin-api also!
