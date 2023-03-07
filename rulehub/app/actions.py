'''
Módulo que define e executa as ações
'''
from choicesenum import ChoicesEnum
from order.grpc.ruler import ruler

class Actions(ChoicesEnum):
    SEND_EMAIL = 'send_email', 'Envia email'
    GENERATE_GUIDE = 'generate_guide', 'Gera guia de remessa'
    UPDATE_MEMBERSHIP = 'update_membership', 'Atualiza assinatura'
    ADD_ITEM, = 'add_item', 'Adiciona produto'
    PAY_TO = 'pay_to', 'Faz pagamento para alguém'

    def send_email(order, info):
        # eviar email para destino, com mensagem
        return email

    def generate_guide(order, info):
        # gera guide n vezes
        return guide

    def update_membership(order, info):
        # atualiza assinatura
        return membership
    
    def add_item(order, info):
        # adiciona item ao pedido
        return order
    
    def pay_to(order, info):
        # Pagamento a um destino
        return receipt

    # ... e quantas outras ações genéricas forem necessárias

    def act(
        actions: [RuleActionProto],
        order: Order,
        info: RuleInfoProto
    ) -> ActionsResultsProto:
        try:
            results = {
                action: eval(action)(
                    order,
                    {
                        action_info: actions[action],
                        general_info: info
                    }
                ) for action in actions.keys()
            }
            return results
        except (
            # exceptions
        ) as e:
            raise e

