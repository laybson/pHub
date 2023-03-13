"""
This module has the common settings between all instances of staging.
"""
from config.settings.base import (
    DB_CONSUMER,
    DB_CONSUMER_READONLY,
    DB_FINANCE,
    DB_FINANCE_READONLY,
    DB_DEFAULT,
    DB_READONLY,
    DB_RO_ASYNC1,
    DB_TRANSPORT,
    DB_TRANSPORT_READONLY,
)
from config.settings.miscellaneous import get_dict_environ

__all__ = [
    'DATABASES',
]


DATABASES = {
    DB_DEFAULT: get_dict_environ('DB_DEFAULT'),
    DB_READONLY: get_dict_environ('DB_READONLY'),
    DB_RO_ASYNC1: get_dict_environ('DB_RO_ASYNC1'),
    DB_CONSUMER: get_dict_environ('DB_CONSUMER'),
    DB_CONSUMER_READONLY: get_dict_environ('DB_CONSUMER_READONLY'),
    DB_FINANCE: get_dict_environ('DB_FINANCE'),
    DB_FINANCE_READONLY: get_dict_environ('DB_FINANCE_READONLY'),
    DB_TRANSPORT: get_dict_environ('DB_TRANSPORT'),
    DB_TRANSPORT_READONLY: get_dict_environ('DB_TRANSPORT_READONLY'),
}
