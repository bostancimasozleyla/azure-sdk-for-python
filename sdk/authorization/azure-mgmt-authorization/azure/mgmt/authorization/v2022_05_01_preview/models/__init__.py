# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from ._models_py3 import ApprovalSettings
from ._models_py3 import ApprovalStage
from ._models_py3 import ErrorAdditionalInfo
from ._models_py3 import ErrorDetail
from ._models_py3 import ErrorResponse
from ._models_py3 import Permission
from ._models_py3 import PermissionGetResult
from ._models_py3 import Principal
from ._models_py3 import RoleDefinition
from ._models_py3 import RoleDefinitionFilter
from ._models_py3 import RoleDefinitionListResult
from ._models_py3 import RoleManagementPolicyApprovalRule
from ._models_py3 import RoleManagementPolicyAuthenticationContextRule
from ._models_py3 import RoleManagementPolicyEnablementRule
from ._models_py3 import RoleManagementPolicyExpirationRule
from ._models_py3 import RoleManagementPolicyNotificationRule
from ._models_py3 import RoleManagementPolicyRule
from ._models_py3 import RoleManagementPolicyRuleTarget
from ._models_py3 import UserSet

from ._authorization_management_client_enums import ApprovalMode
from ._authorization_management_client_enums import EnablementRules
from ._authorization_management_client_enums import NotificationDeliveryMechanism
from ._authorization_management_client_enums import NotificationLevel
from ._authorization_management_client_enums import RecipientType
from ._authorization_management_client_enums import RoleManagementPolicyRuleType
from ._authorization_management_client_enums import UserType
from ._patch import __all__ as _patch_all
from ._patch import *  # pylint: disable=unused-wildcard-import
from ._patch import patch_sdk as _patch_sdk

__all__ = [
    "ApprovalSettings",
    "ApprovalStage",
    "ErrorAdditionalInfo",
    "ErrorDetail",
    "ErrorResponse",
    "Permission",
    "PermissionGetResult",
    "Principal",
    "RoleDefinition",
    "RoleDefinitionFilter",
    "RoleDefinitionListResult",
    "RoleManagementPolicyApprovalRule",
    "RoleManagementPolicyAuthenticationContextRule",
    "RoleManagementPolicyEnablementRule",
    "RoleManagementPolicyExpirationRule",
    "RoleManagementPolicyNotificationRule",
    "RoleManagementPolicyRule",
    "RoleManagementPolicyRuleTarget",
    "UserSet",
    "ApprovalMode",
    "EnablementRules",
    "NotificationDeliveryMechanism",
    "NotificationLevel",
    "RecipientType",
    "RoleManagementPolicyRuleType",
    "UserType",
]
__all__.extend([p for p in _patch_all if p not in __all__])
_patch_sdk()
