# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from google.ads.google_ads.v6.proto.resources import ad_group_pb2 as google_dot_ads_dot_googleads_dot_v6_dot_resources_dot_ad__group__pb2
from google.ads.google_ads.v6.proto.services import ad_group_service_pb2 as google_dot_ads_dot_googleads_dot_v6_dot_services_dot_ad__group__service__pb2


class AdGroupServiceStub(object):
    """Proto file describing the Ad Group service.

    Service to manage ad groups.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetAdGroup = channel.unary_unary(
                '/google.ads.googleads.v6.services.AdGroupService/GetAdGroup',
                request_serializer=google_dot_ads_dot_googleads_dot_v6_dot_services_dot_ad__group__service__pb2.GetAdGroupRequest.SerializeToString,
                response_deserializer=google_dot_ads_dot_googleads_dot_v6_dot_resources_dot_ad__group__pb2.AdGroup.FromString,
                )
        self.MutateAdGroups = channel.unary_unary(
                '/google.ads.googleads.v6.services.AdGroupService/MutateAdGroups',
                request_serializer=google_dot_ads_dot_googleads_dot_v6_dot_services_dot_ad__group__service__pb2.MutateAdGroupsRequest.SerializeToString,
                response_deserializer=google_dot_ads_dot_googleads_dot_v6_dot_services_dot_ad__group__service__pb2.MutateAdGroupsResponse.FromString,
                )


class AdGroupServiceServicer(object):
    """Proto file describing the Ad Group service.

    Service to manage ad groups.
    """

    def GetAdGroup(self, request, context):
        """Returns the requested ad group in full detail.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def MutateAdGroups(self, request, context):
        """Creates, updates, or removes ad groups. Operation statuses are returned.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_AdGroupServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'GetAdGroup': grpc.unary_unary_rpc_method_handler(
                    servicer.GetAdGroup,
                    request_deserializer=google_dot_ads_dot_googleads_dot_v6_dot_services_dot_ad__group__service__pb2.GetAdGroupRequest.FromString,
                    response_serializer=google_dot_ads_dot_googleads_dot_v6_dot_resources_dot_ad__group__pb2.AdGroup.SerializeToString,
            ),
            'MutateAdGroups': grpc.unary_unary_rpc_method_handler(
                    servicer.MutateAdGroups,
                    request_deserializer=google_dot_ads_dot_googleads_dot_v6_dot_services_dot_ad__group__service__pb2.MutateAdGroupsRequest.FromString,
                    response_serializer=google_dot_ads_dot_googleads_dot_v6_dot_services_dot_ad__group__service__pb2.MutateAdGroupsResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'google.ads.googleads.v6.services.AdGroupService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class AdGroupService(object):
    """Proto file describing the Ad Group service.

    Service to manage ad groups.
    """

    @staticmethod
    def GetAdGroup(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.ads.googleads.v6.services.AdGroupService/GetAdGroup',
            google_dot_ads_dot_googleads_dot_v6_dot_services_dot_ad__group__service__pb2.GetAdGroupRequest.SerializeToString,
            google_dot_ads_dot_googleads_dot_v6_dot_resources_dot_ad__group__pb2.AdGroup.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def MutateAdGroups(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.ads.googleads.v6.services.AdGroupService/MutateAdGroups',
            google_dot_ads_dot_googleads_dot_v6_dot_services_dot_ad__group__service__pb2.MutateAdGroupsRequest.SerializeToString,
            google_dot_ads_dot_googleads_dot_v6_dot_services_dot_ad__group__service__pb2.MutateAdGroupsResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
