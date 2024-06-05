# pylint: disable=too-many-lines,too-many-statements
# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator (autorest: 3.10.1, generator: @autorest/python@6.13.18)
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from io import IOBase
import sys
from typing import Any, Callable, Dict, IO, Iterable, Optional, Type, TypeVar, Union, overload
import urllib.parse

from azure.core.exceptions import (
    ClientAuthenticationError,
    HttpResponseError,
    ResourceExistsError,
    ResourceNotFoundError,
    ResourceNotModifiedError,
    map_error,
)
from azure.core.paging import ItemPaged
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import HttpResponse
from azure.core.rest import HttpRequest
from azure.core.tracing.decorator import distributed_trace
from azure.core.utils import case_insensitive_dict

from .. import models as _models
from .._serialization import Serializer
from .._vendor import SearchServiceClientMixinABC, _convert_request

if sys.version_info >= (3, 9):
    from collections.abc import MutableMapping
else:
    from typing import MutableMapping  # type: ignore  # pylint: disable=ungrouped-imports
T = TypeVar("T")
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, HttpResponse], T, Dict[str, Any]], Any]]

_SERIALIZER = Serializer()
_SERIALIZER.client_side_validation = False


def build_create_request(*, x_ms_client_request_id: Optional[str] = None, **kwargs: Any) -> HttpRequest:
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
    _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

    api_version: str = kwargs.pop("api_version", _params.pop("api-version", "2024-05-01-preview"))
    content_type: Optional[str] = kwargs.pop("content_type", _headers.pop("Content-Type", None))
    accept = _headers.pop("Accept", "application/json")

    # Construct URL
    _url = kwargs.pop("template_url", "/aliases")

    # Construct parameters
    _params["api-version"] = _SERIALIZER.query("api_version", api_version, "str")

    # Construct headers
    if x_ms_client_request_id is not None:
        _headers["x-ms-client-request-id"] = _SERIALIZER.header("x_ms_client_request_id", x_ms_client_request_id, "str")
    if content_type is not None:
        _headers["Content-Type"] = _SERIALIZER.header("content_type", content_type, "str")
    _headers["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="POST", url=_url, params=_params, headers=_headers, **kwargs)


def build_list_request(*, x_ms_client_request_id: Optional[str] = None, **kwargs: Any) -> HttpRequest:
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
    _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

    api_version: str = kwargs.pop("api_version", _params.pop("api-version", "2024-05-01-preview"))
    accept = _headers.pop("Accept", "application/json")

    # Construct URL
    _url = kwargs.pop("template_url", "/aliases")

    # Construct parameters
    _params["api-version"] = _SERIALIZER.query("api_version", api_version, "str")

    # Construct headers
    if x_ms_client_request_id is not None:
        _headers["x-ms-client-request-id"] = _SERIALIZER.header("x_ms_client_request_id", x_ms_client_request_id, "str")
    _headers["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="GET", url=_url, params=_params, headers=_headers, **kwargs)


def build_create_or_update_request(
    alias_name: str,
    *,
    prefer: Union[str, _models.Enum0],
    x_ms_client_request_id: Optional[str] = None,
    if_match: Optional[str] = None,
    if_none_match: Optional[str] = None,
    **kwargs: Any
) -> HttpRequest:
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
    _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

    api_version: str = kwargs.pop("api_version", _params.pop("api-version", "2024-05-01-preview"))
    content_type: Optional[str] = kwargs.pop("content_type", _headers.pop("Content-Type", None))
    accept = _headers.pop("Accept", "application/json")

    # Construct URL
    _url = kwargs.pop("template_url", "/aliases('{aliasName}')")
    path_format_arguments = {
        "aliasName": _SERIALIZER.url("alias_name", alias_name, "str"),
    }

    _url: str = _url.format(**path_format_arguments)  # type: ignore

    # Construct parameters
    _params["api-version"] = _SERIALIZER.query("api_version", api_version, "str")

    # Construct headers
    if x_ms_client_request_id is not None:
        _headers["x-ms-client-request-id"] = _SERIALIZER.header("x_ms_client_request_id", x_ms_client_request_id, "str")
    if if_match is not None:
        _headers["If-Match"] = _SERIALIZER.header("if_match", if_match, "str")
    if if_none_match is not None:
        _headers["If-None-Match"] = _SERIALIZER.header("if_none_match", if_none_match, "str")
    _headers["Prefer"] = _SERIALIZER.header("prefer", prefer, "str")
    if content_type is not None:
        _headers["Content-Type"] = _SERIALIZER.header("content_type", content_type, "str")
    _headers["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="PUT", url=_url, params=_params, headers=_headers, **kwargs)


def build_delete_request(
    alias_name: str,
    *,
    x_ms_client_request_id: Optional[str] = None,
    if_match: Optional[str] = None,
    if_none_match: Optional[str] = None,
    **kwargs: Any
) -> HttpRequest:
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
    _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

    api_version: str = kwargs.pop("api_version", _params.pop("api-version", "2024-05-01-preview"))
    accept = _headers.pop("Accept", "application/json")

    # Construct URL
    _url = kwargs.pop("template_url", "/aliases('{aliasName}')")
    path_format_arguments = {
        "aliasName": _SERIALIZER.url("alias_name", alias_name, "str"),
    }

    _url: str = _url.format(**path_format_arguments)  # type: ignore

    # Construct parameters
    _params["api-version"] = _SERIALIZER.query("api_version", api_version, "str")

    # Construct headers
    if x_ms_client_request_id is not None:
        _headers["x-ms-client-request-id"] = _SERIALIZER.header("x_ms_client_request_id", x_ms_client_request_id, "str")
    if if_match is not None:
        _headers["If-Match"] = _SERIALIZER.header("if_match", if_match, "str")
    if if_none_match is not None:
        _headers["If-None-Match"] = _SERIALIZER.header("if_none_match", if_none_match, "str")
    _headers["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="DELETE", url=_url, params=_params, headers=_headers, **kwargs)


def build_get_request(alias_name: str, *, x_ms_client_request_id: Optional[str] = None, **kwargs: Any) -> HttpRequest:
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
    _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

    api_version: str = kwargs.pop("api_version", _params.pop("api-version", "2024-05-01-preview"))
    accept = _headers.pop("Accept", "application/json")

    # Construct URL
    _url = kwargs.pop("template_url", "/aliases('{aliasName}')")
    path_format_arguments = {
        "aliasName": _SERIALIZER.url("alias_name", alias_name, "str"),
    }

    _url: str = _url.format(**path_format_arguments)  # type: ignore

    # Construct parameters
    _params["api-version"] = _SERIALIZER.query("api_version", api_version, "str")

    # Construct headers
    if x_ms_client_request_id is not None:
        _headers["x-ms-client-request-id"] = _SERIALIZER.header("x_ms_client_request_id", x_ms_client_request_id, "str")
    _headers["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="GET", url=_url, params=_params, headers=_headers, **kwargs)


class AliasesOperations:
    """
    .. warning::
        **DO NOT** instantiate this class directly.

        Instead, you should access the following operations through
        :class:`~azure.search.documents.indexes.SearchServiceClient`'s
        :attr:`aliases` attribute.
    """

    models = _models

    def __init__(self, *args, **kwargs):
        input_args = list(args)
        self._client = input_args.pop(0) if input_args else kwargs.pop("client")
        self._config = input_args.pop(0) if input_args else kwargs.pop("config")
        self._serialize = input_args.pop(0) if input_args else kwargs.pop("serializer")
        self._deserialize = input_args.pop(0) if input_args else kwargs.pop("deserializer")

    @overload
    def create(
        self,
        alias: _models.SearchAlias,
        request_options: Optional[_models.RequestOptions] = None,
        *,
        content_type: str = "application/json",
        **kwargs: Any
    ) -> _models.SearchAlias:
        """Creates a new search alias.

        .. seealso::
           - https://docs.microsoft.com/rest/api/searchservice/Create-Alias

        :param alias: The definition of the alias to create. Required.
        :type alias: ~azure.search.documents.indexes.models.SearchAlias
        :param request_options: Parameter group. Default value is None.
        :type request_options: ~azure.search.documents.indexes.models.RequestOptions
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: SearchAlias or the result of cls(response)
        :rtype: ~azure.search.documents.indexes.models.SearchAlias
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @overload
    def create(
        self,
        alias: IO[bytes],
        request_options: Optional[_models.RequestOptions] = None,
        *,
        content_type: str = "application/json",
        **kwargs: Any
    ) -> _models.SearchAlias:
        """Creates a new search alias.

        .. seealso::
           - https://docs.microsoft.com/rest/api/searchservice/Create-Alias

        :param alias: The definition of the alias to create. Required.
        :type alias: IO[bytes]
        :param request_options: Parameter group. Default value is None.
        :type request_options: ~azure.search.documents.indexes.models.RequestOptions
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: SearchAlias or the result of cls(response)
        :rtype: ~azure.search.documents.indexes.models.SearchAlias
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @distributed_trace
    def create(
        self,
        alias: Union[_models.SearchAlias, IO[bytes]],
        request_options: Optional[_models.RequestOptions] = None,
        **kwargs: Any
    ) -> _models.SearchAlias:
        """Creates a new search alias.

        .. seealso::
           - https://docs.microsoft.com/rest/api/searchservice/Create-Alias

        :param alias: The definition of the alias to create. Is either a SearchAlias type or a
         IO[bytes] type. Required.
        :type alias: ~azure.search.documents.indexes.models.SearchAlias or IO[bytes]
        :param request_options: Parameter group. Default value is None.
        :type request_options: ~azure.search.documents.indexes.models.RequestOptions
        :return: SearchAlias or the result of cls(response)
        :rtype: ~azure.search.documents.indexes.models.SearchAlias
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        error_map: MutableMapping[int, Type[HttpResponseError]] = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version: str = kwargs.pop("api_version", _params.pop("api-version", self._config.api_version))
        content_type: Optional[str] = kwargs.pop("content_type", _headers.pop("Content-Type", None))
        cls: ClsType[_models.SearchAlias] = kwargs.pop("cls", None)

        _x_ms_client_request_id = None
        if request_options is not None:
            _x_ms_client_request_id = request_options.x_ms_client_request_id
        content_type = content_type or "application/json"
        _json = None
        _content = None
        if isinstance(alias, (IOBase, bytes)):
            _content = alias
        else:
            _json = self._serialize.body(alias, "SearchAlias")

        _request = build_create_request(
            x_ms_client_request_id=_x_ms_client_request_id,
            api_version=api_version,
            content_type=content_type,
            json=_json,
            content=_content,
            headers=_headers,
            params=_params,
        )
        _request = _convert_request(_request)
        path_format_arguments = {
            "endpoint": self._serialize.url("self._config.endpoint", self._config.endpoint, "str", skip_quote=True),
        }
        _request.url = self._client.format_url(_request.url, **path_format_arguments)

        _stream = False
        pipeline_response: PipelineResponse = self._client._pipeline.run(  # pylint: disable=protected-access
            _request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [201]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.ErrorResponse, pipeline_response)
            raise HttpResponseError(response=response, model=error)

        deserialized = self._deserialize("SearchAlias", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})  # type: ignore

        return deserialized  # type: ignore

    @distributed_trace
    def list(
        self, request_options: Optional[_models.RequestOptions] = None, **kwargs: Any
    ) -> Iterable["_models.SearchAlias"]:
        """Lists all aliases available for a search service.

        .. seealso::
           - https://docs.microsoft.com/rest/api/searchservice/List-Aliases

        :param request_options: Parameter group. Default value is None.
        :type request_options: ~azure.search.documents.indexes.models.RequestOptions
        :return: An iterator like instance of either SearchAlias or the result of cls(response)
        :rtype: ~azure.core.paging.ItemPaged[~azure.search.documents.indexes.models.SearchAlias]
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        _headers = kwargs.pop("headers", {}) or {}
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version: str = kwargs.pop("api_version", _params.pop("api-version", self._config.api_version))
        cls: ClsType[_models.ListAliasesResult] = kwargs.pop("cls", None)

        error_map: MutableMapping[int, Type[HttpResponseError]] = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        def prepare_request(next_link=None):
            if not next_link:
                _x_ms_client_request_id = None
                if request_options is not None:
                    _x_ms_client_request_id = request_options.x_ms_client_request_id

                _request = build_list_request(
                    x_ms_client_request_id=_x_ms_client_request_id,
                    api_version=api_version,
                    headers=_headers,
                    params=_params,
                )
                _request = _convert_request(_request)
                path_format_arguments = {
                    "endpoint": self._serialize.url(
                        "self._config.endpoint", self._config.endpoint, "str", skip_quote=True
                    ),
                }
                _request.url = self._client.format_url(_request.url, **path_format_arguments)

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
                _request = HttpRequest(
                    "GET", urllib.parse.urljoin(next_link, _parsed_next_link.path), params=_next_request_params
                )
                _request = _convert_request(_request)
                path_format_arguments = {
                    "endpoint": self._serialize.url(
                        "self._config.endpoint", self._config.endpoint, "str", skip_quote=True
                    ),
                }
                _request.url = self._client.format_url(_request.url, **path_format_arguments)
                _request.method = "GET"
            return _request

        def extract_data(pipeline_response):
            deserialized = self._deserialize("ListAliasesResult", pipeline_response)
            list_of_elem = deserialized.aliases
            if cls:
                list_of_elem = cls(list_of_elem)  # type: ignore
            return None, iter(list_of_elem)

        def get_next(next_link=None):
            _request = prepare_request(next_link)

            _stream = False
            pipeline_response: PipelineResponse = self._client._pipeline.run(  # pylint: disable=protected-access
                _request, stream=_stream, **kwargs
            )
            response = pipeline_response.http_response

            if response.status_code not in [200]:
                map_error(status_code=response.status_code, response=response, error_map=error_map)
                error = self._deserialize.failsafe_deserialize(_models.ErrorResponse, pipeline_response)
                raise HttpResponseError(response=response, model=error)

            return pipeline_response

        return ItemPaged(get_next, extract_data)

    @overload
    def create_or_update(
        self,
        alias_name: str,
        prefer: Union[str, _models.Enum0],
        alias: _models.SearchAlias,
        if_match: Optional[str] = None,
        if_none_match: Optional[str] = None,
        request_options: Optional[_models.RequestOptions] = None,
        *,
        content_type: str = "application/json",
        **kwargs: Any
    ) -> _models.SearchAlias:
        """Creates a new search alias or updates an alias if it already exists.

        .. seealso::
           - https://docs.microsoft.com/rest/api/searchservice/Update-Alias

        :param alias_name: The definition of the alias to create or update. Required.
        :type alias_name: str
        :param prefer: For HTTP PUT requests, instructs the service to return the created/updated
         resource on success. "return=representation" Required.
        :type prefer: str or ~azure.search.documents.indexes.models.Enum0
        :param alias: The definition of the alias to create or update. Required.
        :type alias: ~azure.search.documents.indexes.models.SearchAlias
        :param if_match: Defines the If-Match condition. The operation will be performed only if the
         ETag on the server matches this value. Default value is None.
        :type if_match: str
        :param if_none_match: Defines the If-None-Match condition. The operation will be performed only
         if the ETag on the server does not match this value. Default value is None.
        :type if_none_match: str
        :param request_options: Parameter group. Default value is None.
        :type request_options: ~azure.search.documents.indexes.models.RequestOptions
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: SearchAlias or the result of cls(response)
        :rtype: ~azure.search.documents.indexes.models.SearchAlias
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @overload
    def create_or_update(
        self,
        alias_name: str,
        prefer: Union[str, _models.Enum0],
        alias: IO[bytes],
        if_match: Optional[str] = None,
        if_none_match: Optional[str] = None,
        request_options: Optional[_models.RequestOptions] = None,
        *,
        content_type: str = "application/json",
        **kwargs: Any
    ) -> _models.SearchAlias:
        """Creates a new search alias or updates an alias if it already exists.

        .. seealso::
           - https://docs.microsoft.com/rest/api/searchservice/Update-Alias

        :param alias_name: The definition of the alias to create or update. Required.
        :type alias_name: str
        :param prefer: For HTTP PUT requests, instructs the service to return the created/updated
         resource on success. "return=representation" Required.
        :type prefer: str or ~azure.search.documents.indexes.models.Enum0
        :param alias: The definition of the alias to create or update. Required.
        :type alias: IO[bytes]
        :param if_match: Defines the If-Match condition. The operation will be performed only if the
         ETag on the server matches this value. Default value is None.
        :type if_match: str
        :param if_none_match: Defines the If-None-Match condition. The operation will be performed only
         if the ETag on the server does not match this value. Default value is None.
        :type if_none_match: str
        :param request_options: Parameter group. Default value is None.
        :type request_options: ~azure.search.documents.indexes.models.RequestOptions
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: SearchAlias or the result of cls(response)
        :rtype: ~azure.search.documents.indexes.models.SearchAlias
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @distributed_trace
    def create_or_update(
        self,
        alias_name: str,
        prefer: Union[str, _models.Enum0],
        alias: Union[_models.SearchAlias, IO[bytes]],
        if_match: Optional[str] = None,
        if_none_match: Optional[str] = None,
        request_options: Optional[_models.RequestOptions] = None,
        **kwargs: Any
    ) -> _models.SearchAlias:
        """Creates a new search alias or updates an alias if it already exists.

        .. seealso::
           - https://docs.microsoft.com/rest/api/searchservice/Update-Alias

        :param alias_name: The definition of the alias to create or update. Required.
        :type alias_name: str
        :param prefer: For HTTP PUT requests, instructs the service to return the created/updated
         resource on success. "return=representation" Required.
        :type prefer: str or ~azure.search.documents.indexes.models.Enum0
        :param alias: The definition of the alias to create or update. Is either a SearchAlias type or
         a IO[bytes] type. Required.
        :type alias: ~azure.search.documents.indexes.models.SearchAlias or IO[bytes]
        :param if_match: Defines the If-Match condition. The operation will be performed only if the
         ETag on the server matches this value. Default value is None.
        :type if_match: str
        :param if_none_match: Defines the If-None-Match condition. The operation will be performed only
         if the ETag on the server does not match this value. Default value is None.
        :type if_none_match: str
        :param request_options: Parameter group. Default value is None.
        :type request_options: ~azure.search.documents.indexes.models.RequestOptions
        :return: SearchAlias or the result of cls(response)
        :rtype: ~azure.search.documents.indexes.models.SearchAlias
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        error_map: MutableMapping[int, Type[HttpResponseError]] = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version: str = kwargs.pop("api_version", _params.pop("api-version", self._config.api_version))
        content_type: Optional[str] = kwargs.pop("content_type", _headers.pop("Content-Type", None))
        cls: ClsType[_models.SearchAlias] = kwargs.pop("cls", None)

        _x_ms_client_request_id = None
        if request_options is not None:
            _x_ms_client_request_id = request_options.x_ms_client_request_id
        content_type = content_type or "application/json"
        _json = None
        _content = None
        if isinstance(alias, (IOBase, bytes)):
            _content = alias
        else:
            _json = self._serialize.body(alias, "SearchAlias")

        _request = build_create_or_update_request(
            alias_name=alias_name,
            prefer=prefer,
            x_ms_client_request_id=_x_ms_client_request_id,
            if_match=if_match,
            if_none_match=if_none_match,
            api_version=api_version,
            content_type=content_type,
            json=_json,
            content=_content,
            headers=_headers,
            params=_params,
        )
        _request = _convert_request(_request)
        path_format_arguments = {
            "endpoint": self._serialize.url("self._config.endpoint", self._config.endpoint, "str", skip_quote=True),
        }
        _request.url = self._client.format_url(_request.url, **path_format_arguments)

        _stream = False
        pipeline_response: PipelineResponse = self._client._pipeline.run(  # pylint: disable=protected-access
            _request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200, 201]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.ErrorResponse, pipeline_response)
            raise HttpResponseError(response=response, model=error)

        if response.status_code == 200:
            deserialized = self._deserialize("SearchAlias", pipeline_response)

        if response.status_code == 201:
            deserialized = self._deserialize("SearchAlias", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})  # type: ignore

        return deserialized  # type: ignore

    @distributed_trace
    def delete(  # pylint: disable=inconsistent-return-statements
        self,
        alias_name: str,
        if_match: Optional[str] = None,
        if_none_match: Optional[str] = None,
        request_options: Optional[_models.RequestOptions] = None,
        **kwargs: Any
    ) -> None:
        """Deletes a search alias and its associated mapping to an index. This operation is permanent,
        with no recovery option. The mapped index is untouched by this operation.

        .. seealso::
           - https://docs.microsoft.com/rest/api/searchservice/Delete-Alias

        :param alias_name: The name of the alias to delete. Required.
        :type alias_name: str
        :param if_match: Defines the If-Match condition. The operation will be performed only if the
         ETag on the server matches this value. Default value is None.
        :type if_match: str
        :param if_none_match: Defines the If-None-Match condition. The operation will be performed only
         if the ETag on the server does not match this value. Default value is None.
        :type if_none_match: str
        :param request_options: Parameter group. Default value is None.
        :type request_options: ~azure.search.documents.indexes.models.RequestOptions
        :return: None or the result of cls(response)
        :rtype: None
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        error_map: MutableMapping[int, Type[HttpResponseError]] = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = kwargs.pop("headers", {}) or {}
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version: str = kwargs.pop("api_version", _params.pop("api-version", self._config.api_version))
        cls: ClsType[None] = kwargs.pop("cls", None)

        _x_ms_client_request_id = None
        if request_options is not None:
            _x_ms_client_request_id = request_options.x_ms_client_request_id

        _request = build_delete_request(
            alias_name=alias_name,
            x_ms_client_request_id=_x_ms_client_request_id,
            if_match=if_match,
            if_none_match=if_none_match,
            api_version=api_version,
            headers=_headers,
            params=_params,
        )
        _request = _convert_request(_request)
        path_format_arguments = {
            "endpoint": self._serialize.url("self._config.endpoint", self._config.endpoint, "str", skip_quote=True),
        }
        _request.url = self._client.format_url(_request.url, **path_format_arguments)

        _stream = False
        pipeline_response: PipelineResponse = self._client._pipeline.run(  # pylint: disable=protected-access
            _request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [204, 404]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.ErrorResponse, pipeline_response)
            raise HttpResponseError(response=response, model=error)

        if cls:
            return cls(pipeline_response, None, {})  # type: ignore

    @distributed_trace
    def get(
        self, alias_name: str, request_options: Optional[_models.RequestOptions] = None, **kwargs: Any
    ) -> _models.SearchAlias:
        """Retrieves an alias definition.

        .. seealso::
           - https://docs.microsoft.com/rest/api/searchservice/Get-Alias

        :param alias_name: The name of the alias to retrieve. Required.
        :type alias_name: str
        :param request_options: Parameter group. Default value is None.
        :type request_options: ~azure.search.documents.indexes.models.RequestOptions
        :return: SearchAlias or the result of cls(response)
        :rtype: ~azure.search.documents.indexes.models.SearchAlias
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        error_map: MutableMapping[int, Type[HttpResponseError]] = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = kwargs.pop("headers", {}) or {}
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version: str = kwargs.pop("api_version", _params.pop("api-version", self._config.api_version))
        cls: ClsType[_models.SearchAlias] = kwargs.pop("cls", None)

        _x_ms_client_request_id = None
        if request_options is not None:
            _x_ms_client_request_id = request_options.x_ms_client_request_id

        _request = build_get_request(
            alias_name=alias_name,
            x_ms_client_request_id=_x_ms_client_request_id,
            api_version=api_version,
            headers=_headers,
            params=_params,
        )
        _request = _convert_request(_request)
        path_format_arguments = {
            "endpoint": self._serialize.url("self._config.endpoint", self._config.endpoint, "str", skip_quote=True),
        }
        _request.url = self._client.format_url(_request.url, **path_format_arguments)

        _stream = False
        pipeline_response: PipelineResponse = self._client._pipeline.run(  # pylint: disable=protected-access
            _request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.ErrorResponse, pipeline_response)
            raise HttpResponseError(response=response, model=error)

        deserialized = self._deserialize("SearchAlias", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})  # type: ignore

        return deserialized  # type: ignore
