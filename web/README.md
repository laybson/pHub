# pHub Web

Este repositório contém o backend da aplicação, baseado em Python com Django.

Servido tanto usando uWSGI, provendo uma API para ser consumida pelos outros serviços, quanto sob um worker Celery assíncrono que consome tasks em uma fila.

A aplicação pode agendar tasks para serem processadas assincronamente usando o framework Celery, podendo enfileirar tarefas no RabbitMQ para serem consumidas posteriormente por um worker assíncrono. Os resultados das tarefas são armazenados no Redis.

O seu armazenamento principal em DB relacional PostgreSQL, gerenciado pelo Django ORM e por Django migrations. Ele também usa o armazenamento Redis para acessos rápidos em memória como cache e dados efêmeros.

Possui também uma solução de Feature flags usando Unleash.

Comunica-se com clientes internos por meio de APIs grpc, e com clientes externos com APIs Rest intermediadas por protocol buffers.
