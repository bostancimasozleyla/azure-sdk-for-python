# pylint: disable=too-many-lines
# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from io import IOBase
from typing import Any, AsyncIterable, Callable, Dict, IO, Optional, TypeVar, Union, cast, overload
import urllib.parse

from azure.core.async_paging import AsyncItemPaged, AsyncList
from azure.core.exceptions import (
    ClientAuthenticationError,
    HttpResponseError,
    ResourceExistsError,
    ResourceNotFoundError,
    ResourceNotModifiedError,
    map_error,
)
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import AsyncHttpResponse
from azure.core.polling import AsyncLROPoller, AsyncNoPolling, AsyncPollingMethod
from azure.core.rest import HttpRequest
from azure.core.tracing.decorator import distributed_trace
from azure.core.tracing.decorator_async import distributed_trace_async
from azure.core.utils import case_insensitive_dict
from azure.mgmt.core.exceptions import ARMErrorFormat
from azure.mgmt.core.polling.async_arm_polling import AsyncARMPolling

from ... import models as _models
from ..._vendor import _convert_request
from ...operations._private_endpoint_connections_operations import (
    build_delete_request,
    build_get_request,
    build_list_by_resource_request,
    build_put_request,
)

T = TypeVar("T")
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, AsyncHttpResponse], T, Dict[str, Any]], Any]]


class PrivateEndpointConnectionsOperations:
    """
    .. warning::
        **DO NOT** instantiate this class directly.

        Instead, you should access the following operations through
        :class:`~azure.mgmt.keyvault.v2022_07_01.aio.KeyVaultManagementClient`'s
        :attr:`private_endpoint_connections` attribute.
    """

    models = _models

    def __init__(self, *args, **kwargs) -> None:
        input_args = list(args)
        self._client = input_args.pop(0) if input_args else kwargs.pop("client")
        self._config = input_args.pop(0) if input_args else kwargs.pop("config")
        self._serialize = input_args.pop(0) if input_args else kwargs.pop("serializer")
        self._deserialize = input_args.pop(0) if input_args else kwargs.pop("deserializer")

    @distributed_trace_async
    async def get(
        self, resource_group_name: str, vault_name: str, private_endpoint_connection_name: str, **kwargs: Any
    ) -> Optional[_models.PrivateEndpointConnection]:
        """Gets the specified private endpoint connection associated with the key vault.

        :param resource_group_name: Name of the resource group that contains the key vault. Required.
        :type resource_group_name: str
        :param vault_name: The name of the key vault. Required.
        :type vault_name: str
        :param private_endpoint_connection_name: Name of the private endpoint connection associated
         with the key vault. Required.
        :type private_endpoint_connection_name: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: PrivateEndpointConnection or None or the result of cls(response)
        :rtype: ~azure.mgmt.keyvault.v2022_07_01.models.PrivateEndpointConnection or None
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        error_map = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = kwargs.pop("headers", {}) or {}
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version: str = kwargs.pop("api_version", _params.pop("api-version", "2022-07-01"))
        cls: ClsType[Optional[_models.PrivateEndpointConnection]] = kwargs.pop("cls", None)

        request = build_get_request(
            resource_group_name=resource_group_name,
            vault_name=vault_name,
            private_endpoint_connection_name=private_endpoint_connection_name,
            subscription_id=self._config.subscription_id,
            api_version=api_version,
            template_url=self.get.metadata["url"],
            headers=_headers,
            params=_params,
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)

        _stream = False
        pipeline_response: PipelineResponse = await self._client._pipeline.run(  # pylint: disable=protected-access
            request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200, 204]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        deserialized = None
        if response.status_code == 200:
            deserialized = self._deserialize("PrivateEndpointConnection", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    get.metadata = {
        "url": "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.KeyVault/vaults/{vaultName}/privateEndpointConnections/{privateEndpointConnectionName}"
    }

    @overload
    async def put(
        self,
        resource_group_name: str,
        vault_name: str,
        private_endpoint_connection_name: str,
        properties: _models.PrivateEndpointConnection,
        *,
        content_type: str = "application/json",
        **kwargs: Any
    ) -> _models.PrivateEndpointConnection:
        """Updates the specified private endpoint connection associated with the key vault.

        :param resource_group_name: Name of the resource group that contains the key vault. Required.
        :type resource_group_name: str
        :param vault_name: The name of the key vault. Required.
        :type vault_name: str
        :param private_endpoint_connection_name: Name of the private endpoint connection associated
         with the key vault. Required.
        :type private_endpoint_connection_name: str
        :param properties: The intended state of private endpoint connection. Required.
        :type properties: ~azure.mgmt.keyvault.v2022_07_01.models.PrivateEndpointConnection
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: PrivateEndpointConnection or the result of cls(response)
        :rtype: ~azure.mgmt.keyvault.v2022_07_01.models.PrivateEndpointConnection
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @overload
    async def put(
        self,
        resource_group_name: str,
        vault_name: str,
        private_endpoint_connection_name: str,
        properties: IO,
        *,
        content_type: str = "application/json",
        **kwargs: Any
    ) -> _models.PrivateEndpointConnection:
        """Updates the specified private endpoint connection associated with the key vault.

        :param resource_group_name: Name of the resource group that contains the key vault. Required.
        :type resource_group_name: str
        :param vault_name: The name of the key vault. Required.
        :type vault_name: str
        :param private_endpoint_connection_name: Name of the private endpoint connection associated
         with the key vault. Required.
        :type private_endpoint_connection_name: str
        :param properties: The intended state of private endpoint connection. Required.
        :type properties: IO
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: PrivateEndpointConnection or the result of cls(response)
        :rtype: ~azure.mgmt.keyvault.v2022_07_01.models.PrivateEndpointConnection
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @distributed_trace_async
    async def put(
        self,
        resource_group_name: str,
        vault_name: str,
        private_endpoint_connection_name: str,
        properties: Union[_models.PrivateEndpointConnection, IO],
        **kwargs: Any
    ) -> _models.PrivateEndpointConnection:
        """Updates the specified private endpoint connection associated with the key vault.

        :param resource_group_name: Name of the resource group that contains the key vault. Required.
        :type resource_group_name: str
        :param vault_name: The name of the key vault. Required.
        :type vault_name: str
        :param private_endpoint_connection_name: Name of the private endpoint connection associated
         with the key vault. Required.
        :type private_endpoint_connection_name: str
        :param properties: The intended state of private endpoint connection. Is either a
         PrivateEndpointConnection type or a IO type. Required.
        :type properties: ~azure.mgmt.keyvault.v2022_07_01.models.PrivateEndpointConnection or IO
        :keyword content_type: Body Parameter content-type. Known values are: 'application/json'.
         Default value is None.
        :paramtype content_type: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: PrivateEndpointConnection or the result of cls(response)
        :rtype: ~azure.mgmt.keyvault.v2022_07_01.models.PrivateEndpointConnection
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        error_map = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version: str = kwargs.pop("api_version", _params.pop("api-version", "2022-07-01"))
        content_type: Optional[str] = kwargs.pop("content_type", _headers.pop("Content-Type", None))
        cls: ClsType[_models.PrivateEndpointConnection] = kwargs.pop("cls", None)

        content_type = content_type or "application/json"
        _json = None
        _content = None
        if isinstance(properties, (IOBase, bytes)):
            _content = properties
        else:
            _json = self._serialize.body(properties, "PrivateEndpointConnection")

        request = build_put_request(
            resource_group_name=resource_group_name,
            vault_name=vault_name,
            private_endpoint_connection_name=private_endpoint_connection_name,
            subscription_id=self._config.subscription_id,
            api_version=api_version,
            content_type=content_type,
            json=_json,
            content=_content,
            template_url=self.put.metadata["url"],
            headers=_headers,
            params=_params,
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)

        _stream = False
        pipeline_response: PipelineResponse = await self._client._pipeline.run(  # pylint: disable=protected-access
            request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        response_headers = {}
        response_headers["Retry-After"] = self._deserialize("int", response.headers.get("Retry-After"))
        response_headers["Azure-AsyncOperation"] = self._deserialize(
            "str", response.headers.get("Azure-AsyncOperation")
        )

        deserialized = self._deserialize("PrivateEndpointConnection", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, response_headers)

        return deserialized

    put.metadata = {
        "url": "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.KeyVault/vaults/{vaultName}/privateEndpointConnections/{privateEndpointConnectionName}"
    }

    async def _delete_initial(
        self, resource_group_name: str, vault_name: str, private_endpoint_connection_name: str, **kwargs: Any
    ) -> Optional[_models.PrivateEndpointConnection]:
        error_map = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = kwargs.pop("headers", {}) or {}
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version: str = kwargs.pop("api_version", _params.pop("api-version", "2022-07-01"))
        cls: ClsType[Optional[_models.PrivateEndpointConnection]] = kwargs.pop("cls", None)

        request = build_delete_request(
            resource_group_name=resource_group_name,
            vault_name=vault_name,
            private_endpoint_connection_name=private_endpoint_connection_name,
            subscription_id=self._config.subscription_id,
            api_version=api_version,
            template_url=self._delete_initial.metadata["url"],
            headers=_headers,
            params=_params,
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)

        _stream = False
        pipeline_response: PipelineResponse = await self._client._pipeline.run(  # pylint: disable=protected-access
            request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200, 202, 204]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        deserialized = None
        response_headers = {}
        if response.status_code == 200:
            deserialized = self._deserialize("PrivateEndpointConnection", pipeline_response)

        if response.status_code == 202:
            response_headers["Retry-After"] = self._deserialize("int", response.headers.get("Retry-After"))
            response_headers["Location"] = self._deserialize("str", response.headers.get("Location"))

        if cls:
            return cls(pipeline_response, deserialized, response_headers)

        return deserialized

    _delete_initial.metadata = {
        "url": "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.KeyVault/vaults/{vaultName}/privateEndpointConnections/{privateEndpointConnectionName}"
    }

    @distributed_trace_async
    async def begin_delete(
        self, resource_group_name: str, vault_name: str, private_endpoint_connection_name: str, **kwargs: Any
    ) -> AsyncLROPoller[_models.PrivateEndpointConnection]:
        """Deletes the specified private endpoint connection associated with the key vault.

        :param resource_group_name: Name of the resource group that contains the key vault. Required.
        :type resource_group_name: str
        :param vault_name: The name of the key vault. Required.
        :type vault_name: str
        :param private_endpoint_connection_name: Name of the private endpoint connection associated
         with the key vault. Required.
        :type private_endpoint_connection_name: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :keyword str continuation_token: A continuation token to restart a poller from a saved state.
        :keyword polling: By default, your polling method will be AsyncARMPolling. Pass in False for
         this operation to not poll, or pass in your own initialized polling object for a personal
         polling strategy.
        :paramtype polling: bool or ~azure.core.polling.AsyncPollingMethod
        :keyword int polling_interval: Default waiting time between two polls for LRO operations if no
         Retry-After header is present.
        :return: An instance of AsyncLROPoller that returns either PrivateEndpointConnection or the
         result of cls(response)
        :rtype:
         ~azure.core.polling.AsyncLROPoller[~azure.mgmt.keyvault.v2022_07_01.models.PrivateEndpointConnection]
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        _headers = kwargs.pop("headers", {}) or {}
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version: str = kwargs.pop("api_version", _params.pop("api-version", "2022-07-01"))
        cls: ClsType[_models.PrivateEndpointConnection] = kwargs.pop("cls", None)
        polling: Union[bool, AsyncPollingMethod] = kwargs.pop("polling", True)
        lro_delay = kwargs.pop("polling_interval", self._config.polling_interval)
        cont_token: Optional[str] = kwargs.pop("continuation_token", None)
        if cont_token is None:
            raw_result = await self._delete_initial(
                resource_group_name=resource_group_name,
                vault_name=vault_name,
                private_endpoint_connection_name=private_endpoint_connection_name,
                api_version=api_version,
                cls=lambda x, y, z: x,
                headers=_headers,
                params=_params,
                **kwargs
            )
        kwargs.pop("error_map", None)

        def get_long_running_output(pipeline_response):
            deserialized = self._deserialize("PrivateEndpointConnection", pipeline_response)
            if cls:
                return cls(pipeline_response, deserialized, {})
            return deserialized

        if polling is True:
            polling_method: AsyncPollingMethod = cast(AsyncPollingMethod, AsyncARMPolling(lro_delay, **kwargs))
        elif polling is False:
            polling_method = cast(AsyncPollingMethod, AsyncNoPolling())
        else:
            polling_method = polling
        if cont_token:
            return AsyncLROPoller.from_continuation_token(
                polling_method=polling_method,
                continuation_token=cont_token,
                client=self._client,
                deserialization_callback=get_long_running_output,
            )
        return AsyncLROPoller(self._client, raw_result, get_long_running_output, polling_method)  # type: ignore

    begin_delete.metadata = {
        "url": "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.KeyVault/vaults/{vaultName}/privateEndpointConnections/{privateEndpointConnectionName}"
    }

    @distributed_trace
    def list_by_resource(
        self, resource_group_name: str, vault_name: str, **kwargs: Any
    ) -> AsyncIterable["_models.PrivateEndpointConnection"]:
        """The List operation gets information about the private endpoint connections associated with the
        vault.

        :param resource_group_name: Name of the resource group that contains the key vault. Required.
        :type resource_group_name: str
        :param vault_name: The name of the key vault. Required.
        :type vault_name: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: An iterator like instance of either PrivateEndpointConnection or the result of
         cls(response)
        :rtype:
         ~azure.core.async_paging.AsyncItemPaged[~azure.mgmt.keyvault.v2022_07_01.models.PrivateEndpointConnection]
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        _headers = kwargs.pop("headers", {}) or {}
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version: str = kwargs.pop("api_version", _params.pop("api-version", "2022-07-01"))
        cls: ClsType[_models.PrivateEndpointConnectionListResult] = kwargs.pop("cls", None)

        error_map = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        def prepare_request(next_link=None):
            if not next_link:

                request = build_list_by_resource_request(
                    resource_group_name=resource_group_name,
                    vault_name=vault_name,
                    subscription_id=self._config.subscription_id,
                    api_version=api_version,
                    template_url=self.list_by_resource.metadata["url"],
                    headers=_headers,
                    params=_params,
                )
                request = _convert_request(request)
                request.url = self._client.format_url(request.url)

            else:
                # make call to next link with the client's api-version
                _parsed_next_link = urllib.parse.urlparse(next_link)
                _next_request_params = case_insensitive_dict(
                    {
                        key: [urllib.parse.quote(v) for v in value]
                        for key, value in urllib.parse.parse_qs(_parsed_next_link.query).items()
                    }
                )
                _next_request_params["api-version"] = self._config.api_version
                request = HttpRequest(
                    "GET", urllib.parse.urljoin(next_link, _parsed_next_link.path), params=_next_request_params
                )
                request = _convert_request(request)
                request.url = self._client.format_url(request.url)
                request.method = "GET"
            return request

        async def extract_data(pipeline_response):
            deserialized = self._deserialize("PrivateEndpointConnectionListResult", pipeline_response)
            list_of_elem = deserialized.value
            if cls:
                list_of_elem = cls(list_of_elem)  # type: ignore
            return deserialized.next_link or None, AsyncList(list_of_elem)

        async def get_next(next_link=None):
            request = prepare_request(next_link)

            _stream = False
            pipeline_response: PipelineResponse = await self._client._pipeline.run(  # pylint: disable=protected-access
                request, stream=_stream, **kwargs
            )
            response = pipeline_response.http_response

            if response.status_code not in [200]:
                map_error(status_code=response.status_code, response=response, error_map=error_map)
                raise HttpResponseError(response=response, error_format=ARMErrorFormat)

            return pipeline_response

        return AsyncItemPaged(get_next, extract_data)

    list_by_resource.metadata = {
        "url": "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.KeyVault/vaults/{vaultName}/privateEndpointConnections"
    }
