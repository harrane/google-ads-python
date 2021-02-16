# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from google.ads.google_ads.v6.proto.resources import campaign_criterion_simulation_pb2 as google_dot_ads_dot_googleads_dot_v6_dot_resources_dot_campaign__criterion__simulation__pb2
from google.ads.google_ads.v6.proto.services import campaign_criterion_simulation_service_pb2 as google_dot_ads_dot_googleads_dot_v6_dot_services_dot_campaign__criterion__simulation__service__pb2


class CampaignCriterionSimulationServiceStub(object):
    """Proto file describing the CampaignCriterionSimulation service.

    Service to fetch campaign criterion simulations.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetCampaignCriterionSimulation = channel.unary_unary(
                '/google.ads.googleads.v6.services.CampaignCriterionSimulationService/GetCampaignCriterionSimulation',
                request_serializer=google_dot_ads_dot_googleads_dot_v6_dot_services_dot_campaign__criterion__simulation__service__pb2.GetCampaignCriterionSimulationRequest.SerializeToString,
                response_deserializer=google_dot_ads_dot_googleads_dot_v6_dot_resources_dot_campaign__criterion__simulation__pb2.CampaignCriterionSimulation.FromString,
                )


class CampaignCriterionSimulationServiceServicer(object):
    """Proto file describing the CampaignCriterionSimulation service.

    Service to fetch campaign criterion simulations.
    """

    def GetCampaignCriterionSimulation(self, request, context):
        """Returns the requested campaign criterion simulation in full detail.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_CampaignCriterionSimulationServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'GetCampaignCriterionSimulation': grpc.unary_unary_rpc_method_handler(
                    servicer.GetCampaignCriterionSimulation,
                    request_deserializer=google_dot_ads_dot_googleads_dot_v6_dot_services_dot_campaign__criterion__simulation__service__pb2.GetCampaignCriterionSimulationRequest.FromString,
                    response_serializer=google_dot_ads_dot_googleads_dot_v6_dot_resources_dot_campaign__criterion__simulation__pb2.CampaignCriterionSimulation.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'google.ads.googleads.v6.services.CampaignCriterionSimulationService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class CampaignCriterionSimulationService(object):
    """Proto file describing the CampaignCriterionSimulation service.

    Service to fetch campaign criterion simulations.
    """

    @staticmethod
    def GetCampaignCriterionSimulation(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.ads.googleads.v6.services.CampaignCriterionSimulationService/GetCampaignCriterionSimulation',
            google_dot_ads_dot_googleads_dot_v6_dot_services_dot_campaign__criterion__simulation__service__pb2.GetCampaignCriterionSimulationRequest.SerializeToString,
            google_dot_ads_dot_googleads_dot_v6_dot_resources_dot_campaign__criterion__simulation__pb2.CampaignCriterionSimulation.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
