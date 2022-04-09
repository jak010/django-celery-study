import pika


class Publisher:
    def __init__(self):
        self.__url = "127.0.0.1"
        self.__port = 5672
        self.__vhost = "/vhost-1"
        self.__cred = pika.PlainCredentials(
            "root", "1234"
        )
        self.__queue = "test1"

    def main(self):
        conn = pika.BlockingConnection(
            pika.ConnectionParameters(
                self.__url,
                self.__port,
                self.__vhost,
                self.__cred
            )
        )
        channel = conn.channel()
        channel.basic_publish(
            exchange="",
            routing_key=self.__queue,
            body=b"Hello Queue"
        )
        channel.close()


if __name__ == '__main__':
    pub = Publisher()
    from time import sleep
    for idx in range(1, 1000000):
        sleep(1)
        print(idx)
        pub.main()
