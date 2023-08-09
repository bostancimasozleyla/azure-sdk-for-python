# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from azure.identity import DefaultAzureCredential
from azure.mgmt.redis import RedisManagementClient

"""
# PREREQUISITES
    pip install azure-identity
    pip install azure-mgmt-redis
# USAGE
    python redis_cache_list_private_link_resources.py

    Before run the sample, please set the values of the client ID, tenant ID and client secret
    of the AAD application as environment variables: AZURE_CLIENT_ID, AZURE_TENANT_ID,
    AZURE_CLIENT_SECRET. For more info about how to get the value, please see:
    https://docs.microsoft.com/azure/active-directory/develop/howto-create-service-principal-portal
"""


def main():
    client = RedisManagementClient(
        credential=DefaultAzureCredential(),
        subscription_id="{subscription-id}",
    )

    response = client.private_link_resources.list_by_redis_cache(
        resource_group_name="rgtest01",
        cache_name="cacheTest01",
    )
    for item in response:
        print(item)


# x-ms-original-file: specification/redis/resource-manager/Microsoft.Cache/stable/2023-04-01/examples/RedisCacheListPrivateLinkResources.json
if __name__ == "__main__":
    main()
