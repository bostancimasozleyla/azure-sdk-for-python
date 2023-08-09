# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from typing import Any, Optional, TYPE_CHECKING

from azure.mgmt.core import ARMPipelineClient
from azure.profiles import KnownProfiles, ProfileDefinition
from azure.profiles.multiapiclient import MultiApiClientMixin

from ._configuration import PolicyClientConfiguration
from ._serialization import Deserializer, Serializer

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from azure.core.credentials import TokenCredential

class _SDKClient(object):
    def __init__(self, *args, **kwargs):
        """This is a fake class to support current implemetation of MultiApiClientMixin."
        Will be removed in final version of multiapi azure-core based client
        """
        pass

class PolicyClient(MultiApiClientMixin, _SDKClient):
    """To manage and control access to your resources, you can define customized policies and assign them at a scope.

    This ready contains multiple API versions, to help you deal with all of the Azure clouds
    (Azure Stack, Azure Government, Azure China, etc.).
    By default, it uses the latest API version available on public Azure.
    For production, you should stick to a particular api-version and/or profile.
    The profile sets a mapping between an operation group and its API version.
    The api-version parameter sets the default API version if the operation
    group is not described in the profile.

    :param credential: Credential needed for the client to connect to Azure. Required.
    :type credential: ~azure.core.credentials.TokenCredential
    :param subscription_id: The ID of the target subscription. Required.
    :type subscription_id: str
    :param api_version: API version to use if no profile is provided, or if missing in profile.
    :type api_version: str
    :param base_url: Service URL
    :type base_url: str
    :param profile: A profile definition, from KnownProfiles to dict.
    :type profile: azure.profiles.KnownProfiles
    """

    DEFAULT_API_VERSION = '2022-06-01'
    _PROFILE_TAG = "azure.mgmt.resource.policy.PolicyClient"
    LATEST_PROFILE = ProfileDefinition({
        _PROFILE_TAG: {
            None: DEFAULT_API_VERSION,
            'data_policy_manifests': '2020-09-01',
            'policy_definitions': '2021-06-01',
            'policy_set_definitions': '2021-06-01',
        }},
        _PROFILE_TAG + " latest"
    )

    def __init__(
        self,
        credential: "TokenCredential",
        subscription_id: str,
        api_version: Optional[str]=None,
        base_url: str = "https://management.azure.com",
        profile: KnownProfiles=KnownProfiles.default,
        **kwargs: Any
    ):
        self._config = PolicyClientConfiguration(credential, subscription_id, **kwargs)
        self._client = ARMPipelineClient(base_url=base_url, config=self._config, **kwargs)
        super(PolicyClient, self).__init__(
            api_version=api_version,
            profile=profile
        )

    @classmethod
    def _models_dict(cls, api_version):
        return {k: v for k, v in cls.models(api_version).__dict__.items() if isinstance(v, type)}

    @classmethod
    def models(cls, api_version=DEFAULT_API_VERSION):
        """Module depends on the API version:

           * 2015-10-01-preview: :mod:`v2015_10_01_preview.models<azure.mgmt.resource.policy.v2015_10_01_preview.models>`
           * 2016-04-01: :mod:`v2016_04_01.models<azure.mgmt.resource.policy.v2016_04_01.models>`
           * 2016-12-01: :mod:`v2016_12_01.models<azure.mgmt.resource.policy.v2016_12_01.models>`
           * 2017-06-01-preview: :mod:`v2017_06_01_preview.models<azure.mgmt.resource.policy.v2017_06_01_preview.models>`
           * 2018-03-01: :mod:`v2018_03_01.models<azure.mgmt.resource.policy.v2018_03_01.models>`
           * 2018-05-01: :mod:`v2018_05_01.models<azure.mgmt.resource.policy.v2018_05_01.models>`
           * 2019-01-01: :mod:`v2019_01_01.models<azure.mgmt.resource.policy.v2019_01_01.models>`
           * 2019-06-01: :mod:`v2019_06_01.models<azure.mgmt.resource.policy.v2019_06_01.models>`
           * 2019-09-01: :mod:`v2019_09_01.models<azure.mgmt.resource.policy.v2019_09_01.models>`
           * 2020-07-01-preview: :mod:`v2020_07_01_preview.models<azure.mgmt.resource.policy.v2020_07_01_preview.models>`
           * 2020-09-01: :mod:`v2020_09_01.models<azure.mgmt.resource.policy.v2020_09_01.models>`
           * 2021-06-01: :mod:`v2021_06_01.models<azure.mgmt.resource.policy.v2021_06_01.models>`
           * 2022-06-01: :mod:`v2022_06_01.models<azure.mgmt.resource.policy.v2022_06_01.models>`
           * 2022-07-01-preview: :mod:`v2022_07_01_preview.models<azure.mgmt.resource.policy.v2022_07_01_preview.models>`
           * 2022-08-01-preview: :mod:`v2022_08_01_preview.models<azure.mgmt.resource.policy.v2022_08_01_preview.models>`
        """
        if api_version == '2015-10-01-preview':
            from .v2015_10_01_preview import models
            return models
        elif api_version == '2016-04-01':
            from .v2016_04_01 import models
            return models
        elif api_version == '2016-12-01':
            from .v2016_12_01 import models
            return models
        elif api_version == '2017-06-01-preview':
            from .v2017_06_01_preview import models
            return models
        elif api_version == '2018-03-01':
            from .v2018_03_01 import models
            return models
        elif api_version == '2018-05-01':
            from .v2018_05_01 import models
            return models
        elif api_version == '2019-01-01':
            from .v2019_01_01 import models
            return models
        elif api_version == '2019-06-01':
            from .v2019_06_01 import models
            return models
        elif api_version == '2019-09-01':
            from .v2019_09_01 import models
            return models
        elif api_version == '2020-07-01-preview':
            from .v2020_07_01_preview import models
            return models
        elif api_version == '2020-09-01':
            from .v2020_09_01 import models
            return models
        elif api_version == '2021-06-01':
            from .v2021_06_01 import models
            return models
        elif api_version == '2022-06-01':
            from .v2022_06_01 import models
            return models
        elif api_version == '2022-07-01-preview':
            from .v2022_07_01_preview import models
            return models
        elif api_version == '2022-08-01-preview':
            from .v2022_08_01_preview import models
            return models
        raise ValueError("API version {} is not available".format(api_version))

    @property
    def data_policy_manifests(self):
        """Instance depends on the API version:

           * 2020-09-01: :class:`DataPolicyManifestsOperations<azure.mgmt.resource.policy.v2020_09_01.operations.DataPolicyManifestsOperations>`
        """
        api_version = self._get_api_version('data_policy_manifests')
        if api_version == '2020-09-01':
            from .v2020_09_01.operations import DataPolicyManifestsOperations as OperationClass
        else:
            raise ValueError("API version {} does not have operation group 'data_policy_manifests'".format(api_version))
        self._config.api_version = api_version
        return OperationClass(self._client, self._config, Serializer(self._models_dict(api_version)), Deserializer(self._models_dict(api_version)))

    @property
    def policy_assignments(self):
        """Instance depends on the API version:

           * 2015-10-01-preview: :class:`PolicyAssignmentsOperations<azure.mgmt.resource.policy.v2015_10_01_preview.operations.PolicyAssignmentsOperations>`
           * 2016-04-01: :class:`PolicyAssignmentsOperations<azure.mgmt.resource.policy.v2016_04_01.operations.PolicyAssignmentsOperations>`
           * 2016-12-01: :class:`PolicyAssignmentsOperations<azure.mgmt.resource.policy.v2016_12_01.operations.PolicyAssignmentsOperations>`
           * 2017-06-01-preview: :class:`PolicyAssignmentsOperations<azure.mgmt.resource.policy.v2017_06_01_preview.operations.PolicyAssignmentsOperations>`
           * 2018-03-01: :class:`PolicyAssignmentsOperations<azure.mgmt.resource.policy.v2018_03_01.operations.PolicyAssignmentsOperations>`
           * 2018-05-01: :class:`PolicyAssignmentsOperations<azure.mgmt.resource.policy.v2018_05_01.operations.PolicyAssignmentsOperations>`
           * 2019-01-01: :class:`PolicyAssignmentsOperations<azure.mgmt.resource.policy.v2019_01_01.operations.PolicyAssignmentsOperations>`
           * 2019-06-01: :class:`PolicyAssignmentsOperations<azure.mgmt.resource.policy.v2019_06_01.operations.PolicyAssignmentsOperations>`
           * 2019-09-01: :class:`PolicyAssignmentsOperations<azure.mgmt.resource.policy.v2019_09_01.operations.PolicyAssignmentsOperations>`
           * 2020-09-01: :class:`PolicyAssignmentsOperations<azure.mgmt.resource.policy.v2020_09_01.operations.PolicyAssignmentsOperations>`
           * 2021-06-01: :class:`PolicyAssignmentsOperations<azure.mgmt.resource.policy.v2021_06_01.operations.PolicyAssignmentsOperations>`
           * 2022-06-01: :class:`PolicyAssignmentsOperations<azure.mgmt.resource.policy.v2022_06_01.operations.PolicyAssignmentsOperations>`
        """
        api_version = self._get_api_version('policy_assignments')
        if api_version == '2015-10-01-preview':
            from .v2015_10_01_preview.operations import PolicyAssignmentsOperations as OperationClass
        elif api_version == '2016-04-01':
            from .v2016_04_01.operations import PolicyAssignmentsOperations as OperationClass
        elif api_version == '2016-12-01':
            from .v2016_12_01.operations import PolicyAssignmentsOperations as OperationClass
        elif api_version == '2017-06-01-preview':
            from .v2017_06_01_preview.operations import PolicyAssignmentsOperations as OperationClass
        elif api_version == '2018-03-01':
            from .v2018_03_01.operations import PolicyAssignmentsOperations as OperationClass
        elif api_version == '2018-05-01':
            from .v2018_05_01.operations import PolicyAssignmentsOperations as OperationClass
        elif api_version == '2019-01-01':
            from .v2019_01_01.operations import PolicyAssignmentsOperations as OperationClass
        elif api_version == '2019-06-01':
            from .v2019_06_01.operations import PolicyAssignmentsOperations as OperationClass
        elif api_version == '2019-09-01':
            from .v2019_09_01.operations import PolicyAssignmentsOperations as OperationClass
        elif api_version == '2020-09-01':
            from .v2020_09_01.operations import PolicyAssignmentsOperations as OperationClass
        elif api_version == '2021-06-01':
            from .v2021_06_01.operations import PolicyAssignmentsOperations as OperationClass
        elif api_version == '2022-06-01':
            from .v2022_06_01.operations import PolicyAssignmentsOperations as OperationClass
        else:
            raise ValueError("API version {} does not have operation group 'policy_assignments'".format(api_version))
        self._config.api_version = api_version
        return OperationClass(self._client, self._config, Serializer(self._models_dict(api_version)), Deserializer(self._models_dict(api_version)))

    @property
    def policy_definitions(self):
        """Instance depends on the API version:

           * 2015-10-01-preview: :class:`PolicyDefinitionsOperations<azure.mgmt.resource.policy.v2015_10_01_preview.operations.PolicyDefinitionsOperations>`
           * 2016-04-01: :class:`PolicyDefinitionsOperations<azure.mgmt.resource.policy.v2016_04_01.operations.PolicyDefinitionsOperations>`
           * 2016-12-01: :class:`PolicyDefinitionsOperations<azure.mgmt.resource.policy.v2016_12_01.operations.PolicyDefinitionsOperations>`
           * 2018-03-01: :class:`PolicyDefinitionsOperations<azure.mgmt.resource.policy.v2018_03_01.operations.PolicyDefinitionsOperations>`
           * 2018-05-01: :class:`PolicyDefinitionsOperations<azure.mgmt.resource.policy.v2018_05_01.operations.PolicyDefinitionsOperations>`
           * 2019-01-01: :class:`PolicyDefinitionsOperations<azure.mgmt.resource.policy.v2019_01_01.operations.PolicyDefinitionsOperations>`
           * 2019-06-01: :class:`PolicyDefinitionsOperations<azure.mgmt.resource.policy.v2019_06_01.operations.PolicyDefinitionsOperations>`
           * 2019-09-01: :class:`PolicyDefinitionsOperations<azure.mgmt.resource.policy.v2019_09_01.operations.PolicyDefinitionsOperations>`
           * 2020-09-01: :class:`PolicyDefinitionsOperations<azure.mgmt.resource.policy.v2020_09_01.operations.PolicyDefinitionsOperations>`
           * 2021-06-01: :class:`PolicyDefinitionsOperations<azure.mgmt.resource.policy.v2021_06_01.operations.PolicyDefinitionsOperations>`
        """
        api_version = self._get_api_version('policy_definitions')
        if api_version == '2015-10-01-preview':
            from .v2015_10_01_preview.operations import PolicyDefinitionsOperations as OperationClass
        elif api_version == '2016-04-01':
            from .v2016_04_01.operations import PolicyDefinitionsOperations as OperationClass
        elif api_version == '2016-12-01':
            from .v2016_12_01.operations import PolicyDefinitionsOperations as OperationClass
        elif api_version == '2018-03-01':
            from .v2018_03_01.operations import PolicyDefinitionsOperations as OperationClass
        elif api_version == '2018-05-01':
            from .v2018_05_01.operations import PolicyDefinitionsOperations as OperationClass
        elif api_version == '2019-01-01':
            from .v2019_01_01.operations import PolicyDefinitionsOperations as OperationClass
        elif api_version == '2019-06-01':
            from .v2019_06_01.operations import PolicyDefinitionsOperations as OperationClass
        elif api_version == '2019-09-01':
            from .v2019_09_01.operations import PolicyDefinitionsOperations as OperationClass
        elif api_version == '2020-09-01':
            from .v2020_09_01.operations import PolicyDefinitionsOperations as OperationClass
        elif api_version == '2021-06-01':
            from .v2021_06_01.operations import PolicyDefinitionsOperations as OperationClass
        else:
            raise ValueError("API version {} does not have operation group 'policy_definitions'".format(api_version))
        self._config.api_version = api_version
        return OperationClass(self._client, self._config, Serializer(self._models_dict(api_version)), Deserializer(self._models_dict(api_version)))

    @property
    def policy_exemptions(self):
        """Instance depends on the API version:

           * 2020-07-01-preview: :class:`PolicyExemptionsOperations<azure.mgmt.resource.policy.v2020_07_01_preview.operations.PolicyExemptionsOperations>`
           * 2022-07-01-preview: :class:`PolicyExemptionsOperations<azure.mgmt.resource.policy.v2022_07_01_preview.operations.PolicyExemptionsOperations>`
        """
        api_version = self._get_api_version('policy_exemptions')
        if api_version == '2020-07-01-preview':
            from .v2020_07_01_preview.operations import PolicyExemptionsOperations as OperationClass
        elif api_version == '2022-07-01-preview':
            from .v2022_07_01_preview.operations import PolicyExemptionsOperations as OperationClass
        else:
            raise ValueError("API version {} does not have operation group 'policy_exemptions'".format(api_version))
        self._config.api_version = api_version
        return OperationClass(self._client, self._config, Serializer(self._models_dict(api_version)), Deserializer(self._models_dict(api_version)))

    @property
    def policy_set_definitions(self):
        """Instance depends on the API version:

           * 2017-06-01-preview: :class:`PolicySetDefinitionsOperations<azure.mgmt.resource.policy.v2017_06_01_preview.operations.PolicySetDefinitionsOperations>`
           * 2018-03-01: :class:`PolicySetDefinitionsOperations<azure.mgmt.resource.policy.v2018_03_01.operations.PolicySetDefinitionsOperations>`
           * 2018-05-01: :class:`PolicySetDefinitionsOperations<azure.mgmt.resource.policy.v2018_05_01.operations.PolicySetDefinitionsOperations>`
           * 2019-01-01: :class:`PolicySetDefinitionsOperations<azure.mgmt.resource.policy.v2019_01_01.operations.PolicySetDefinitionsOperations>`
           * 2019-06-01: :class:`PolicySetDefinitionsOperations<azure.mgmt.resource.policy.v2019_06_01.operations.PolicySetDefinitionsOperations>`
           * 2019-09-01: :class:`PolicySetDefinitionsOperations<azure.mgmt.resource.policy.v2019_09_01.operations.PolicySetDefinitionsOperations>`
           * 2020-09-01: :class:`PolicySetDefinitionsOperations<azure.mgmt.resource.policy.v2020_09_01.operations.PolicySetDefinitionsOperations>`
           * 2021-06-01: :class:`PolicySetDefinitionsOperations<azure.mgmt.resource.policy.v2021_06_01.operations.PolicySetDefinitionsOperations>`
        """
        api_version = self._get_api_version('policy_set_definitions')
        if api_version == '2017-06-01-preview':
            from .v2017_06_01_preview.operations import PolicySetDefinitionsOperations as OperationClass
        elif api_version == '2018-03-01':
            from .v2018_03_01.operations import PolicySetDefinitionsOperations as OperationClass
        elif api_version == '2018-05-01':
            from .v2018_05_01.operations import PolicySetDefinitionsOperations as OperationClass
        elif api_version == '2019-01-01':
            from .v2019_01_01.operations import PolicySetDefinitionsOperations as OperationClass
        elif api_version == '2019-06-01':
            from .v2019_06_01.operations import PolicySetDefinitionsOperations as OperationClass
        elif api_version == '2019-09-01':
            from .v2019_09_01.operations import PolicySetDefinitionsOperations as OperationClass
        elif api_version == '2020-09-01':
            from .v2020_09_01.operations import PolicySetDefinitionsOperations as OperationClass
        elif api_version == '2021-06-01':
            from .v2021_06_01.operations import PolicySetDefinitionsOperations as OperationClass
        else:
            raise ValueError("API version {} does not have operation group 'policy_set_definitions'".format(api_version))
        self._config.api_version = api_version
        return OperationClass(self._client, self._config, Serializer(self._models_dict(api_version)), Deserializer(self._models_dict(api_version)))

    @property
    def variable_values(self):
        """Instance depends on the API version:

           * 2022-08-01-preview: :class:`VariableValuesOperations<azure.mgmt.resource.policy.v2022_08_01_preview.operations.VariableValuesOperations>`
        """
        api_version = self._get_api_version('variable_values')
        if api_version == '2022-08-01-preview':
            from .v2022_08_01_preview.operations import VariableValuesOperations as OperationClass
        else:
            raise ValueError("API version {} does not have operation group 'variable_values'".format(api_version))
        self._config.api_version = api_version
        return OperationClass(self._client, self._config, Serializer(self._models_dict(api_version)), Deserializer(self._models_dict(api_version)))

    @property
    def variables(self):
        """Instance depends on the API version:

           * 2022-08-01-preview: :class:`VariablesOperations<azure.mgmt.resource.policy.v2022_08_01_preview.operations.VariablesOperations>`
        """
        api_version = self._get_api_version('variables')
        if api_version == '2022-08-01-preview':
            from .v2022_08_01_preview.operations import VariablesOperations as OperationClass
        else:
            raise ValueError("API version {} does not have operation group 'variables'".format(api_version))
        self._config.api_version = api_version
        return OperationClass(self._client, self._config, Serializer(self._models_dict(api_version)), Deserializer(self._models_dict(api_version)))

    def close(self):
        self._client.close()
    def __enter__(self):
        self._client.__enter__()
        return self
    def __exit__(self, *exc_details):
        self._client.__exit__(*exc_details)
