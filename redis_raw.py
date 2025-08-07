"""
Comando Redis Básicos
"""

import redis 

redis_conn = redis.Redis(host='redis-18063.crce196.sa-east-1-2.ec2.redns.redis-cloud.com',password="8ka9H0iv0v4jdvh1QiRaaLsbEIkMnBZQ" , port=18063, db=0)


redis_conn.hset('user', 'name', 'John Doe')
redis_conn.hset('user', 'email', 'john.doe@example.com')
redis_conn.delete('chave_1')

nome = redis_conn.hget('user', 'name').decode('utf-8')
email = redis_conn.hget('user', 'email').decode('utf-8')
redis_conn.hdel('user', 'age')

key = redis_conn.exists('chave_1')
field_key = redis_conn.hexists('user', 'name')

print(f"Chave 'chave_1' existe: {field_key}")

print(f"Chave 'user' existe: {key}")

print(f"Nome: {nome}")
print(f"Email: {email}")
