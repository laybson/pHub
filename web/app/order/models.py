'''
Define os modelos de dados para a aplicação.
'''
from django.db import models

class Costumer(models.Model):
    '''
    Representa um usuário que realiza um pedido
    '''
    name = models.CharField(max_length=50)

    def to_proto(self) -> CostumerProto:
        # retorna proto


class Admin(models.Model):
    '''
    Representa um usuário que gerencia produtos e regras
    '''
    name = models.CharField(max_length=50)

    def to_proto(self) -> AdminProto:
        # retorna proto


class Order(models.Model):
    '''
    Representa um pedido que gerencia produtos e regras
    '''
    customer = models.ForeignKey(Costumer)
    product = models.ForeignKey(Product)

    status = models.CharField(length=3)

    def to_proto(self) -> OrderProto:
        # retorna proto


class Product(models.Model):
    '''
    Representa um produto
    '''
    name = models.CharField(max_length=50)

    admin = models.ForeignKey(Admin)
    product_type = models.ForeignKey(ProductType)

    status = models.CharField(length=3)

    metadata = PostgresJSONField()

    def to_proto(self) -> ProductProto:
        # retorna proto
