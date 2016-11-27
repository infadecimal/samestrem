from django import http


class FilterPersistMiddleware(object):
    """
    Remember and apply saved list filter on list view
    """

    def process_request(self, request):
        if '/admin/' not in request.path or request.method == 'POST' \
                or 'jsi18n' in request.path:
            return None

        referrer = request.META.get('HTTP_REFERER')

        if referrer:
            # referred from somewhere not admin? remove referrer
            if 'google.com' in referrer:
                referrer = ''
            else:
                referrer = request.META['HTTP_REFERER'].split('?')[0]
                referrer = referrer[referrer.find('/admin'):len(referrer)]
        else:
            referrer = u''

        popup = 'pop=1' in request.META['QUERY_STRING']
        path = request.path
        query_string = request.META['QUERY_STRING']
        session = request.session
        
        if session.get('redirected', False):#so that we dont loop once redirected
            del session['redirected']
            return None

        key = 'key'+path.replace('/','_')
        if popup:
            key = 'popup'+key

        if path == referrer: 
            """ We are in the same page as before. We assume that filters were
                changed and update them. """
            if query_string == '': #Filter is empty, delete it
                if session.has_key(key):
                    del session[key]
                return None
            else:
                request.session[key] = query_string
        else: 
            """ We are are coming from another page. Set querystring to
                saved or default value. """
            if query_string and not referrer:
                request.session[key] = query_string
            else:
                query_string=session.get(key, '')
            if query_string is not None:
                redirect_to = path+'?'+query_string
                request.session['redirected'] = True
                return http.HttpResponseRedirect(redirect_to)
            else:
                return None
