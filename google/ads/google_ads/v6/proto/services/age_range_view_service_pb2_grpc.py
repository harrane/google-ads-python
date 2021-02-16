# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from google.ads.google_ads.v6.proto.resources import age_range_view_pb2 as google_dot_ads_dot_googleads_dot_v6_dot_resources_dot_age__range__view__pb2
from google.ads.google_ads.v6.proto.services import age_range_view_service_pb2 as google_dot_ads_dot_googleads_dot_v6_dot_services_dot_age__range__view__service__pb2


class AgeRangeViewServiceStub(object):
    """Proto file describing the Age Range View service.

    Service to manage age range views.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetAgeRangeView = channel.unary_unary(
                '/google.ads.googleads.v6.services.AgeRangeViewService/GetAgeRangeView',
                request_serializer=google_dot_ads_dot_googleads_dot_v6_dot_services_dot_age__range__view__service__pb2.GetAgeRangeViewRequest.SerializeToString,
                response_deserializer=google_dot_ads_dot_googleads_dot_v6_dot_resources_dot_age__range__view__pb2.AgeRangeView.FromString,
                )


class AgeRangeViewServiceServicer(object):
    """Proto file describing the Age Range View service.

    Service to manage age range views.
    """

    def GetAgeRangeView(self, request, context):
        """Returns the requested age range view in full detail.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_AgeRangeViewServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'GetAgeRangeView': grpc.unary_unary_rpc_method_handler(
                    servicer.GetAgeRangeView,
                    request_deserializer=google_dot_ads_dot_googleads_dot_v6_dot_services_dot_age__range__view__service__pb2.GetAgeRangeViewRequest.FromString,
                    response_serializer=google_dot_ads_dot_googleads_dot_v6_dot_resources_dot_age__range__view__pb2.AgeRangeView.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'google.ads.googleads.v6.services.AgeRangeViewService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class AgeRangeViewService(object):
    """Proto file describing the Age Range View service.

    Service to manage age range views.
    """

    @staticmethod
    def GetAgeRangeView(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.ads.googleads.v6.services.AgeRangeViewService/GetAgeRangeView',
            google_dot_ads_dot_googleads_dot_v6_dot_services_dot_age__range__view__service__pb2.GetAgeRangeViewRequest.SerializeToString,
            google_dot_ads_dot_googleads_dot_v6_dot_resources_dot_age__range__view__pb2.AgeRangeView.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
