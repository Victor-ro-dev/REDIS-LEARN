from models.connection.redis_connection import RedisConnectionHandle
from models.redis_repository import RedisRepository

from datetime import datetime

redis_handle = RedisConnectionHandle()
redis_conn = redis_handle.connect()
repository = RedisRepository(redis_conn)


current_data = datetime.now().strftime("%Y-%m-%d")

print(current_data)

repository.insert_hash_ex(current_data, 'banana', 3.12, 40)
repository.insert_hash(current_data, 'apple', 2.34)
repository.insert_hash(current_data, 'uva', 7.34)