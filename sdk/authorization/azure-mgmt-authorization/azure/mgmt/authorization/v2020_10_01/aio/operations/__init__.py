# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from ._eligible_child_resources_operations import EligibleChildResourcesOperations
from ._role_assignment_schedules_operations import RoleAssignmentSchedulesOperations
from ._role_assignment_schedule_instances_operations import RoleAssignmentScheduleInstancesOperations
from ._role_assignment_schedule_requests_operations import RoleAssignmentScheduleRequestsOperations
from ._role_eligibility_schedules_operations import RoleEligibilitySchedulesOperations
from ._role_eligibility_schedule_instances_operations import RoleEligibilityScheduleInstancesOperations
from ._role_eligibility_schedule_requests_operations import RoleEligibilityScheduleRequestsOperations
from ._role_management_policies_operations import RoleManagementPoliciesOperations
from ._role_management_policy_assignments_operations import RoleManagementPolicyAssignmentsOperations

from ._patch import __all__ as _patch_all
from ._patch import *  # pylint: disable=unused-wildcard-import
from ._patch import patch_sdk as _patch_sdk

__all__ = [
    "EligibleChildResourcesOperations",
    "RoleAssignmentSchedulesOperations",
    "RoleAssignmentScheduleInstancesOperations",
    "RoleAssignmentScheduleRequestsOperations",
    "RoleEligibilitySchedulesOperations",
    "RoleEligibilityScheduleInstancesOperations",
    "RoleEligibilityScheduleRequestsOperations",
    "RoleManagementPoliciesOperations",
    "RoleManagementPolicyAssignmentsOperations",
]
__all__.extend([p for p in _patch_all if p not in __all__])
_patch_sdk()
