# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import communication_pb2 as communication__pb2


class CommunicationServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.SendMission = channel.unary_unary(
                '/communication.CommunicationService/SendMission',
                request_serializer=communication__pb2.Mission.SerializeToString,
                response_deserializer=communication__pb2.Acknowledge.FromString,
                )
        self.SendStatus = channel.unary_unary(
                '/communication.CommunicationService/SendStatus',
                request_serializer=communication__pb2.Status.SerializeToString,
                response_deserializer=communication__pb2.Acknowledge.FromString,
                )


class CommunicationServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def SendMission(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SendStatus(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_CommunicationServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'SendMission': grpc.unary_unary_rpc_method_handler(
                    servicer.SendMission,
                    request_deserializer=communication__pb2.Mission.FromString,
                    response_serializer=communication__pb2.Acknowledge.SerializeToString,
            ),
            'SendStatus': grpc.unary_unary_rpc_method_handler(
                    servicer.SendStatus,
                    request_deserializer=communication__pb2.Status.FromString,
                    response_serializer=communication__pb2.Acknowledge.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'communication.CommunicationService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class CommunicationService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def SendMission(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/communication.CommunicationService/SendMission',
            communication__pb2.Mission.SerializeToString,
            communication__pb2.Acknowledge.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SendStatus(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/communication.CommunicationService/SendStatus',
            communication__pb2.Status.SerializeToString,
            communication__pb2.Acknowledge.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)