from app.rule_manager import RuleManager
from app import repository

class RuleService:
    @classmethod
    def ruler(cls, order, info):
        # Serviço chamado na troca de status para realizar ações de regras
        package = order.package
        rules = Set(
            repository.get_rules_by_package(package) +
            repository.get_rules_by_package_type(package.type)
        )
        results = [
            RuleManager(Rule(rule)).act(order, info) for rule in rules
        ]
        return results
    
    # rule crud

class AnnotationService:
    @classmethod
    def annotate(cls, package, package_type, rules):
        # cria anotação
        # validações
        annotation = repository.annotate(package, package_type, rules)
        return annotation

    @classmethod
    def add_rules(cls, info):
        # adiciona regras a uma anotação existente
        # validações
        return annotation
    
    @classmethod
    def remove_rules(cls, info):
        # adiciona regras de uma anotação existente
        # validações
        return annotation
    
    # annotation crud