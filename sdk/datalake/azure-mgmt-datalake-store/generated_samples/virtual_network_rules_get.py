# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from azure.identity import DefaultAzureCredential
from azure.mgmt.datalake.store import DataLakeStoreAccountManagementClient

"""
# PREREQUISITES
    pip install azure-identity
    pip install azure-mgmt-datalake-store
# USAGE
    python virtual_network_rules_get.py

    Before run the sample, please set the values of the client ID, tenant ID and client secret
    of the AAD application as environment variables: AZURE_CLIENT_ID, AZURE_TENANT_ID,
    AZURE_CLIENT_SECRET. For more info about how to get the value, please see:
    https://docs.microsoft.com/azure/active-directory/develop/howto-create-service-principal-portal
"""


def main():
    client = DataLakeStoreAccountManagementClient(
        credential=DefaultAzureCredential(),
        subscription_id="34adfa4f-cedf-4dc0-ba29-b6d1a69ab345",
    )

    response = client.virtual_network_rules.get(
        resource_group_name="contosorg",
        account_name="contosoadla",
        virtual_network_rule_name="test_virtual_network_rules_name",
    )
    print(response)


# x-ms-original-file: specification/datalake-store/resource-manager/Microsoft.DataLakeStore/stable/2016-11-01/examples/VirtualNetworkRules_Get.json
if __name__ == "__main__":
    main()
