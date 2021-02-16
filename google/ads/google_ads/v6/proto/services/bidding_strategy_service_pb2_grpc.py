# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from google.ads.google_ads.v6.proto.resources import bidding_strategy_pb2 as google_dot_ads_dot_googleads_dot_v6_dot_resources_dot_bidding__strategy__pb2
from google.ads.google_ads.v6.proto.services import bidding_strategy_service_pb2 as google_dot_ads_dot_googleads_dot_v6_dot_services_dot_bidding__strategy__service__pb2


class BiddingStrategyServiceStub(object):
    """Proto file describing the Bidding Strategy service.

    Service to manage bidding strategies.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetBiddingStrategy = channel.unary_unary(
                '/google.ads.googleads.v6.services.BiddingStrategyService/GetBiddingStrategy',
                request_serializer=google_dot_ads_dot_googleads_dot_v6_dot_services_dot_bidding__strategy__service__pb2.GetBiddingStrategyRequest.SerializeToString,
                response_deserializer=google_dot_ads_dot_googleads_dot_v6_dot_resources_dot_bidding__strategy__pb2.BiddingStrategy.FromString,
                )
        self.MutateBiddingStrategies = channel.unary_unary(
                '/google.ads.googleads.v6.services.BiddingStrategyService/MutateBiddingStrategies',
                request_serializer=google_dot_ads_dot_googleads_dot_v6_dot_services_dot_bidding__strategy__service__pb2.MutateBiddingStrategiesRequest.SerializeToString,
                response_deserializer=google_dot_ads_dot_googleads_dot_v6_dot_services_dot_bidding__strategy__service__pb2.MutateBiddingStrategiesResponse.FromString,
                )


class BiddingStrategyServiceServicer(object):
    """Proto file describing the Bidding Strategy service.

    Service to manage bidding strategies.
    """

    def GetBiddingStrategy(self, request, context):
        """Returns the requested bidding strategy in full detail.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def MutateBiddingStrategies(self, request, context):
        """Creates, updates, or removes bidding strategies. Operation statuses are
        returned.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_BiddingStrategyServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'GetBiddingStrategy': grpc.unary_unary_rpc_method_handler(
                    servicer.GetBiddingStrategy,
                    request_deserializer=google_dot_ads_dot_googleads_dot_v6_dot_services_dot_bidding__strategy__service__pb2.GetBiddingStrategyRequest.FromString,
                    response_serializer=google_dot_ads_dot_googleads_dot_v6_dot_resources_dot_bidding__strategy__pb2.BiddingStrategy.SerializeToString,
            ),
            'MutateBiddingStrategies': grpc.unary_unary_rpc_method_handler(
                    servicer.MutateBiddingStrategies,
                    request_deserializer=google_dot_ads_dot_googleads_dot_v6_dot_services_dot_bidding__strategy__service__pb2.MutateBiddingStrategiesRequest.FromString,
                    response_serializer=google_dot_ads_dot_googleads_dot_v6_dot_services_dot_bidding__strategy__service__pb2.MutateBiddingStrategiesResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'google.ads.googleads.v6.services.BiddingStrategyService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class BiddingStrategyService(object):
    """Proto file describing the Bidding Strategy service.

    Service to manage bidding strategies.
    """

    @staticmethod
    def GetBiddingStrategy(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.ads.googleads.v6.services.BiddingStrategyService/GetBiddingStrategy',
            google_dot_ads_dot_googleads_dot_v6_dot_services_dot_bidding__strategy__service__pb2.GetBiddingStrategyRequest.SerializeToString,
            google_dot_ads_dot_googleads_dot_v6_dot_resources_dot_bidding__strategy__pb2.BiddingStrategy.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def MutateBiddingStrategies(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.ads.googleads.v6.services.BiddingStrategyService/MutateBiddingStrategies',
            google_dot_ads_dot_googleads_dot_v6_dot_services_dot_bidding__strategy__service__pb2.MutateBiddingStrategiesRequest.SerializeToString,
            google_dot_ads_dot_googleads_dot_v6_dot_services_dot_bidding__strategy__service__pb2.MutateBiddingStrategiesResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
