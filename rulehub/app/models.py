from django.db import models
from djongo import models as djongo_models

class ProductType(models.Model):
    '''
    Representa o tipo de um produto
    '''
    name = models.CharField(max_length=50)

    def to_proto(self) -> ProductProto:
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


class Order(models.Model):
    '''
    Representa um pedido que gerencia produtos e regras
    '''
    customer = models.ForeignKey(Costumer)
    product = models.ForeignKey(Product)

    status = models.CharField(length=3)

    def to_proto(self) -> OrderProto:
        # retorna proto


class Annotation(djongo_models.Model):
    '''
    Representa a anotação de um produto
    '''
    product_type = models.ForeignKey(Product)
    product_type = models.ForeignKey(ProductType)
    rules = djongo_models.ArrayField(
        model_container=djongo_models.EmbeddedModelField(
            Rule,
        )
    )

    def to_proto(self) -> OrderProto:
        # retorna proto



class Rule(djongo_models.Model):
    '''
    Representa a regra a ser anotada em um produto
    '''
    name = models.CharField(max_length=100)
    action = djongo_models.EmbeddedModelField(
        object,
    )
    rules = djongo_models.ArrayField(
        model_container=djongo_models.EmbeddedModelField(
            Rule,
        )
    )
    order_statuses = djongo_models.ArrayField(
        model_container=models.CharField(max_length=50),
    )

    def to_proto(self) -> OrderProto:
        # retorna proto
