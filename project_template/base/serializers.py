from rest_framework import serializers


class Serializer(serializers.Serializer):
    def get_request_ip_address(self):
        return self.context.get("ip_address")

    def get_request_endpoint_url(self):
        return self.context.get("endpoint_url")

    def get_view_name(self):
        return self.context.get("endpoint_name")

    def get_requet_method_type(self):
        request = self.context.get("request")
        return request.method


class ModelSerializer(serializers.ModelSerializer):
    def get_request_ip_address(self):
        view = self.context.get("view")
        return view.get_request_ip_address()

    def get_request_endpoint_url(self):
        view = self.context.get("view")
        return view.get_request_endpoint_url()

    def get_view_name(self):
        view = self.context.get("view")
        return view.get_view_name()

    def get_requet_method_type(self):
        request = self.context.get("request")
        return request.method
