from models import User
import asyncio
import orm


@asyncio.coroutine
def test(loop):
    yield from orm.create_pool(loop=loop, user='www-data', password='www-data', db='awesome')
    u = User(name='Test', email='test@example.com',
             passwd='123', image='about:blank')
    # pdb.set_trace()
    yield from u.save()


loop = asyncio.get_event_loop()
loop.run_until_complete(test(loop))
for x in test(loop):
    pass
loop.close()
