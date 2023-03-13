'''
Módulo que gerencia as regras
'''
class RuleManager():
    def __init__(self, rule):
        self._rule = rule
    
    def set_rule(self, rule):
        self._rule = rule

    def create(rule_info) -> OrderProto:
        # Faz a criação e armazenamento da nova regra
        repository.create_rule(rule_info)
        return new_rule.to_proto()
    
    def update(rule_info) -> OrderProto:
        # Faz a atualização e armazenamento da nova regra
        repository.update_rule(rule_info)
        return rule.to_proto()

    def act(self, order, info):
        self._rule.act(order, info)


class Rule():
    def __init__(self, rule_model):
        self.rule = rule_model
        self.children = [Rule(rule) for rule in rule_model.rules]

    def act(self, order, info):
        result = [
            Actions.act([rule.action], order, info),
            *[Actions.act([child.action], order, info) for child in self.children]
        ]
        return result

    def set_child_rule(self, rule):
        # validações
        # adiciona uma regra filha
        return rules
    
    def set_order_status(self, order):
        # validações
        # adiciona um order status
        return statuses
