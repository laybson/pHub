'''
Camada de services
'''
from abc import ABC, abstractmethod
from repository import (
    Order,
    Product
)
from order.order_statuses import OrderStatuses

class OrderService:
    @classmethod
    def create_order(cls, request: OrderRequest) -> OrderResponse:
        # Parse da request e validações
        order = Order.create(order_info)
        return OrderResponse(order=order)
    
    @classmethod
    def update_order(cls, request: UpdateOrderRequest) -> UpdateOrderResponse:
        # Parse da request e validações
        status = OrderStatuses.get(request.status).handler()
        order = Order(status).update(update_info)
        return UpdateOrderResponse(order=order)


class RuleService:
    @classmethod
    def get_or_create_rule(cls, rule_info) -> GetOrCreateRuleResponse:
        # Parse da request e validações
        try:
            rule = get_or_create(rule_info)
            # gRpc Call para criação ou leitura de regra no serviço rulehub
        except RpcError as e:
            raise e
        return GetOrCreateRuleResponse(rule=rule)

# product services
