from redis import Redis

class RedisRepository:
    def __init__(self, redis_connection: Redis) -> None:
        self.__redis_connection = redis_connection

    def insert(self, key: str, value: str) -> None:
        self.__redis_connection.set(key, value)

    def get(self, key: str) -> str:
        value = self.__redis_connection.get(key)
        return value.decode('utf-8')
    
    def insert_hash(self, hash_name: str, field: str, value: str) -> None:
        self.__redis_connection.hset(hash_name, field, value)

    def get_hash(self, hash_name: str, field: str) -> str:
        value = self.__redis_connection.hget(hash_name, field)
        return value.decode('utf-8') if value else None

    def insert_ex(self, key: str, value: str, ex: int) -> None:
        self.__redis_connection.set(key, value, ex=ex)

    def insert_hash_ex(self, hash_name: str, field: str, value: str, ex: int) -> None:
        self.__redis_connection.hset(hash_name, field, value)
        self.__redis_connection.expire(hash_name, ex)
