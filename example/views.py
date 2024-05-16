# example/views.py
from datetime import datetime

from django.http import HttpResponse

def index(request):
    now = datetime.now()
    html = f'''
    <html>
        <body>
            <h1>Hello from Mashhad!</h1>
            <p>This is an example of Django project.</p>
            <p>The current time is { now }.</p>
        </body>
    </html>
    '''
    return HttpResponse(html)
