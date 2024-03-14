## Работа с MongoDB



Для знакомства с настройками MongoDB настраиваем Docker, а именно используем `docker-compose.yml`:

```
# Use root/example as user/password credentials
version: '3.8'

services:

  mongo:
    image: mongo
    restart: always
    ports:
      - 27017:27017
    environment:
      MONGO_INITDB_ROOT_USERNAME: root
      MONGO_INITDB_ROOT_PASSWORD: example

  mongo-express:
    image: mongo-express
    restart: always
    ports:
      - 8081:8081
    environment:
      ME_CONFIG_MONGODB_ADMINUSERNAME: root
      ME_CONFIG_MONGODB_ADMINPASSWORD: example
      ME_CONFIG_MONGODB_URL: mongodb://root:example@mongo:27017/
```


Далее запускаем докер через: `docker-compose up -d`

![alt text](/data/docker-compose-up.png) 


После выполнения видим, что образ появился в docker:

![alt text](/data/docker-success.png)


Как вариант можем теперь использовать для работы с БД - MongoDB Compass и вручную загрузить используемый датасет и работать с ним, но будем работать через python:

[Скипт с загрузкой базы данных и запросами](/data/mongoDB_script.py)


Если кратко, то в скрипте мы:
1. Подключаемся к настроенной базе данных
2. Удаляем старые данные, если существовали
3. Читаем данные из csv файла и загружаем их в бд
4. Делаем запросы на выборку (первый класс, определенный человек, выжившие мужчины)
5. Запросы на обновление (конкретный человек выжил, повышение класса в зависимости от тарифа)
6. Запросы на удаление (конкретный человек, погибшие, несовершеннолетние)
7. Сравнение производительности запросов выборки в зависимости от существования индекса (индекс на тариф)