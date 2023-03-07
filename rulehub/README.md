# rulehub

Este repositório contém o microserviço de gerenciamento e execução de regras no phub.

A aplicação usa Python com Django, com armazenamento em MongoDB.

Regras são modelos de dados com uma ação intrínseca, e que podem conter outras regras. Essa ação define um comportamento, com seus própios parâmetros, que deve ser executado no momento de troca de estado de um pedido.

A ação é executada com a chamada da função generalista que tem o seu nome. A combinação da ação da regra com as das suas regras filhas, podem produzir um sem número de possibilidades de comportamentos distintos.  

As regras podem ser vinculadas a produtos ou tipos de produto através da criação de anotações.
