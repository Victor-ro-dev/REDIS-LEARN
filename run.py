from models.connection.redis_connection import RedisConnectionHandle
from models.redis.redis_repository import RedisRepository
from configs.start_form import start_form

from datetime import datetime

redis_handle = RedisConnectionHandle()
redis_conn = redis_handle.connect()
repository = RedisRepository(redis_conn)


current_data = datetime.now().strftime("%Y-%m-%d")

print(current_data)

repository.insert_hash_ex(current_data, 'banana', 3.12, 40)
repository.insert_hash(current_data, 'apple', 2.34)
repository.insert_hash(current_data, 'uva', 7.34)

hash_items = redis_conn.hgetall(current_data)
print(hash_items)


python_dict = {}

for key, value in hash_items.items():
    python_dict[key.decode('utf-8')] = value.decode('utf-8') 

print(python_dict)
start_form.load_info(python_dict)

value = start_form.get_info('banana')
print(value)