# Pulsar xd

1. ```docker compose up```
2. Убираем с message поле args и запускаем
3. ```./producer.py``` ```./consumer.py```
4. Отправляем несколько сообщений и останавливаем их
5. ```docker exec -it broker bash```
6. обновляем схему ```/pulsar/bin/pulsar-admin namespaces set-schema-compatibility-strategy --compatibility FORWARD_TRANSITIVE public/default```
7. возвращаем args ```message.py```
8. ```./producer.py```
9. ```./consumer.py```
10. отправляем ещё сообщения
11. подтвердим схемы
    ```/pulsar/bin/pulsar-admin schemas get --version 0 persistent://public/default/message-topic```  
    ```/pulsar/bin/pulsar-admin schemas get persistent://public/default/message-topic```  