# Django Celery Study Repository

### README

- django Celery Study Repository

### Docker Compose

- rabbitmq는 관리를 위한 rabbitmq-management를 사용하기로 함
- rabiitmq-management: 15672

```yml
    version: '3'
    services:
      db:
        ports:
          - "9901:3306"
        expose:
          - "9901"
        build:
          context: .
        platform: linux/amd64  # mac에서 compose 할 경우 주석 해제 한 후 사용할 것
      rabbitmq:
        image: 'rabbitmq:3-management'
        container_name: 'my-rabbit'
        ports:
          - "5672:5672"
        environment:
          RABBITMQ_DEFAULT_USER: "root"
          RABBITMQ_DEFAULT_PASS: "1234"
   ```


