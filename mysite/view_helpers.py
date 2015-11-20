# view_helpers.py
# 
# Contains functions that are imported by views.py modules

from django.shortcuts import render


def multipurpose(request, title, subtitle=None, is_safe=False, 
                 show_back=False, show_reload=False):
    """Multipurpose page
    
    Copied from here:
        ~/progs/pts_git/pts/mysite/view_helpers.py
    
    is_safe: If True --> It is safe to render HTML in the subtitle.
             If False --> Escape all HTML in the subtitle.
    
    show_back:      Should we display a large 'Back' button?
    
    show_reload:    Should we display a large 'Reload' button?
                    The reload button reloads the page via GET, never POST.
    
    Use show_reload if the URL has not changed, and thus the back button would send you back two pages, not just one.
    
    NOTE: In Firefox 38.0.1 on 2015-05-28, the 'Back' button does the correct thing even in the case of a POST request to the same URL. That is to say, the 'Back' button does NOT change the URL. I am not sure whether this can be relied upon, it is probably best to use show_reload when we are reloading a POSTed page.
    
    """
    
    if subtitle == None:
        subtitle = title + '.'
    
    return render(request, 'hfcd/multipurpose.html', {
        'user': request.user,
        'page_title': title,
        'subtitle': subtitle,
        'is_safe': is_safe,
        'show_back': show_back,
        'show_reload': show_reload,
    })
