# -*- coding: utf-8 -*-
from ipware import get_client_ip
from rest_framework import mixins, viewsets

from .helper import response_modification


class ViewSet(viewsets.ViewSet):
    """
    Overriding : Modify the API response format for common place.
    """

    def initial(self, request, *args, **kwargs):
        client_ip, _ = get_client_ip(request)
        request.META["REMOTE_ADDR"] = client_ip

        return super().initial(request, *args, **kwargs)

    def finalize_response(self, request, response, *args, **kwargs):
        response = response_modification(response)
        return super().finalize_response(request, response, *args, **kwargs)

    def get_request_ip_address(self):
        return self.request.META.get("REMOTE_ADDR")

    def get_request_endpoint_url(self):
        return self.request.get_full_path()

    def get_requet_method_type(self):
        return self.request.method

    def get_serializer_context(self):
        """
        Set client IP Address and request url in the context
        """
        context = {}
        context["request"] = self.request
        context["ip_address"] = self.get_request_ip_address()
        context["endpoint_url"] = self.get_request_endpoint_url()
        context["endpoint_name"] = self.get_view_name()

        return context


class GenericViewSet(viewsets.GenericViewSet):
    """
    Overriding : Modify the API response format for common place.
    """

    def initial(self, request, *args, **kwargs):
        client_ip, _ = get_client_ip(request)
        request.META["REMOTE_ADDR"] = client_ip

        return super().initial(request, *args, **kwargs)

    def finalize_response(self, request, response, *args, **kwargs):
        response = response_modification(response)
        return super().finalize_response(request, response, *args, **kwargs)

    def get_request_ip_address(self):
        return self.request.META.get("REMOTE_ADDR")

    def get_request_endpoint_url(self):
        return self.request.get_full_path()

    def get_requet_method_type(self):
        return self.request.method

    def get_serializer_context(self):
        """
        Set client IP Address and request url in the context
        """
        context = super().get_serializer_context()

        context["user"] = self.request.user
        context["ip_address"] = self.get_request_ip_address()
        context["endpoint_url"] = self.get_request_endpoint_url()
        context["endpoint_name"] = self.get_view_name()

        return context


class ModelViewSet(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    GenericViewSet,
):
    """
    Overriding : Modify the API response format for common place.

    A viewset that provides default `create()`, `retrieve()`, `update()`,
    `partial_update()`, `destroy()` and `list()` actions.
    """

    pass


class CreateViewSet(mixins.CreateModelMixin, GenericViewSet):
    """
    Overriding : Modify the API response format for common place.

    A viewset that provides default `create()` actions.
    """

    pass


class CreateListViewSet(mixins.CreateModelMixin, mixins.ListModelMixin, GenericViewSet):
    """
    Overriding : Modify the API response format for common place.

    A viewset that provides default `create()` and `list()` actions.
    """

    pass


class CreateRetrieveViewSet(
    mixins.CreateModelMixin, mixins.RetrieveModelMixin, GenericViewSet
):
    """
    Overriding : Modify the API response format for common place.

    A viewset that provides default `create()` and `retrieve()` actions.
    """

    pass


class CreateRetrieveDestoryViewSet(
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.DestroyModelMixin,
    GenericViewSet,
):
    """
    Overriding : Modify the API response format for common place.

    A viewset that provides default `create()`, `retrieve()` and `destroy()` actions.
    """

    pass


class CreateUpdateRetrieveDestoryViewSet(
    mixins.CreateModelMixin,
    mixins.UpdateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.DestroyModelMixin,
    GenericViewSet,
):
    """
    Overriding : Modify the API response format for common place.

    A viewset that provides default `create()`, `update()`, `retrieve()` and `destroy()` actions.
    """

    pass


class CreateListRetrieveViewSet(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    GenericViewSet,
):
    """
    Overriding : Modify the API response format for common place.

    A viewset that provides default `create()`, `retrieve()` and `list()` actions.
    """

    pass


class ListViewSet(mixins.ListModelMixin, GenericViewSet):
    """
    Overriding : Modify the API response format for common place.

    A viewset that provides default `list()` actions.
    """

    pass


class ListRetrieveViewSet(
    mixins.ListModelMixin, mixins.RetrieveModelMixin, GenericViewSet
):
    """
    Overriding : Modify the API response format for common place.

    A viewset that provides default `retrieve()`,  and `list()` actions.
    """

    pass


class RetrieveUpdateViewSet(
    mixins.RetrieveModelMixin, mixins.UpdateModelMixin, GenericViewSet
):
    """
    Overriding : Modify the API response format for common place.

    A viewset that provides default `retrieve()` actions.
    """

    pass


class RetrieveViewSet(mixins.RetrieveModelMixin, GenericViewSet):
    """
    Overriding : Modify the API response format for common place.

    A viewset that provides default `retrieve()` actions.
    """

    pass


class UpdateViewSet(mixins.UpdateModelMixin, GenericViewSet):
    """
    Overriding : Modify the API response format for common place.

     A viewset that provides default `update()` actions.
    """

    pass
