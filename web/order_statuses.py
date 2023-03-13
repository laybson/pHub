from abc import ABC, abstractmethod
from choicesenum import ChoicesEnum
from order.grpc.ruler import ruler

'''
Representa os possíveis status dos pedidos
'''
class OrderStatuses(ChoicesEnum):
    ORDERED = 'ord', 'Pedid realizado'
    PAID_OUT = 'pay', 'Pedido pago'
    MEMBERSHIP = 'mem', 'Assinado'
    MEMBERSHIP_BASIC, = 'msb', 'Assinante Básico'
    MAMBERSHIP_PREMIUM = 'msp', 'Assinante Premium'

    def handler(self, order):
        mapping = {
            OrderStatuses.ORDERED: Ordered,
            OrderStatuses.PAID_OUT: PaidOut,
            OrderStatuses.MEMBERSHIP: Membership,
            OrderStatuses.MEMBERSHIP_BASIC: MembershipBasic,
            OrderStatuses.MAMBERSHIP_PREMIUM: MembershipPremium,
        }
        return mapping.get(self)


class OrderStatus(ABC):
    @abstractmethod
    def update(self, order):
        pass


class Ordered(OrderStatus):
    @ruler(order)
    def update(self, order):
        # transforma status em pago ou cancelado
        return status
    
    def pay(self, order):
        # set pago
        return update(paid_order)
    
    def cancelado(self, order):
        # set cancelado
        return update(canceled_order)


class PaidOut(OrderStatus):
    @ruler(order)
    def update(self, order):
        # transforma status em pago
        return status
    
    def undo(self, order):
        # desfaz pagamento
        return update(canceled_order)


class Membership(PaidOut):
    @ruler(order, info)
    def update(self, order):
        # transforma status membro
        return status
    
    def undo(self, order):
        # desfaz pagamento
        return update(canceled_order)
    
    def change_membership(self, order):
        # muda assinatura
        return update(new_membership_order)


class MembershipBasic(Membership):
    @ruler(order)
    def update(self, order):
        # transforma status membro basic
        return status

    def undo(self, order):
        # desfaz pagamento de membro
        return update(canceled_order)

    def change_membership(self, order):
        # muda assinatura
        return update(new_membership_order)


class MembershipPremium(Membership):
    @ruler(order)
    def update(self, order):
        # transforma status membro premium
        return status

    def undo(self, order):
        # desfaz pagamento de membro
        return update(canceled_order)

    def change_membership(self, order):
        # muda assinatura
        return update(new_membership_order)
