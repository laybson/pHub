'''
Camada de repository do contexto de Orders
'''
from order.models import (
    Order as OrderModel,
    Package as PackageModel,
)

class Order():
    def __init__(self, status):
        self._status = status
    
    def set_status(self, status):
        self._status = status

    def create(order_info) -> OrderProto:
        # Faz a criação e armazenamento do novo pedido
        return order.to_proto()

    def update(update_info) -> OrderProto:
        # Atualiza dados do pedido
        self._status.update(self, update_info)
        return order.to_proto()

# product repository calls