from .connect_options import connection_options
from redis import Redis

class RedisConnectionHandle:
    def __init__(self):
        self.__host = connection_options["HOST"]
        self.__port = connection_options["PORT"]
        self.__db = connection_options["DB"]
        self.__password = connection_options["PASSWORD"]
        self.__conn = None


    def connect(self) -> Redis:
        if self.__conn is None:
            self.__conn = Redis(
                host=self.__host,
                port=self.__port,
                db=self.__db,
                password=self.__password
            )
            return self.__conn
        
    def get_connection(self) -> Redis:
        return self.__conn