# pHub Ops

Este repositório armazena todo o código de infraestrutura do pHub, como por exemplo:

- provisionamento e setup de VMs
- construção de docker images
- lançamento de docker containers
- deploy de código
- deploy de dependências
- instalação de software e setup do ambiente de trabalho local
- outras tarefas administrativas

A maioria dos softwares é executada dentro de docker containers.
O setup local e os servers de prod usarão o docker, exceto softwares stateful, como RabbitMQ, Postgres e Redis, que funcionam melhor com comunicação direta com o OS, fora do isolamento do docker.

O servidor seria construído por meio do Terraform
