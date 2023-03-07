from logging import logger
from google.protobuf.json_format import MessageToJson
from google.protobuf.json_format import Parse, MessageToDict
from rest_framework.views import APIView
from rest_framework import status, serializers
from rest_framework.permissions import IsAuthenticated
from rest_framework.request import Request
from rest_framework.response import Response
from order.service import (
    OrderService,
    ProductService,
    RuleService
)
from proto.phub.api import (
    RESPONSE_STATUS_ERROR,
    RESPONSE_STATUS_OK,
    UpdateOrderRequest,
    UpdateOrderResponse,
    OrderRequest,
    OrderResponse,
    OrderLog,
    ProductRequest,
    ProductResponse,
    ProductLog,
    GetOrCreateRuleRequest,
    GetOrCreateRuleResponse,
    RuleLog,
)

class OrderResource(APIView):
    '''
    Este recurso gera uma nova Order.
    '''

    @staticmethod
    def _log(
        message: str,
        request: OrderRequest,
        response: OrderResponse
    ):
        log = OrderLog(
            request=request,
            response=response
        )
        logger.info(message=message, extra=log)

    @staticmethod
    def _build_error_response(
        request_data: OrderRequest,
        error: Exception,
        http_status=status.HTTP_400_BAD_REQUEST
    ) -> Response:
        error_response = OrderResponse(status=RESPONSE_STATUS_ERROR, error_msg=error.message)

        self._log('Order error', request_data, error_response)
        logger.info(, extra=log)

        return Response(
            data=MessageToDict(error_response),
            status=http_status,
            exception=True,
        )

    def post(self, request: Request) -> Response:
        request_data = request.data

        self._log('Order create request', request_data)

        try:
            response = OrderService.create_order(request_data)

            self._log('Order completed', request_data, response)
            return Response(MessageToDict(response, float_precision=20), status=200)

        except (
            ValidationError,
            InvalidProduct
        ) as e:
            return self._build_error_response(
                request_data,
                e
            )
        except (
            ProdcutNotFound,
            AdminNotFound
        ) as e:
            return self._build_error_response(
                request_data,
                e,
                status.HTTP_404_NOT_FOUND
            )

class UpdateOrderResource(APIView):
    '''
    Este recurso atualiza uma Order, aplicando as regras existentes.
    '''

    @staticmethod
    def _log(
        message: str,
        request: UpdateOrderRequest,
        response: UpdateOrderResponse,
    ):
        log = OrderLog(
            request=request,
            response=response
        )
        logger.info(message=message, extra=log)
        

    @staticmethod
    def _build_error_response(
        request: OrderRequest,
        error: Exception,
        http_status=status.HTTP_400_BAD_REQUEST
    ) -> Response:
        error_response = UpdateOrderResponse(status=RESPONSE_STATUS_ERROR, error_msg=error.message)

        self._log('Order update error', request, error_response)

        return Response(
            data=MessageToDict(error_response),
            status=http_status,
            exception=True,
        )

    def post(self, request: Request) -> Response:
        request_data = request.data

        self._log('Order update request', request_data)

        try:
            response = OrderService.update_order(request_data)

            self._log('Order updated', request_data, response)

            return Response(MessageToDict(response, float_precision=20), status=200)

        except (
            ValidationError,
            RuleError,
            InvalidProduct
        ) as e:
            return self._build_error_response(
                request_data,
                e
            )
        except (
            ProdcutNotFound,
            OrderNotFound,
            AdminNotFound
        ) as e:
            return self._build_error_response(
                request_data,
                e,
                status.HTTP_404_NOT_FOUND
            )


class GetOrCreateRule(APIView):
    '''
    Get or create rule from rulehub
    '''

    @staticmethod
    def _log(
        request: GetOrCreateRuleRequest,
        response: GetOrCreateRuleResponse,
        message: str
    ):
        log = RuleLog(
            request=request,
            response=response
        )
        logger.info(message=message, extra=log)
    
    @staticmethod
    def _build_error_response(
        request: GetOrCreateRuleRequest,
        error: Exception,
        http_status=status.HTTP_400_BAD_REQUEST
    ) -> Response:
        error_response = GetOrCreateRuleResponse(status=RESPONSE_STATUS_ERROR, error_msg=error.message)

        self._log('Rule return error', request, error_response)

        return Response(
            data=MessageToDict(error_response),
            status=http_status,
            exception=True,
        )
    
    def post(self, request: Request) -> Response:
        request_data = request.data

        self._log('Rule request', request_data)

        try:
            response = RuleService.get_or_create_rule(request_data)

            self._log('Rule returned', request_data, response)

            return Response(MessageToDict(response, float_precision=20), status=200)

        except (
            ValidationError,
            RuleError,
            InvalidProduct,
            InvalidOrder
        ) as e:
            return self._build_error_response(
                request_data,
                e
            )
        except (
            ProdcutNotFound,
            OrderNotFound,
            AdminNotFound
        ) as e:
            return self._build_error_response(
                request_data,
                e,
                status.HTTP_404_NOT_FOUND
            )

# Product crud resources
# Rule application resource

