# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
#
# Code generated by aaz-dev-tools
# --------------------------------------------------------------------------------------------

# pylint: skip-file
# flake8: noqa

from azure.cli.core.aaz import *


@register_command(
    "network route-filter show",
    is_preview=True,
)
class Show(AAZCommand):
    """Get the details of a route filter.

    :example: Get the details of a route filter.
        az network route-filter show -g MyResourceGroup -n MyRouteFilter

    :example: Get the details of a route filter. (autogenerated)
        az network route-filter show --expand peerings --name MyRouteFilter --resource-group MyResourceGroup
    """

    _aaz_info = {
        "version": "2021-08-01",
        "resources": [
            ["mgmt-plane", "/subscriptions/{}/resourcegroups/{}/providers/microsoft.network/routefilters/{}", "2021-08-01"],
        ]
    }

    def _handler(self, command_args):
        super()._handler(command_args)
        self._execute_operations()
        return self._output()

    _args_schema = None

    @classmethod
    def _build_arguments_schema(cls, *args, **kwargs):
        if cls._args_schema is not None:
            return cls._args_schema
        cls._args_schema = super()._build_arguments_schema(*args, **kwargs)

        # define Arg Group ""

        _args_schema = cls._args_schema
        _args_schema.resource_group = AAZResourceGroupNameArg(
            required=True,
        )
        _args_schema.name = AAZStrArg(
            options=["-n", "--name"],
            help="Name of the route filter.",
            required=True,
            id_part="name",
        )
        _args_schema.expand = AAZStrArg(
            options=["--expand"],
            help="Expands referenced express route bgp peering resources.",
        )
        return cls._args_schema

    def _execute_operations(self):
        self.pre_operations()
        self.RouteFiltersGet(ctx=self.ctx)()
        self.post_operations()

    @register_callback
    def pre_operations(self):
        pass

    @register_callback
    def post_operations(self):
        pass

    def _output(self, *args, **kwargs):
        result = self.deserialize_output(self.ctx.vars.instance, client_flatten=True)
        return result

    class RouteFiltersGet(AAZHttpOperation):
        CLIENT_TYPE = "MgmtClient"

        def __call__(self, *args, **kwargs):
            request = self.make_request()
            session = self.client.send_request(request=request, stream=False, **kwargs)
            if session.http_response.status_code in [200]:
                return self.on_200(session)

            return self.on_error(session.http_response)

        @property
        def url(self):
            return self.client.format_url(
                "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/routeFilters/{routeFilterName}",
                **self.url_parameters
            )

        @property
        def method(self):
            return "GET"

        @property
        def error_format(self):
            return "ODataV4Format"

        @property
        def url_parameters(self):
            parameters = {
                **self.serialize_url_param(
                    "resourceGroupName", self.ctx.args.resource_group,
                    required=True,
                ),
                **self.serialize_url_param(
                    "routeFilterName", self.ctx.args.name,
                    required=True,
                ),
                **self.serialize_url_param(
                    "subscriptionId", self.ctx.subscription_id,
                    required=True,
                ),
            }
            return parameters

        @property
        def query_parameters(self):
            parameters = {
                **self.serialize_query_param(
                    "$expand", self.ctx.args.expand,
                ),
                **self.serialize_query_param(
                    "api-version", "2021-08-01",
                    required=True,
                ),
            }
            return parameters

        @property
        def header_parameters(self):
            parameters = {
                **self.serialize_header_param(
                    "Accept", "application/json",
                ),
            }
            return parameters

        def on_200(self, session):
            data = self.deserialize_http_content(session)
            self.ctx.set_var(
                "instance",
                data,
                schema_builder=self._build_schema_on_200
            )

        _schema_on_200 = None

        @classmethod
        def _build_schema_on_200(cls):
            if cls._schema_on_200 is not None:
                return cls._schema_on_200

            cls._schema_on_200 = AAZObjectType()

            _schema_on_200 = cls._schema_on_200
            _schema_on_200.etag = AAZStrType(
                flags={"read_only": True},
            )
            _schema_on_200.id = AAZStrType()
            _schema_on_200.location = AAZStrType(
                flags={"required": True},
            )
            _schema_on_200.name = AAZStrType(
                flags={"read_only": True},
            )
            _schema_on_200.properties = AAZObjectType(
                flags={"client_flatten": True},
            )
            _schema_on_200.tags = AAZDictType()
            _schema_on_200.type = AAZStrType(
                flags={"read_only": True},
            )

            properties = cls._schema_on_200.properties
            properties.ipv6_peerings = AAZListType(
                serialized_name="ipv6Peerings",
                flags={"read_only": True},
            )
            properties.peerings = AAZListType(
                flags={"read_only": True},
            )
            properties.provisioning_state = AAZStrType(
                serialized_name="provisioningState",
                flags={"read_only": True},
            )
            properties.rules = AAZListType()

            ipv6_peerings = cls._schema_on_200.properties.ipv6_peerings
            ipv6_peerings.Element = AAZObjectType(
                flags={"read_only": True},
            )
            _ShowHelper._build_schema_express_route_circuit_peering_read(ipv6_peerings.Element)

            peerings = cls._schema_on_200.properties.peerings
            peerings.Element = AAZObjectType(
                flags={"read_only": True},
            )
            _ShowHelper._build_schema_express_route_circuit_peering_read(peerings.Element)

            rules = cls._schema_on_200.properties.rules
            rules.Element = AAZObjectType()

            _element = cls._schema_on_200.properties.rules.Element
            _element.etag = AAZStrType(
                flags={"read_only": True},
            )
            _element.id = AAZStrType()
            _element.location = AAZStrType()
            _element.name = AAZStrType()
            _element.properties = AAZObjectType(
                flags={"client_flatten": True},
            )

            properties = cls._schema_on_200.properties.rules.Element.properties
            properties.access = AAZStrType(
                flags={"required": True},
            )
            properties.communities = AAZListType(
                flags={"required": True},
            )
            properties.provisioning_state = AAZStrType(
                serialized_name="provisioningState",
                flags={"read_only": True},
            )
            properties.route_filter_rule_type = AAZStrType(
                serialized_name="routeFilterRuleType",
                flags={"required": True},
            )

            communities = cls._schema_on_200.properties.rules.Element.properties.communities
            communities.Element = AAZStrType()

            tags = cls._schema_on_200.tags
            tags.Element = AAZStrType()

            return cls._schema_on_200


class _ShowHelper:
    """Helper class for Show"""

    _schema_express_route_circuit_peering_config_read = None

    @classmethod
    def _build_schema_express_route_circuit_peering_config_read(cls, _schema):
        if cls._schema_express_route_circuit_peering_config_read is not None:
            _schema.advertised_communities = cls._schema_express_route_circuit_peering_config_read.advertised_communities
            _schema.advertised_public_prefixes = cls._schema_express_route_circuit_peering_config_read.advertised_public_prefixes
            _schema.advertised_public_prefixes_state = cls._schema_express_route_circuit_peering_config_read.advertised_public_prefixes_state
            _schema.customer_asn = cls._schema_express_route_circuit_peering_config_read.customer_asn
            _schema.legacy_mode = cls._schema_express_route_circuit_peering_config_read.legacy_mode
            _schema.routing_registry_name = cls._schema_express_route_circuit_peering_config_read.routing_registry_name
            return

        cls._schema_express_route_circuit_peering_config_read = _schema_express_route_circuit_peering_config_read = AAZObjectType(
            flags={"read_only": True}
        )

        express_route_circuit_peering_config_read = _schema_express_route_circuit_peering_config_read
        express_route_circuit_peering_config_read.advertised_communities = AAZListType(
            serialized_name="advertisedCommunities",
            flags={"read_only": True},
        )
        express_route_circuit_peering_config_read.advertised_public_prefixes = AAZListType(
            serialized_name="advertisedPublicPrefixes",
            flags={"read_only": True},
        )
        express_route_circuit_peering_config_read.advertised_public_prefixes_state = AAZStrType(
            serialized_name="advertisedPublicPrefixesState",
            flags={"read_only": True},
        )
        express_route_circuit_peering_config_read.customer_asn = AAZIntType(
            serialized_name="customerASN",
            flags={"read_only": True},
        )
        express_route_circuit_peering_config_read.legacy_mode = AAZIntType(
            serialized_name="legacyMode",
            flags={"read_only": True},
        )
        express_route_circuit_peering_config_read.routing_registry_name = AAZStrType(
            serialized_name="routingRegistryName",
            flags={"read_only": True},
        )

        advertised_communities = _schema_express_route_circuit_peering_config_read.advertised_communities
        advertised_communities.Element = AAZStrType(
            flags={"read_only": True},
        )

        advertised_public_prefixes = _schema_express_route_circuit_peering_config_read.advertised_public_prefixes
        advertised_public_prefixes.Element = AAZStrType(
            flags={"read_only": True},
        )

        _schema.advertised_communities = cls._schema_express_route_circuit_peering_config_read.advertised_communities
        _schema.advertised_public_prefixes = cls._schema_express_route_circuit_peering_config_read.advertised_public_prefixes
        _schema.advertised_public_prefixes_state = cls._schema_express_route_circuit_peering_config_read.advertised_public_prefixes_state
        _schema.customer_asn = cls._schema_express_route_circuit_peering_config_read.customer_asn
        _schema.legacy_mode = cls._schema_express_route_circuit_peering_config_read.legacy_mode
        _schema.routing_registry_name = cls._schema_express_route_circuit_peering_config_read.routing_registry_name

    _schema_express_route_circuit_peering_read = None

    @classmethod
    def _build_schema_express_route_circuit_peering_read(cls, _schema):
        if cls._schema_express_route_circuit_peering_read is not None:
            _schema.etag = cls._schema_express_route_circuit_peering_read.etag
            _schema.id = cls._schema_express_route_circuit_peering_read.id
            _schema.name = cls._schema_express_route_circuit_peering_read.name
            _schema.properties = cls._schema_express_route_circuit_peering_read.properties
            _schema.type = cls._schema_express_route_circuit_peering_read.type
            return

        cls._schema_express_route_circuit_peering_read = _schema_express_route_circuit_peering_read = AAZObjectType(
            flags={"read_only": True}
        )

        express_route_circuit_peering_read = _schema_express_route_circuit_peering_read
        express_route_circuit_peering_read.etag = AAZStrType(
            flags={"read_only": True},
        )
        express_route_circuit_peering_read.id = AAZStrType(
            flags={"read_only": True},
        )
        express_route_circuit_peering_read.name = AAZStrType(
            flags={"read_only": True},
        )
        express_route_circuit_peering_read.properties = AAZObjectType(
            flags={"client_flatten": True, "read_only": True},
        )
        express_route_circuit_peering_read.type = AAZStrType(
            flags={"read_only": True},
        )

        properties = _schema_express_route_circuit_peering_read.properties
        properties.azure_asn = AAZIntType(
            serialized_name="azureASN",
            flags={"read_only": True},
        )
        properties.connections = AAZListType(
            flags={"read_only": True},
        )
        properties.express_route_connection = AAZObjectType(
            serialized_name="expressRouteConnection",
            flags={"read_only": True},
        )
        properties.gateway_manager_etag = AAZStrType(
            serialized_name="gatewayManagerEtag",
            flags={"read_only": True},
        )
        properties.ipv6_peering_config = AAZObjectType(
            serialized_name="ipv6PeeringConfig",
            flags={"read_only": True},
        )
        properties.last_modified_by = AAZStrType(
            serialized_name="lastModifiedBy",
            flags={"read_only": True},
        )
        properties.microsoft_peering_config = AAZObjectType(
            serialized_name="microsoftPeeringConfig",
            flags={"read_only": True},
        )
        cls._build_schema_express_route_circuit_peering_config_read(properties.microsoft_peering_config)
        properties.peer_asn = AAZIntType(
            serialized_name="peerASN",
            flags={"read_only": True},
        )
        properties.peered_connections = AAZListType(
            serialized_name="peeredConnections",
            flags={"read_only": True},
        )
        properties.peering_type = AAZStrType(
            serialized_name="peeringType",
            flags={"read_only": True},
        )
        properties.primary_azure_port = AAZStrType(
            serialized_name="primaryAzurePort",
            flags={"read_only": True},
        )
        properties.primary_peer_address_prefix = AAZStrType(
            serialized_name="primaryPeerAddressPrefix",
            flags={"read_only": True},
        )
        properties.provisioning_state = AAZStrType(
            serialized_name="provisioningState",
            flags={"read_only": True},
        )
        properties.route_filter = AAZObjectType(
            serialized_name="routeFilter",
            flags={"read_only": True},
        )
        cls._build_schema_sub_resource_read(properties.route_filter)
        properties.secondary_azure_port = AAZStrType(
            serialized_name="secondaryAzurePort",
            flags={"read_only": True},
        )
        properties.secondary_peer_address_prefix = AAZStrType(
            serialized_name="secondaryPeerAddressPrefix",
            flags={"read_only": True},
        )
        properties.shared_key = AAZStrType(
            serialized_name="sharedKey",
            flags={"read_only": True},
        )
        properties.state = AAZStrType(
            flags={"read_only": True},
        )
        properties.stats = AAZObjectType(
            flags={"read_only": True},
        )
        properties.vlan_id = AAZIntType(
            serialized_name="vlanId",
            flags={"read_only": True},
        )

        connections = _schema_express_route_circuit_peering_read.properties.connections
        connections.Element = AAZObjectType(
            flags={"read_only": True},
        )

        _element = _schema_express_route_circuit_peering_read.properties.connections.Element
        _element.etag = AAZStrType(
            flags={"read_only": True},
        )
        _element.id = AAZStrType(
            flags={"read_only": True},
        )
        _element.name = AAZStrType(
            flags={"read_only": True},
        )
        _element.properties = AAZObjectType(
            flags={"client_flatten": True, "read_only": True},
        )
        _element.type = AAZStrType(
            flags={"read_only": True},
        )

        properties = _schema_express_route_circuit_peering_read.properties.connections.Element.properties
        properties.address_prefix = AAZStrType(
            serialized_name="addressPrefix",
            flags={"read_only": True},
        )
        properties.authorization_key = AAZStrType(
            serialized_name="authorizationKey",
            flags={"read_only": True},
        )
        properties.circuit_connection_status = AAZStrType(
            serialized_name="circuitConnectionStatus",
            flags={"read_only": True},
        )
        properties.express_route_circuit_peering = AAZObjectType(
            serialized_name="expressRouteCircuitPeering",
            flags={"read_only": True},
        )
        cls._build_schema_sub_resource_read(properties.express_route_circuit_peering)
        properties.ipv6_circuit_connection_config = AAZObjectType(
            serialized_name="ipv6CircuitConnectionConfig",
            flags={"read_only": True},
        )
        properties.peer_express_route_circuit_peering = AAZObjectType(
            serialized_name="peerExpressRouteCircuitPeering",
            flags={"read_only": True},
        )
        cls._build_schema_sub_resource_read(properties.peer_express_route_circuit_peering)
        properties.provisioning_state = AAZStrType(
            serialized_name="provisioningState",
            flags={"read_only": True},
        )

        ipv6_circuit_connection_config = _schema_express_route_circuit_peering_read.properties.connections.Element.properties.ipv6_circuit_connection_config
        ipv6_circuit_connection_config.address_prefix = AAZStrType(
            serialized_name="addressPrefix",
            flags={"read_only": True},
        )
        ipv6_circuit_connection_config.circuit_connection_status = AAZStrType(
            serialized_name="circuitConnectionStatus",
            flags={"read_only": True},
        )

        express_route_connection = _schema_express_route_circuit_peering_read.properties.express_route_connection
        express_route_connection.id = AAZStrType(
            flags={"read_only": True},
        )

        ipv6_peering_config = _schema_express_route_circuit_peering_read.properties.ipv6_peering_config
        ipv6_peering_config.microsoft_peering_config = AAZObjectType(
            serialized_name="microsoftPeeringConfig",
            flags={"read_only": True},
        )
        cls._build_schema_express_route_circuit_peering_config_read(ipv6_peering_config.microsoft_peering_config)
        ipv6_peering_config.primary_peer_address_prefix = AAZStrType(
            serialized_name="primaryPeerAddressPrefix",
            flags={"read_only": True},
        )
        ipv6_peering_config.route_filter = AAZObjectType(
            serialized_name="routeFilter",
            flags={"read_only": True},
        )
        cls._build_schema_sub_resource_read(ipv6_peering_config.route_filter)
        ipv6_peering_config.secondary_peer_address_prefix = AAZStrType(
            serialized_name="secondaryPeerAddressPrefix",
            flags={"read_only": True},
        )
        ipv6_peering_config.state = AAZStrType(
            flags={"read_only": True},
        )

        peered_connections = _schema_express_route_circuit_peering_read.properties.peered_connections
        peered_connections.Element = AAZObjectType(
            flags={"read_only": True},
        )

        _element = _schema_express_route_circuit_peering_read.properties.peered_connections.Element
        _element.etag = AAZStrType(
            flags={"read_only": True},
        )
        _element.id = AAZStrType(
            flags={"read_only": True},
        )
        _element.name = AAZStrType(
            flags={"read_only": True},
        )
        _element.properties = AAZObjectType(
            flags={"client_flatten": True, "read_only": True},
        )
        _element.type = AAZStrType(
            flags={"read_only": True},
        )

        properties = _schema_express_route_circuit_peering_read.properties.peered_connections.Element.properties
        properties.address_prefix = AAZStrType(
            serialized_name="addressPrefix",
            flags={"read_only": True},
        )
        properties.auth_resource_guid = AAZStrType(
            serialized_name="authResourceGuid",
            flags={"read_only": True},
        )
        properties.circuit_connection_status = AAZStrType(
            serialized_name="circuitConnectionStatus",
            flags={"read_only": True},
        )
        properties.connection_name = AAZStrType(
            serialized_name="connectionName",
            flags={"read_only": True},
        )
        properties.express_route_circuit_peering = AAZObjectType(
            serialized_name="expressRouteCircuitPeering",
            flags={"read_only": True},
        )
        cls._build_schema_sub_resource_read(properties.express_route_circuit_peering)
        properties.peer_express_route_circuit_peering = AAZObjectType(
            serialized_name="peerExpressRouteCircuitPeering",
            flags={"read_only": True},
        )
        cls._build_schema_sub_resource_read(properties.peer_express_route_circuit_peering)
        properties.provisioning_state = AAZStrType(
            serialized_name="provisioningState",
            flags={"read_only": True},
        )

        stats = _schema_express_route_circuit_peering_read.properties.stats
        stats.primarybytes_in = AAZIntType(
            serialized_name="primarybytesIn",
            flags={"read_only": True},
        )
        stats.primarybytes_out = AAZIntType(
            serialized_name="primarybytesOut",
            flags={"read_only": True},
        )
        stats.secondarybytes_in = AAZIntType(
            serialized_name="secondarybytesIn",
            flags={"read_only": True},
        )
        stats.secondarybytes_out = AAZIntType(
            serialized_name="secondarybytesOut",
            flags={"read_only": True},
        )

        _schema.etag = cls._schema_express_route_circuit_peering_read.etag
        _schema.id = cls._schema_express_route_circuit_peering_read.id
        _schema.name = cls._schema_express_route_circuit_peering_read.name
        _schema.properties = cls._schema_express_route_circuit_peering_read.properties
        _schema.type = cls._schema_express_route_circuit_peering_read.type

    _schema_sub_resource_read = None

    @classmethod
    def _build_schema_sub_resource_read(cls, _schema):
        if cls._schema_sub_resource_read is not None:
            _schema.id = cls._schema_sub_resource_read.id
            return

        cls._schema_sub_resource_read = _schema_sub_resource_read = AAZObjectType(
            flags={"read_only": True}
        )

        sub_resource_read = _schema_sub_resource_read
        sub_resource_read.id = AAZStrType(
            flags={"read_only": True},
        )

        _schema.id = cls._schema_sub_resource_read.id


__all__ = ["Show"]