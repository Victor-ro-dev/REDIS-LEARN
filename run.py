from models.connection.redis_connection import RedisConnectionHandle
from models.redis_repository import RedisRepository


redis_handle = RedisConnectionHandle()
redis_conn = redis_handle.connect()
repository = RedisRepository(redis_conn)
repository.insert('user:name', 'John Doe')
repository.insert('user:email', 'john.doe@example.com')


