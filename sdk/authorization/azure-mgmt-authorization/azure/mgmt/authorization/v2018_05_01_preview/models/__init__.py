# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from ._models_py3 import AccessReviewDecision
from ._models_py3 import AccessReviewDecisionListResult
from ._models_py3 import AccessReviewDecisionProperties
from ._models_py3 import AccessReviewDecisionTarget
from ._models_py3 import AccessReviewDefaultSettings
from ._models_py3 import AccessReviewInstance
from ._models_py3 import AccessReviewInstanceListResult
from ._models_py3 import AccessReviewReviewer
from ._models_py3 import AccessReviewScheduleDefinition
from ._models_py3 import AccessReviewScheduleDefinitionListResult
from ._models_py3 import AccessReviewScheduleDefinitionProperties
from ._models_py3 import AccessReviewScheduleSettings
from ._models_py3 import ErrorDefinition
from ._models_py3 import ErrorDefinitionProperties
from ._models_py3 import Operation
from ._models_py3 import OperationDisplay
from ._models_py3 import OperationListResult
from ._models_py3 import ServicePrincipalDecisionTarget
from ._models_py3 import UserDecisionTarget

from ._authorization_management_client_enums import AccessRecommendationType
from ._authorization_management_client_enums import AccessReviewActorIdentityType
from ._authorization_management_client_enums import AccessReviewApplyResult
from ._authorization_management_client_enums import AccessReviewInstanceStatus
from ._authorization_management_client_enums import AccessReviewRecurrencePatternType
from ._authorization_management_client_enums import AccessReviewRecurrenceRangeType
from ._authorization_management_client_enums import AccessReviewResult
from ._authorization_management_client_enums import AccessReviewReviewerType
from ._authorization_management_client_enums import AccessReviewScheduleDefinitionReviewersType
from ._authorization_management_client_enums import AccessReviewScheduleDefinitionStatus
from ._authorization_management_client_enums import AccessReviewScopePrincipalType
from ._authorization_management_client_enums import DecisionTargetType
from ._authorization_management_client_enums import DefaultDecisionType
from ._patch import __all__ as _patch_all
from ._patch import *  # pylint: disable=unused-wildcard-import
from ._patch import patch_sdk as _patch_sdk

__all__ = [
    "AccessReviewDecision",
    "AccessReviewDecisionListResult",
    "AccessReviewDecisionProperties",
    "AccessReviewDecisionTarget",
    "AccessReviewDefaultSettings",
    "AccessReviewInstance",
    "AccessReviewInstanceListResult",
    "AccessReviewReviewer",
    "AccessReviewScheduleDefinition",
    "AccessReviewScheduleDefinitionListResult",
    "AccessReviewScheduleDefinitionProperties",
    "AccessReviewScheduleSettings",
    "ErrorDefinition",
    "ErrorDefinitionProperties",
    "Operation",
    "OperationDisplay",
    "OperationListResult",
    "ServicePrincipalDecisionTarget",
    "UserDecisionTarget",
    "AccessRecommendationType",
    "AccessReviewActorIdentityType",
    "AccessReviewApplyResult",
    "AccessReviewInstanceStatus",
    "AccessReviewRecurrencePatternType",
    "AccessReviewRecurrenceRangeType",
    "AccessReviewResult",
    "AccessReviewReviewerType",
    "AccessReviewScheduleDefinitionReviewersType",
    "AccessReviewScheduleDefinitionStatus",
    "AccessReviewScopePrincipalType",
    "DecisionTargetType",
    "DefaultDecisionType",
]
__all__.extend([p for p in _patch_all if p not in __all__])
_patch_sdk()
