from coreweb import get
from models import User, Blog
import asyncio
import time


@get('/')
@asyncio.coroutine
def index(request):
    summary = 'Lorem ipsum dolor sit amet, consectetur adipisicing elit. Expedita ipsam vero tempore magni nulla consequuntur, iusto fugit optio voluptates error eaque doloremque molestias exercitationem saepe repellendus maiores id. Natus, nostrum.'
    blogs = [
        Blog(id='1', name='Test Blog', summary=summary, created_at=time.time() - 120),
        Blog(id='2', name='Something New', summary=summary, created_at=time.time() - 3600),
        Blog(id='3', name='Learn Swift', summary=summary, created_at=time.time() - 7200)
    ]
    return {
        '__template__': 'blogs.html',
        'users': blogs
    }
