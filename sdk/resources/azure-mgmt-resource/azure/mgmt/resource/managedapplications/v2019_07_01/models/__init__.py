# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from ._models_py3 import Application
from ._models_py3 import ApplicationArtifact
from ._models_py3 import ApplicationAuthorization
from ._models_py3 import ApplicationBillingDetailsDefinition
from ._models_py3 import ApplicationClientDetails
from ._models_py3 import ApplicationDefinition
from ._models_py3 import ApplicationDefinitionArtifact
from ._models_py3 import ApplicationDefinitionListResult
from ._models_py3 import ApplicationDeploymentPolicy
from ._models_py3 import ApplicationJitAccessPolicy
from ._models_py3 import ApplicationListResult
from ._models_py3 import ApplicationManagementPolicy
from ._models_py3 import ApplicationNotificationEndpoint
from ._models_py3 import ApplicationNotificationPolicy
from ._models_py3 import ApplicationPackageContact
from ._models_py3 import ApplicationPackageLockingPolicyDefinition
from ._models_py3 import ApplicationPackageSupportUrls
from ._models_py3 import ApplicationPatchable
from ._models_py3 import ApplicationPolicy
from ._models_py3 import ApplicationPropertiesPatchable
from ._models_py3 import ErrorAdditionalInfo
from ._models_py3 import ErrorDetail
from ._models_py3 import ErrorResponse
from ._models_py3 import GenericResource
from ._models_py3 import Identity
from ._models_py3 import JitApproverDefinition
from ._models_py3 import JitAuthorizationPolicies
from ._models_py3 import JitRequestDefinition
from ._models_py3 import JitRequestDefinitionListResult
from ._models_py3 import JitRequestPatchable
from ._models_py3 import JitSchedulingPolicy
from ._models_py3 import Operation
from ._models_py3 import OperationAutoGenerated
from ._models_py3 import OperationDisplay
from ._models_py3 import OperationDisplayAutoGenerated
from ._models_py3 import OperationListResult
from ._models_py3 import Plan
from ._models_py3 import PlanPatchable
from ._models_py3 import Resource
from ._models_py3 import Sku
from ._models_py3 import UserAssignedResourceIdentity

from ._application_client_enums import ActionType
from ._application_client_enums import ApplicationArtifactName
from ._application_client_enums import ApplicationArtifactType
from ._application_client_enums import ApplicationDefinitionArtifactName
from ._application_client_enums import ApplicationLockLevel
from ._application_client_enums import ApplicationManagementMode
from ._application_client_enums import DeploymentMode
from ._application_client_enums import JitApprovalMode
from ._application_client_enums import JitApproverType
from ._application_client_enums import JitRequestState
from ._application_client_enums import JitSchedulingType
from ._application_client_enums import Origin
from ._application_client_enums import ProvisioningState
from ._application_client_enums import ResourceIdentityType
from ._patch import __all__ as _patch_all
from ._patch import *  # pylint: disable=unused-wildcard-import
from ._patch import patch_sdk as _patch_sdk

__all__ = [
    "Application",
    "ApplicationArtifact",
    "ApplicationAuthorization",
    "ApplicationBillingDetailsDefinition",
    "ApplicationClientDetails",
    "ApplicationDefinition",
    "ApplicationDefinitionArtifact",
    "ApplicationDefinitionListResult",
    "ApplicationDeploymentPolicy",
    "ApplicationJitAccessPolicy",
    "ApplicationListResult",
    "ApplicationManagementPolicy",
    "ApplicationNotificationEndpoint",
    "ApplicationNotificationPolicy",
    "ApplicationPackageContact",
    "ApplicationPackageLockingPolicyDefinition",
    "ApplicationPackageSupportUrls",
    "ApplicationPatchable",
    "ApplicationPolicy",
    "ApplicationPropertiesPatchable",
    "ErrorAdditionalInfo",
    "ErrorDetail",
    "ErrorResponse",
    "GenericResource",
    "Identity",
    "JitApproverDefinition",
    "JitAuthorizationPolicies",
    "JitRequestDefinition",
    "JitRequestDefinitionListResult",
    "JitRequestPatchable",
    "JitSchedulingPolicy",
    "Operation",
    "OperationAutoGenerated",
    "OperationDisplay",
    "OperationDisplayAutoGenerated",
    "OperationListResult",
    "Plan",
    "PlanPatchable",
    "Resource",
    "Sku",
    "UserAssignedResourceIdentity",
    "ActionType",
    "ApplicationArtifactName",
    "ApplicationArtifactType",
    "ApplicationDefinitionArtifactName",
    "ApplicationLockLevel",
    "ApplicationManagementMode",
    "DeploymentMode",
    "JitApprovalMode",
    "JitApproverType",
    "JitRequestState",
    "JitSchedulingType",
    "Origin",
    "ProvisioningState",
    "ResourceIdentityType",
]
__all__.extend([p for p in _patch_all if p not in __all__])
_patch_sdk()
