# EntityGroupControllerApi

`ThingsboardClient` methods:

```python
None client.add_entities_to_entity_group(entity_group_id: str, request_body: List[str])  # Add entities to the group (addEntitiesToEntityGroup)
EntityGroup client.assign_entity_group_to_edge(edge_id: str, group_type: str, entity_group_id: str)  # Assign entity group to edge (assignEntityGroupToEdge)
None client.delete_entity_group(entity_group_id: str)  # Delete Entity Group (deleteEntityGroup)
List[EntityGroupInfo] client.get_all_edge_entity_groups(edge_id: str, group_type: str)  # Get All Edge Entity Groups by entity type (getAllEdgeEntityGroups)
List[EntityGroupInfo] client.get_all_entity_groups_by_owner_and_type(owner_type: str, owner_id: str, group_type: str)  # Get Entity Groups by owner and entity type (getAllEntityGroupsByOwnerAndType)
List[EntityGroupInfo] client.get_all_entity_groups_by_type(group_type: str, include_shared: Optional[bool] = None)  # Get Entity Groups by entity type (getAllEntityGroupsByType)
List[EntityGroupInfo] client.get_all_shared_entity_groups(group_type: str)  # Get Shared Entity Groups by entity type (getAllSharedEntityGroups)
PageDataEntityGroupInfo client.get_edge_entity_groups(edge_id: str, group_type: str, page_size: str, page: str, text_search: Optional[str] = None, sort_property: Optional[str] = None, sort_order: Optional[str] = None)  # Get Edge Entity Groups by entity type (getEdgeEntityGroups)
PageDataShortEntityView client.get_entities(entity_group_id: str, page_size: str, page: str, text_search: Optional[str] = None, sort_property: Optional[str] = None, sort_order: Optional[str] = None)  # Get Group Entities (getEntities)
EntityGroupInfo client.get_entity_group_all_by_owner_and_type(owner_type: str, owner_id: str, group_type: str)  # Get special group All by owner and entity type (getEntityGroupsByOwnerAndType)
EntityGroupInfo client.get_entity_group_by_id(entity_group_id: str)  # Get Entity Group Info (getEntityGroupById)
EntityGroupInfo client.get_entity_group_by_owner_and_name_and_type(owner_type: str, owner_id: str, group_type: str, group_name: str)  # Get Entity Group by owner, type and name (getEntityGroupByOwnerAndNameAndType)
EntityInfo client.get_entity_group_entity_info_by_id(entity_group_id: str)  # Get Entity Group Entity Info (getEntityGroupEntityInfoById)
List[EntityInfo] client.get_entity_group_entity_infos_by_ids(entity_group_ids: List[str])  # Get Entity Group Entity Infos by Ids (getEntityGroupEntityInfosByIds)
PageDataEntityInfo client.get_entity_group_entity_infos_by_owner_and_type_and_page_link(owner_type: str, owner_id: str, group_type: str, page_size: str, page: str, text_search: Optional[str] = None, sort_property: Optional[str] = None, sort_order: Optional[str] = None)  # Get Entity Group Entity Infos by owner and entity type and page link (getEntityGroupEntityInfosByOwnerAndTypeAndPageLink)
PageDataEntityInfo client.get_entity_group_entity_infos_by_type_and_page_link(group_type: str, page_size: str, page: str, include_shared: Optional[bool] = None, text_search: Optional[str] = None, sort_property: Optional[str] = None, sort_order: Optional[str] = None)  # Get Entity Group Entity Infos by entity type and page link (getEntityGroupEntityInfosByTypeAndPageLink)
PageDataEntityInfo client.get_entity_group_entity_infos_hierarchy_by_owner_and_type_and_page_link(owner_type: str, owner_id: str, group_type: str, page_size: str, page: str, text_search: Optional[str] = None, sort_property: Optional[str] = None, sort_order: Optional[str] = None)  # Get Entity Group Entity Infos for all owners starting from specified than ending with owner of current user (getEntityGroupEntityInfosHierarchyByOwnerAndTypeAndPageLink)
List[EntityGroupInfo] client.get_entity_groups_by_ids(entity_group_ids: List[str])  # Get Entity Groups by Ids (getEntityGroupsByIds)
PageDataEntityGroupInfo client.get_entity_groups_by_owner_and_type_and_page_link(owner_type: str, owner_id: str, group_type: str, page_size: str, page: str, text_search: Optional[str] = None, sort_property: Optional[str] = None, sort_order: Optional[str] = None)  # Get Entity Groups by owner and entity type and page link (getEntityGroupsByOwnerAndTypeAndPageLink)
PageDataEntityGroupInfo client.get_entity_groups_by_type_and_page_link(group_type: str, page_size: str, page: str, include_shared: Optional[bool] = None, text_search: Optional[str] = None, sort_property: Optional[str] = None, sort_order: Optional[str] = None)  # Get Entity Groups by entity type and page link (getEntityGroupsByTypeAndPageLink)
List[EntityGroupId] client.get_entity_groups_for_entity(entity_type: str, entity_id: str)  # Get Entity Groups by Entity Id (getEntityGroupsForEntity)
PageDataEntityGroupInfo client.get_entity_groups_hierarchy_by_owner_and_type_and_page_link(owner_type: str, owner_id: str, group_type: str, page_size: str, page: str, text_search: Optional[str] = None, sort_property: Optional[str] = None, sort_order: Optional[str] = None)  # Get Entity Groups for all owners starting from specified than ending with owner of current user (getEntityGroupsHierarchyByOwnerAndTypeAndPageLink)
ShortEntityView client.get_group_entity(entity_group_id: str, entity_id: str)  # Get Group Entity (getGroupEntity)
EntityInfo client.get_owner_info(owner_type: str, owner_id: str)  # Get Owner Info (getOwnerInfo)
PageDataEntityInfo client.get_owner_infos(page_size: str, page: str, text_search: Optional[str] = None, sort_property: Optional[str] = None, sort_order: Optional[str] = None)  # Get Owner Infos (getOwnerInfos)
PageDataContactBasedObject client.get_owners(page_size: str, page: str, text_search: Optional[str] = None, sort_property: Optional[str] = None, sort_order: Optional[str] = None)  # Get Owners (getOwners)
PageDataEntityInfo client.get_shared_entity_group_entity_infos_by_type_and_page_link(group_type: str, page_size: str, page: str, text_search: Optional[str] = None, sort_property: Optional[str] = None, sort_order: Optional[str] = None)  # Get Shared Entity Group Entity Infos by entity type and page link (getSharedEntityGroupEntityInfosByTypeAndPageLink)
PageDataEntityGroupInfo client.get_shared_entity_groups_by_type_and_page_link(group_type: str, page_size: str, page: str, text_search: Optional[str] = None, sort_property: Optional[str] = None, sort_order: Optional[str] = None)  # Get Shared Entity Groups by entity type and page link (getSharedEntityGroupsByTypeAndPageLink)
None client.make_entity_group_private(entity_group_id: str)  # Make Entity Group Private (makeEntityGroupPrivate)
None client.make_entity_group_public(entity_group_id: str)  # Make Entity Group Publicly available (makeEntityGroupPublic)
None client.remove_entities_from_entity_group(entity_group_id: str, request_body: List[str])  # Remove entities from the group (removeEntitiesFromEntityGroup)
EntityGroupInfo client.save_entity_group(entity_group: EntityGroup)  # Create Or Update Entity Group (saveEntityGroup)
None client.share_entity_group(entity_group_id: str, share_group_request: ShareGroupRequest)  # Share the Entity Group (shareEntityGroup)
None client.share_entity_group_to_child_owner_user_group(entity_group_id: str, user_group_id: str, role_id: str)  # Share the Entity Group with User group (shareEntityGroupToChildOwnerUserGroup)
EntityGroup client.unassign_entity_group_from_edge(edge_id: str, group_type: str, entity_group_id: str)  # Unassign entity group from edge (unassignEntityGroupFromEdge)
```


## add_entities_to_entity_group

```python
None client.add_entities_to_entity_group(entity_group_id: str, request_body: List[str])
```

**POST** `/api/entityGroup/{entityGroupId}/addEntities`

Add entities to the group (addEntitiesToEntityGroup)

Add entities to the specified entity group. This operation is idempotent: entities that are already members of the group are silently ignored. Entity group allows you to group multiple entities of the same entity type (Device, Asset, Customer, User, Dashboard, etc). Entity Group always have an owner - particular Tenant or Customer. Each entity may belong to multiple groups simultaneously.  Available for users with 'TENANT_ADMIN' or 'CUSTOMER_USER' authority. Security check is performed to verify that the user has 'ADD_TO_GROUP' permission for specified group.


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **entity_group_id** | **str** | A string value representing the Entity Group Id. For example, '784f394c-42b6-435a-983c-b7beff2784f9' | |
| **request_body** | **List[str]** |  | |

### Return type

None (empty response body)


## assign_entity_group_to_edge

```python
EntityGroup client.assign_entity_group_to_edge(edge_id: str, group_type: str, entity_group_id: str)
```

**POST** `/api/edge/{edgeId}/entityGroup/{entityGroupId}/{groupType}`

Assign entity group to edge (assignEntityGroupToEdge)

Creates assignment of an existing entity group to an instance of The Edge. Assignment works in async way - first, notification event pushed to edge service queue on platform. Second, remote edge service will receive a copy of assignment entity group (Edge will receive this instantly, if it's currently connected, or once it's going to be connected to platform). Third, once entity group will be delivered to edge service, edge will request entities of this group to be send to edge. Once entities will be delivered to edge service, they are going to be available for usage on remote edge instance.  Available for users with 'TENANT_ADMIN' or 'CUSTOMER_USER' authority. Security check is performed to verify that the user has 'WRITE' permission for the entity (entities).


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **edge_id** | **str** | A string value representing the edge id. For example, '784f394c-42b6-435a-983c-b7beff2784f9' | |
| **group_type** | **str** | EntityGroup type | [enum: ASSET, DEVICE, USER, ENTITY_VIEW, DASHBOARD] |
| **entity_group_id** | **str** | A string value representing the Entity Group Id. For example, '784f394c-42b6-435a-983c-b7beff2784f9' | |

### Return type

**EntityGroup**


## delete_entity_group

```python
None client.delete_entity_group(entity_group_id: str)
```

**DELETE** `/api/entityGroup/{entityGroupId}`

Delete Entity Group (deleteEntityGroup)

Deletes the entity group but does not delete the entities in the group, since they are also present in reserved group 'All'. Referencing non-existing Entity Group Id will cause an error.  Available for users with 'TENANT_ADMIN' or 'CUSTOMER_USER' authority. Security check is performed to verify that the user has 'DELETE' permission for specified group.


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **entity_group_id** | **str** | A string value representing the Entity Group Id. For example, '784f394c-42b6-435a-983c-b7beff2784f9' | |

### Return type

None (empty response body)


## get_all_edge_entity_groups

```python
List[EntityGroupInfo] client.get_all_edge_entity_groups(edge_id: str, group_type: str)
```

**GET** `/api/allEntityGroups/edge/{edgeId}/{groupType}`

Get All Edge Entity Groups by entity type (getAllEdgeEntityGroups)

Fetch the list of Entity Group Info objects based on the provided Entity Type and assigned to the provided Edge entity. Entity group allows you to group multiple entities of the same entity type (Device, Asset, Customer, User, Dashboard, etc). Entity Group always have an owner - particular Tenant or Customer. Each entity may belong to multiple groups simultaneously.Entity Group Info extends Entity Group object and adds 'ownerIds' - a list of owner ids.  Available for users with 'TENANT_ADMIN' or 'CUSTOMER_USER' authority. Security check is performed to verify that the user has 'READ' permission for the entity (entities).


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **edge_id** | **str** | A string value representing the edge id. For example, '784f394c-42b6-435a-983c-b7beff2784f9' | |
| **group_type** | **str** | EntityGroup type | [enum: ASSET, DEVICE, USER, ENTITY_VIEW, DASHBOARD] |

### Return type

**List[EntityGroupInfo]**


## get_all_entity_groups_by_owner_and_type

```python
List[EntityGroupInfo] client.get_all_entity_groups_by_owner_and_type(owner_type: str, owner_id: str, group_type: str)
```

**GET** `/api/entityGroups/{ownerType}/{ownerId}/{groupType}/all`

Get Entity Groups by owner and entity type (getAllEntityGroupsByOwnerAndType)

Fetch the list of Entity Group Info objects based on the provided Owner Id and Entity Type. Entity group allows you to group multiple entities of the same entity type (Device, Asset, Customer, User, Dashboard, etc). Entity Group always have an owner - particular Tenant or Customer. Each entity may belong to multiple groups simultaneously.Entity Group Info extends Entity Group object and adds 'ownerIds' - a list of owner ids.  Available for users with 'TENANT_ADMIN' or 'CUSTOMER_USER' authority. Security check is performed to verify that the user has 'READ' permission for specified group.


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **owner_type** | **str** | Tenant or Customer | [enum: TENANT, CUSTOMER] |
| **owner_id** | **str** | A string value representing the Tenant or Customer id | |
| **group_type** | **str** | Entity Group type | [enum: CUSTOMER, ASSET, DEVICE, USER, ENTITY_VIEW, DASHBOARD, EDGE] |

### Return type

**List[EntityGroupInfo]**


## get_all_entity_groups_by_type

```python
List[EntityGroupInfo] client.get_all_entity_groups_by_type(group_type: str, include_shared: Optional[bool] = None)
```

**GET** `/api/entityGroups/{groupType}/all`

Get Entity Groups by entity type (getAllEntityGroupsByType)

Fetch the list of Entity Group Info objects based on the provided Entity Type. Entity group allows you to group multiple entities of the same entity type (Device, Asset, Customer, User, Dashboard, etc). Entity Group always have an owner - particular Tenant or Customer. Each entity may belong to multiple groups simultaneously.Entity Group Info extends Entity Group object and adds 'ownerIds' - a list of owner ids.  Available for users with 'TENANT_ADMIN' or 'CUSTOMER_USER' authority. Security check is performed to verify that the user has 'READ' permission for specified group.


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **group_type** | **str** | Entity Group type | [enum: CUSTOMER, ASSET, DEVICE, USER, ENTITY_VIEW, DASHBOARD, EDGE] |
| **include_shared** | **bool** | Whether to include shared entity groups. | [optional] |

### Return type

**List[EntityGroupInfo]**


## get_all_shared_entity_groups

```python
List[EntityGroupInfo] client.get_all_shared_entity_groups(group_type: str)
```

**GET** `/api/entityGroups/{groupType}/shared/all`

Get Shared Entity Groups by entity type (getAllSharedEntityGroups)

Fetch the list of Shared Entity Group Info objects based on the provided Entity Type. Entity group allows you to group multiple entities of the same entity type (Device, Asset, Customer, User, Dashboard, etc). Entity Group always have an owner - particular Tenant or Customer. Each entity may belong to multiple groups simultaneously.Entity Group Info extends Entity Group object and adds 'ownerIds' - a list of owner ids.  Available for users with 'TENANT_ADMIN' or 'CUSTOMER_USER' authority. Security check is performed to verify that the user has 'READ' permission for specified group.


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **group_type** | **str** | Entity Group type | [enum: CUSTOMER, ASSET, DEVICE, USER, ENTITY_VIEW, DASHBOARD, EDGE] |

### Return type

**List[EntityGroupInfo]**


## get_edge_entity_groups

```python
PageDataEntityGroupInfo client.get_edge_entity_groups(edge_id: str, group_type: str, page_size: str, page: str, text_search: Optional[str] = None, sort_property: Optional[str] = None, sort_order: Optional[str] = None)
```

**GET** `/api/entityGroups/edge/{edgeId}/{groupType}`

Get Edge Entity Groups by entity type (getEdgeEntityGroups)

Returns a page of Entity Group Info objects based on the provided Entity Type and assigned to the provided Edge entity. Entity group allows you to group multiple entities of the same entity type (Device, Asset, Customer, User, Dashboard, etc). Entity Group always have an owner - particular Tenant or Customer. Each entity may belong to multiple groups simultaneously.Entity Group Info extends Entity Group object and adds 'ownerIds' - a list of owner ids.You can specify parameters to filter the results. The result is wrapped with PageData object that allows you to iterate over result set using pagination. See response schema for more details.   Available for users with 'TENANT_ADMIN' or 'CUSTOMER_USER' authority. Security check is performed to verify that the user has 'READ' permission for the entity (entities).


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **edge_id** | **str** | A string value representing the edge id. For example, '784f394c-42b6-435a-983c-b7beff2784f9' | |
| **group_type** | **str** | EntityGroup type | [enum: ASSET, DEVICE, USER, ENTITY_VIEW, DASHBOARD] |
| **page_size** | **str** | Maximum amount of entities in a one page | |
| **page** | **str** | Sequence number of page starting from 0 | |
| **text_search** | **str** | The case insensitive 'startsWith' filter based on the entity group name. | [optional] |
| **sort_property** | **str** | Property of entity to sort by | [optional] |
| **sort_order** | **str** | Sort order. ASC (ASCENDING) or DESC (DESCENDING) | [optional] [enum: ASC, DESC] |

### Return type

**PageDataEntityGroupInfo**


## get_entities

```python
PageDataShortEntityView client.get_entities(entity_group_id: str, page_size: str, page: str, text_search: Optional[str] = None, sort_property: Optional[str] = None, sort_order: Optional[str] = None)
```

**GET** `/api/entityGroup/{entityGroupId}/entities`

Get Group Entities (getEntities)

Returns a page of Short Entity View objects that belongs to specified Entity Group Id. Short Entity View object contains the entity id and number of fields (attributes, telemetry, etc). List of those fields is configurable and defined in the group configuration.You can specify parameters to filter the results. The result is wrapped with PageData object that allows you to iterate over result set using pagination. See response schema for more details.   Available for users with 'TENANT_ADMIN' or 'CUSTOMER_USER' authority. Security check is performed to verify that the user has 'READ' permission for specified group.


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **entity_group_id** | **str** | A string value representing the Entity Group Id. For example, '784f394c-42b6-435a-983c-b7beff2784f9' | |
| **page_size** | **str** | Maximum amount of entities in a one page | |
| **page** | **str** | Sequence number of page starting from 0 | |
| **text_search** | **str** | The case insensitive 'startsWith' filter based on the entity group name. | [optional] |
| **sort_property** | **str** | Property of entity to sort by | [optional] |
| **sort_order** | **str** | Sort order. ASC (ASCENDING) or DESC (DESCENDING) | [optional] [enum: ASC, DESC] |

### Return type

**PageDataShortEntityView**


## get_entity_group_all_by_owner_and_type

```python
EntityGroupInfo client.get_entity_group_all_by_owner_and_type(owner_type: str, owner_id: str, group_type: str)
```

**GET** `/api/entityGroup/all/{ownerType}/{ownerId}/{groupType}`

Get special group All by owner and entity type (getEntityGroupsByOwnerAndType)

Fetch reserved group 'All' based on the provided Owner Id and Entity Type. Entity group allows you to group multiple entities of the same entity type (Device, Asset, Customer, User, Dashboard, etc). Entity Group always have an owner - particular Tenant or Customer. Each entity may belong to multiple groups simultaneously.Entity Group Info extends Entity Group object and adds 'ownerIds' - a list of owner ids.  Available for users with 'TENANT_ADMIN' or 'CUSTOMER_USER' authority. Security check is performed to verify that the user has 'READ' permission for specified group.


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **owner_type** | **str** | Tenant or Customer | [enum: TENANT, CUSTOMER] |
| **owner_id** | **str** | A string value representing the Tenant or Customer id | |
| **group_type** | **str** | Entity Group type | [enum: CUSTOMER, ASSET, DEVICE, USER, ENTITY_VIEW, DASHBOARD, EDGE] |

### Return type

**EntityGroupInfo**


## get_entity_group_by_id

```python
EntityGroupInfo client.get_entity_group_by_id(entity_group_id: str)
```

**GET** `/api/entityGroup/{entityGroupId}`

Get Entity Group Info (getEntityGroupById)

Fetch the Entity Group object based on the provided Entity Group Id. Entity group allows you to group multiple entities of the same entity type (Device, Asset, Customer, User, Dashboard, etc). Entity Group always have an owner - particular Tenant or Customer. Each entity may belong to multiple groups simultaneously.Entity Group Info extends Entity Group object and adds 'ownerIds' - a list of owner ids.  Entity group name is unique in the scope of owner and entity type. For example, you can't create two tenant device groups called 'Water meters'. However, you may create device and asset group with the same name. And also you may create groups with the same name for two different customers of the same tenant.   Available for users with 'TENANT_ADMIN' or 'CUSTOMER_USER' authority. Security check is performed to verify that the user has 'READ' permission for specified group.


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **entity_group_id** | **str** | A string value representing the Entity Group Id. For example, '784f394c-42b6-435a-983c-b7beff2784f9' | |

### Return type

**EntityGroupInfo**


## get_entity_group_by_owner_and_name_and_type

```python
EntityGroupInfo client.get_entity_group_by_owner_and_name_and_type(owner_type: str, owner_id: str, group_type: str, group_name: str)
```

**GET** `/api/entityGroup/{ownerType}/{ownerId}/{groupType}/{groupName}`

Get Entity Group by owner, type and name (getEntityGroupByOwnerAndNameAndType)

Fetch the Entity Group object based on the provided Entity Group Id. Entity group allows you to group multiple entities of the same entity type (Device, Asset, Customer, User, Dashboard, etc). Entity Group always have an owner - particular Tenant or Customer. Each entity may belong to multiple groups simultaneously.Entity Group Info extends Entity Group object and adds 'ownerIds' - a list of owner ids.  Entity group name is unique in the scope of owner and entity type. For example, you can't create two tenant device groups called 'Water meters'. However, you may create device and asset group with the same name. And also you may create groups with the same name for two different customers of the same tenant.   Available for users with 'TENANT_ADMIN' or 'CUSTOMER_USER' authority. Security check is performed to verify that the user has 'READ' permission for specified group.


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **owner_type** | **str** | Tenant or Customer | [enum: TENANT, CUSTOMER] |
| **owner_id** | **str** | A string value representing the Tenant or Customer id | |
| **group_type** | **str** | Entity Group type | [enum: CUSTOMER, ASSET, DEVICE, USER, ENTITY_VIEW, DASHBOARD, EDGE] |
| **group_name** | **str** | Entity Group name | |

### Return type

**EntityGroupInfo**


## get_entity_group_entity_info_by_id

```python
EntityInfo client.get_entity_group_entity_info_by_id(entity_group_id: str)
```

**GET** `/api/entityGroupInfo/{entityGroupId}`

Get Entity Group Entity Info (getEntityGroupEntityInfoById)

Fetch the Entity Group Entity Info object based on the provided Entity Group Id. Entity Info is a lightweight object that contains only id and name of the entity group.   Entity group name is unique in the scope of owner and entity type. For example, you can't create two tenant device groups called 'Water meters'. However, you may create device and asset group with the same name. And also you may create groups with the same name for two different customers of the same tenant.   Available for users with 'TENANT_ADMIN' or 'CUSTOMER_USER' authority. Security check is performed to verify that the user has 'READ' permission for specified group.


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **entity_group_id** | **str** | A string value representing the Entity Group Id. For example, '784f394c-42b6-435a-983c-b7beff2784f9' | |

### Return type

**EntityInfo**


## get_entity_group_entity_infos_by_ids

```python
List[EntityInfo] client.get_entity_group_entity_infos_by_ids(entity_group_ids: List[str])
```

**GET** `/api/entityGroupInfos`

Get Entity Group Entity Infos by Ids (getEntityGroupEntityInfosByIds)

Fetch the list of Entity Group Entity Info objects based on the provided entity group ids list. Entity Info is a lightweight object that contains only id and name of the entity group.   Available for users with 'TENANT_ADMIN' or 'CUSTOMER_USER' authority. Security check is performed to verify that the user has 'READ' permission for specified group.


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **entity_group_ids** | **List[str]** | A list of group ids, separated by comma ',' | |

### Return type

**List[EntityInfo]**


## get_entity_group_entity_infos_by_owner_and_type_and_page_link

```python
PageDataEntityInfo client.get_entity_group_entity_infos_by_owner_and_type_and_page_link(owner_type: str, owner_id: str, group_type: str, page_size: str, page: str, text_search: Optional[str] = None, sort_property: Optional[str] = None, sort_order: Optional[str] = None)
```

**GET** `/api/entityGroupInfos/{ownerType}/{ownerId}/{groupType}`

Get Entity Group Entity Infos by owner and entity type and page link (getEntityGroupEntityInfosByOwnerAndTypeAndPageLink)

Returns a page of Entity Group Entity Info objects based on the provided Owner Id and Entity Type and Page Link. Entity Info is a lightweight object that contains only id and name of the entity group. You can specify parameters to filter the results. The result is wrapped with PageData object that allows you to iterate over result set using pagination. See response schema for more details.   Available for users with 'TENANT_ADMIN' or 'CUSTOMER_USER' authority. Security check is performed to verify that the user has 'READ' permission for specified group.


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **owner_type** | **str** | Tenant or Customer | [enum: TENANT, CUSTOMER] |
| **owner_id** | **str** | A string value representing the Tenant or Customer id | |
| **group_type** | **str** | Entity Group type | [enum: CUSTOMER, ASSET, DEVICE, USER, ENTITY_VIEW, DASHBOARD, EDGE] |
| **page_size** | **str** | Maximum amount of entities in a one page | |
| **page** | **str** | Sequence number of page starting from 0 | |
| **text_search** | **str** | The case insensitive 'startsWith' filter based on the entity group name. | [optional] |
| **sort_property** | **str** | Property of entity to sort by | [optional] |
| **sort_order** | **str** | Sort order. ASC (ASCENDING) or DESC (DESCENDING) | [optional] [enum: ASC, DESC] |

### Return type

**PageDataEntityInfo**


## get_entity_group_entity_infos_by_type_and_page_link

```python
PageDataEntityInfo client.get_entity_group_entity_infos_by_type_and_page_link(group_type: str, page_size: str, page: str, include_shared: Optional[bool] = None, text_search: Optional[str] = None, sort_property: Optional[str] = None, sort_order: Optional[str] = None)
```

**GET** `/api/entityGroupInfos/{groupType}`

Get Entity Group Entity Infos by entity type and page link (getEntityGroupEntityInfosByTypeAndPageLink)

Returns a page of Entity Group Entity Info objects based on the provided Entity Type and Page Link. Entity Info is a lightweight object that contains only id and name of the entity group. You can specify parameters to filter the results. The result is wrapped with PageData object that allows you to iterate over result set using pagination. See response schema for more details.   Available for users with 'TENANT_ADMIN' or 'CUSTOMER_USER' authority. Security check is performed to verify that the user has 'READ' permission for specified group.


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **group_type** | **str** | Entity Group type | [enum: CUSTOMER, ASSET, DEVICE, USER, ENTITY_VIEW, DASHBOARD, EDGE] |
| **page_size** | **str** | Maximum amount of entities in a one page | |
| **page** | **str** | Sequence number of page starting from 0 | |
| **include_shared** | **bool** | Whether to include shared entity groups. | [optional] |
| **text_search** | **str** | The case insensitive 'startsWith' filter based on the entity group name. | [optional] |
| **sort_property** | **str** | Property of entity to sort by | [optional] |
| **sort_order** | **str** | Sort order. ASC (ASCENDING) or DESC (DESCENDING) | [optional] [enum: ASC, DESC] |

### Return type

**PageDataEntityInfo**


## get_entity_group_entity_infos_hierarchy_by_owner_and_type_and_page_link

```python
PageDataEntityInfo client.get_entity_group_entity_infos_hierarchy_by_owner_and_type_and_page_link(owner_type: str, owner_id: str, group_type: str, page_size: str, page: str, text_search: Optional[str] = None, sort_property: Optional[str] = None, sort_order: Optional[str] = None)
```

**GET** `/api/entityGroupInfosHierarchy/{ownerType}/{ownerId}/{groupType}`

Get Entity Group Entity Infos for all owners starting from specified than ending with owner of current user (getEntityGroupEntityInfosHierarchyByOwnerAndTypeAndPageLink)

Returns a page of Entity Group Entity Info objects based on the provided Owner Id and Entity Type and Page Link. Entity Info is a lightweight object that contains only id and name of the entity group. You can specify parameters to filter the results. The result is wrapped with PageData object that allows you to iterate over result set using pagination. See response schema for more details.   Available for users with 'TENANT_ADMIN' or 'CUSTOMER_USER' authority. Security check is performed to verify that the user has 'READ' permission for specified group.


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **owner_type** | **str** | Tenant or Customer | [enum: TENANT, CUSTOMER] |
| **owner_id** | **str** | A string value representing the Tenant or Customer id | |
| **group_type** | **str** | Entity Group type | [enum: CUSTOMER, ASSET, DEVICE, USER, ENTITY_VIEW, DASHBOARD, EDGE] |
| **page_size** | **str** | Maximum amount of entities in a one page | |
| **page** | **str** | Sequence number of page starting from 0 | |
| **text_search** | **str** | The case insensitive 'startsWith' filter based on the entity group name. | [optional] |
| **sort_property** | **str** | Property of entity to sort by | [optional] |
| **sort_order** | **str** | Sort order. ASC (ASCENDING) or DESC (DESCENDING) | [optional] [enum: ASC, DESC] |

### Return type

**PageDataEntityInfo**


## get_entity_groups_by_ids

```python
List[EntityGroupInfo] client.get_entity_groups_by_ids(entity_group_ids: List[str])
```

**GET** `/api/entityGroups/list`

Get Entity Groups by Ids (getEntityGroupsByIds)

Fetch the list of Entity Group Info objects based on the provided entity group ids list. Entity group allows you to group multiple entities of the same entity type (Device, Asset, Customer, User, Dashboard, etc). Entity Group always have an owner - particular Tenant or Customer. Each entity may belong to multiple groups simultaneously.Entity Group Info extends Entity Group object and adds 'ownerIds' - a list of owner ids.  Available for users with 'TENANT_ADMIN' or 'CUSTOMER_USER' authority. Security check is performed to verify that the user has 'READ' permission for specified group.


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **entity_group_ids** | **List[str]** | A list of group ids, separated by comma ',' | |

### Return type

**List[EntityGroupInfo]**


## get_entity_groups_by_owner_and_type_and_page_link

```python
PageDataEntityGroupInfo client.get_entity_groups_by_owner_and_type_and_page_link(owner_type: str, owner_id: str, group_type: str, page_size: str, page: str, text_search: Optional[str] = None, sort_property: Optional[str] = None, sort_order: Optional[str] = None)
```

**GET** `/api/entityGroups/{ownerType}/{ownerId}/{groupType}`

Get Entity Groups by owner and entity type and page link (getEntityGroupsByOwnerAndTypeAndPageLink)

Returns a page of Entity Group objects based on the provided Owner Id and Entity Type and Page Link. Entity group allows you to group multiple entities of the same entity type (Device, Asset, Customer, User, Dashboard, etc). Entity Group always have an owner - particular Tenant or Customer. Each entity may belong to multiple groups simultaneously.You can specify parameters to filter the results. The result is wrapped with PageData object that allows you to iterate over result set using pagination. See response schema for more details.   Available for users with 'TENANT_ADMIN' or 'CUSTOMER_USER' authority. Security check is performed to verify that the user has 'READ' permission for specified group.


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **owner_type** | **str** | Tenant or Customer | [enum: TENANT, CUSTOMER] |
| **owner_id** | **str** | A string value representing the Tenant or Customer id | |
| **group_type** | **str** | Entity Group type | [enum: CUSTOMER, ASSET, DEVICE, USER, ENTITY_VIEW, DASHBOARD, EDGE] |
| **page_size** | **str** | Maximum amount of entities in a one page | |
| **page** | **str** | Sequence number of page starting from 0 | |
| **text_search** | **str** | The case insensitive 'startsWith' filter based on the entity group name. | [optional] |
| **sort_property** | **str** | Property of entity to sort by | [optional] |
| **sort_order** | **str** | Sort order. ASC (ASCENDING) or DESC (DESCENDING) | [optional] [enum: ASC, DESC] |

### Return type

**PageDataEntityGroupInfo**


## get_entity_groups_by_type_and_page_link

```python
PageDataEntityGroupInfo client.get_entity_groups_by_type_and_page_link(group_type: str, page_size: str, page: str, include_shared: Optional[bool] = None, text_search: Optional[str] = None, sort_property: Optional[str] = None, sort_order: Optional[str] = None)
```

**GET** `/api/entityGroups/{groupType}`

Get Entity Groups by entity type and page link (getEntityGroupsByTypeAndPageLink)

Returns a page of Entity Group Info objects based on the provided Entity Type and Page Link. Entity group allows you to group multiple entities of the same entity type (Device, Asset, Customer, User, Dashboard, etc). Entity Group always have an owner - particular Tenant or Customer. Each entity may belong to multiple groups simultaneously.Entity Group Info extends Entity Group object and adds 'ownerIds' - a list of owner ids.You can specify parameters to filter the results. The result is wrapped with PageData object that allows you to iterate over result set using pagination. See response schema for more details.   Available for users with 'TENANT_ADMIN' or 'CUSTOMER_USER' authority. Security check is performed to verify that the user has 'READ' permission for specified group.


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **group_type** | **str** | Entity Group type | [enum: CUSTOMER, ASSET, DEVICE, USER, ENTITY_VIEW, DASHBOARD, EDGE] |
| **page_size** | **str** | Maximum amount of entities in a one page | |
| **page** | **str** | Sequence number of page starting from 0 | |
| **include_shared** | **bool** | Whether to include shared entity groups. | [optional] |
| **text_search** | **str** | The case insensitive 'startsWith' filter based on the entity group name. | [optional] |
| **sort_property** | **str** | Property of entity to sort by | [optional] |
| **sort_order** | **str** | Sort order. ASC (ASCENDING) or DESC (DESCENDING) | [optional] [enum: ASC, DESC] |

### Return type

**PageDataEntityGroupInfo**


## get_entity_groups_for_entity

```python
List[EntityGroupId] client.get_entity_groups_for_entity(entity_type: str, entity_id: str)
```

**GET** `/api/entityGroups/{entityType}/{entityId}`

Get Entity Groups by Entity Id (getEntityGroupsForEntity)

Returns a list of groups that contain the specified Entity Id. For example, all device groups that contain specific device. The list always contain at least one element - special group 'All'.You can specify parameters to filter the results. The result is wrapped with PageData object that allows you to iterate over result set using pagination. See response schema for more details.   Available for users with 'TENANT_ADMIN' or 'CUSTOMER_USER' authority. Security check is performed to verify that the user has 'READ' permission for the entity (entities).


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **entity_type** | **str** | Entity Group type | [enum: CUSTOMER, ASSET, DEVICE, USER, ENTITY_VIEW, DASHBOARD, EDGE] |
| **entity_id** | **str** | A string value representing the entity id. For example, '784f394c-42b6-435a-983c-b7beff2784f9' | |

### Return type

**List[EntityGroupId]**


## get_entity_groups_hierarchy_by_owner_and_type_and_page_link

```python
PageDataEntityGroupInfo client.get_entity_groups_hierarchy_by_owner_and_type_and_page_link(owner_type: str, owner_id: str, group_type: str, page_size: str, page: str, text_search: Optional[str] = None, sort_property: Optional[str] = None, sort_order: Optional[str] = None)
```

**GET** `/api/entityGroupsHierarchy/{ownerType}/{ownerId}/{groupType}`

Get Entity Groups for all owners starting from specified than ending with owner of current user (getEntityGroupsHierarchyByOwnerAndTypeAndPageLink)

Returns a page of Entity Group objects based on the provided Owner Id and Entity Type and Page Link. Entity group allows you to group multiple entities of the same entity type (Device, Asset, Customer, User, Dashboard, etc). Entity Group always have an owner - particular Tenant or Customer. Each entity may belong to multiple groups simultaneously.You can specify parameters to filter the results. The result is wrapped with PageData object that allows you to iterate over result set using pagination. See response schema for more details.   Available for users with 'TENANT_ADMIN' or 'CUSTOMER_USER' authority. Security check is performed to verify that the user has 'READ' permission for specified group.


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **owner_type** | **str** | Tenant or Customer | [enum: TENANT, CUSTOMER] |
| **owner_id** | **str** | A string value representing the Tenant or Customer id | |
| **group_type** | **str** | Entity Group type | [enum: CUSTOMER, ASSET, DEVICE, USER, ENTITY_VIEW, DASHBOARD, EDGE] |
| **page_size** | **str** | Maximum amount of entities in a one page | |
| **page** | **str** | Sequence number of page starting from 0 | |
| **text_search** | **str** | The case insensitive 'startsWith' filter based on the entity group name. | [optional] |
| **sort_property** | **str** | Property of entity to sort by | [optional] |
| **sort_order** | **str** | Sort order. ASC (ASCENDING) or DESC (DESCENDING) | [optional] [enum: ASC, DESC] |

### Return type

**PageDataEntityGroupInfo**


## get_group_entity

```python
ShortEntityView client.get_group_entity(entity_group_id: str, entity_id: str)
```

**GET** `/api/entityGroup/{entityGroupId}/{entityId}`

Get Group Entity (getGroupEntity)

Fetch the Short Entity View object based on the group and entity id. Short Entity View object contains the entity id and number of fields (attributes, telemetry, etc). List of those fields is configurable and defined in the group configuration.  Available for users with 'TENANT_ADMIN' or 'CUSTOMER_USER' authority. Security check is performed to verify that the user has 'READ' permission for specified group.


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **entity_group_id** | **str** | A string value representing the Entity Group Id. For example, '784f394c-42b6-435a-983c-b7beff2784f9' | |
| **entity_id** | **str** | A string value representing the entity id. For example, '784f394c-42b6-435a-983c-b7beff2784f9' | |

### Return type

**ShortEntityView**


## get_owner_info

```python
EntityInfo client.get_owner_info(owner_type: str, owner_id: str)
```

**GET** `/api/ownerInfo/{ownerType}/{ownerId}`

Get Owner Info (getOwnerInfo)

Fetch the owner info (tenant or customer) presented as Entity Info object based on the provided owner Id.   Available for users with 'TENANT_ADMIN' or 'CUSTOMER_USER' authority. Security check is performed to verify that the user has 'READ' permission for specified group.


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **owner_type** | **str** | Tenant or Customer | [enum: TENANT, CUSTOMER] |
| **owner_id** | **str** | A string value representing the Tenant or Customer id | |

### Return type

**EntityInfo**


## get_owner_infos

```python
PageDataEntityInfo client.get_owner_infos(page_size: str, page: str, text_search: Optional[str] = None, sort_property: Optional[str] = None, sort_order: Optional[str] = None)
```

**GET** `/api/ownerInfos`

Get Owner Infos (getOwnerInfos)

Provides a rage view of Customers that the current user has READ access to. If the current user is Tenant administrator, the result set also contains the tenant. The call is designed for the UI auto-complete component to show tenant and all possible Customers that the user may select to change the owner of the particular entity or entity group.  Available for users with 'TENANT_ADMIN' or 'CUSTOMER_USER' authority. Security check is performed to verify that the user has 'READ' permission for the entity (entities).


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **page_size** | **str** | Maximum amount of entities in a one page | |
| **page** | **str** | Sequence number of page starting from 0 | |
| **text_search** | **str** | The case insensitive 'startsWith' filter based on the entity group name. | [optional] |
| **sort_property** | **str** | Property of entity to sort by | [optional] |
| **sort_order** | **str** | Sort order. ASC (ASCENDING) or DESC (DESCENDING) | [optional] [enum: ASC, DESC] |

### Return type

**PageDataEntityInfo**


## get_owners

```python
PageDataContactBasedObject client.get_owners(page_size: str, page: str, text_search: Optional[str] = None, sort_property: Optional[str] = None, sort_order: Optional[str] = None)
```

**GET** `/api/owners`

Get Owners (getOwners)

Provides a rage view of Customers that the current user has READ access to. If the current user is Tenant administrator, the result set also contains the tenant. The call is designed for the UI auto-complete component to show tenant and all possible Customers that the user may select to change the owner of the particular entity or entity group.  Available for users with 'TENANT_ADMIN' or 'CUSTOMER_USER' authority. Security check is performed to verify that the user has 'READ' permission for the entity (entities).


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **page_size** | **str** | Maximum amount of entities in a one page | |
| **page** | **str** | Sequence number of page starting from 0 | |
| **text_search** | **str** | The case insensitive 'startsWith' filter based on the entity group name. | [optional] |
| **sort_property** | **str** | Property of entity to sort by | [optional] |
| **sort_order** | **str** | Sort order. ASC (ASCENDING) or DESC (DESCENDING) | [optional] [enum: ASC, DESC] |

### Return type

**PageDataContactBasedObject**


## get_shared_entity_group_entity_infos_by_type_and_page_link

```python
PageDataEntityInfo client.get_shared_entity_group_entity_infos_by_type_and_page_link(group_type: str, page_size: str, page: str, text_search: Optional[str] = None, sort_property: Optional[str] = None, sort_order: Optional[str] = None)
```

**GET** `/api/entityGroupInfos/{groupType}/shared`

Get Shared Entity Group Entity Infos by entity type and page link (getSharedEntityGroupEntityInfosByTypeAndPageLink)

Returns a page of Shared Entity Group Entity Info objects based on the provided Entity Type and Page Link. Entity Info is a lightweight object that contains only id and name of the entity group. You can specify parameters to filter the results. The result is wrapped with PageData object that allows you to iterate over result set using pagination. See response schema for more details.   Available for users with 'TENANT_ADMIN' or 'CUSTOMER_USER' authority. Security check is performed to verify that the user has 'READ' permission for specified group.


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **group_type** | **str** | Entity Group type | [enum: CUSTOMER, ASSET, DEVICE, USER, ENTITY_VIEW, DASHBOARD, EDGE] |
| **page_size** | **str** | Maximum amount of entities in a one page | |
| **page** | **str** | Sequence number of page starting from 0 | |
| **text_search** | **str** | The case insensitive 'startsWith' filter based on the entity group name. | [optional] |
| **sort_property** | **str** | Property of entity to sort by | [optional] |
| **sort_order** | **str** | Sort order. ASC (ASCENDING) or DESC (DESCENDING) | [optional] [enum: ASC, DESC] |

### Return type

**PageDataEntityInfo**


## get_shared_entity_groups_by_type_and_page_link

```python
PageDataEntityGroupInfo client.get_shared_entity_groups_by_type_and_page_link(group_type: str, page_size: str, page: str, text_search: Optional[str] = None, sort_property: Optional[str] = None, sort_order: Optional[str] = None)
```

**GET** `/api/entityGroups/{groupType}/shared`

Get Shared Entity Groups by entity type and page link (getSharedEntityGroupsByTypeAndPageLink)

Returns a page of Shared Entity Group Info objects based on the provided Entity Type and Page Link. Entity group allows you to group multiple entities of the same entity type (Device, Asset, Customer, User, Dashboard, etc). Entity Group always have an owner - particular Tenant or Customer. Each entity may belong to multiple groups simultaneously.Entity Group Info extends Entity Group object and adds 'ownerIds' - a list of owner ids.You can specify parameters to filter the results. The result is wrapped with PageData object that allows you to iterate over result set using pagination. See response schema for more details.   Available for users with 'TENANT_ADMIN' or 'CUSTOMER_USER' authority. Security check is performed to verify that the user has 'READ' permission for specified group.


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **group_type** | **str** | Entity Group type | [enum: CUSTOMER, ASSET, DEVICE, USER, ENTITY_VIEW, DASHBOARD, EDGE] |
| **page_size** | **str** | Maximum amount of entities in a one page | |
| **page** | **str** | Sequence number of page starting from 0 | |
| **text_search** | **str** | The case insensitive 'startsWith' filter based on the entity group name. | [optional] |
| **sort_property** | **str** | Property of entity to sort by | [optional] |
| **sort_order** | **str** | Sort order. ASC (ASCENDING) or DESC (DESCENDING) | [optional] [enum: ASC, DESC] |

### Return type

**PageDataEntityGroupInfo**


## make_entity_group_private

```python
None client.make_entity_group_private(entity_group_id: str)
```

**POST** `/api/entityGroup/{entityGroupId}/makePrivate`

Make Entity Group Private (makeEntityGroupPrivate)

Make the entity group not available for non authorized users. Every group is private by default. This call is useful to hide the group that was previously made public.  Available for users with 'TENANT_ADMIN' or 'CUSTOMER_USER' authority. Security check is performed to verify that the user has 'WRITE' permission for specified group.


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **entity_group_id** | **str** | A string value representing the Entity Group Id. For example, '784f394c-42b6-435a-983c-b7beff2784f9' | |

### Return type

None (empty response body)


## make_entity_group_public

```python
None client.make_entity_group_public(entity_group_id: str)
```

**POST** `/api/entityGroup/{entityGroupId}/makePublic`

Make Entity Group Publicly available (makeEntityGroupPublic)

Make the entity group available for non authorized users. Useful for public dashboards that will be embedded into the public websites.   Available for users with 'TENANT_ADMIN' or 'CUSTOMER_USER' authority. Security check is performed to verify that the user has 'WRITE' permission for specified group.


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **entity_group_id** | **str** | A string value representing the Entity Group Id. For example, '784f394c-42b6-435a-983c-b7beff2784f9' | |

### Return type

None (empty response body)


## remove_entities_from_entity_group

```python
None client.remove_entities_from_entity_group(entity_group_id: str, request_body: List[str])
```

**POST** `/api/entityGroup/{entityGroupId}/deleteEntities`

Remove entities from the group (removeEntitiesFromEntityGroup)

Removes entities from the specified entity group. Entity group allows you to group multiple entities of the same entity type (Device, Asset, Customer, User, Dashboard, etc). Entity Group always have an owner - particular Tenant or Customer. Each entity may belong to multiple groups simultaneously.  Available for users with 'TENANT_ADMIN' or 'CUSTOMER_USER' authority. Security check is performed to verify that the user has 'REMOVE_FROM_GROUP' permission for specified group.


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **entity_group_id** | **str** | A string value representing the Entity Group Id. For example, '784f394c-42b6-435a-983c-b7beff2784f9' | |
| **request_body** | **List[str]** |  | |

### Return type

None (empty response body)


## save_entity_group

```python
EntityGroupInfo client.save_entity_group(entity_group: EntityGroup)
```

**POST** `/api/entityGroup`

Create Or Update Entity Group (saveEntityGroup)

Create or update the Entity Group. When creating Entity Group, platform generates Entity Group Id as [time-based UUID](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_1_(date-time_and_MAC_address)). The newly created Entity Group Id will be present in the response. Specify existing Entity Group Id to update the group. Referencing non-existing Entity Group Id will cause 'Not Found' error.Remove 'id', 'tenantId' and optionally 'ownerId' from the request body example (below) to create new Entity Group entity. When 'ownerId' is not set (or null), it defaults to the current user's owner (Tenant for tenant admins, Customer for customer users).   Entity group name is unique in the scope of owner and entity type. For example, you can't create two tenant device groups called 'Water meters'. However, you may create device and asset group with the same name. And also you may create groups with the same name for two different customers of the same tenant.   Available for users with 'TENANT_ADMIN' or 'CUSTOMER_USER' authority. Security check is performed to verify that the user has 'WRITE' permission for specified group.


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **entity_group** | **EntityGroup** |  | |

### Return type

**EntityGroupInfo**


## share_entity_group

```python
None client.share_entity_group(entity_group_id: str, share_group_request: ShareGroupRequest)
```

**POST** `/api/entityGroup/{entityGroupId}/share`

Share the Entity Group (shareEntityGroup)

Share the entity group with certain user group based on the provided Share Group Request. The request is quite flexible and processing of the request involves multiple security checks using platform RBAC feature.  Available for users with 'TENANT_ADMIN' or 'CUSTOMER_USER' authority. Security check is performed to verify that the user has 'WRITE' permission for specified group.


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **entity_group_id** | **str** | A string value representing the Entity Group Id. For example, '784f394c-42b6-435a-983c-b7beff2784f9' | |
| **share_group_request** | **ShareGroupRequest** |  | |

### Return type

None (empty response body)


## share_entity_group_to_child_owner_user_group

```python
None client.share_entity_group_to_child_owner_user_group(entity_group_id: str, user_group_id: str, role_id: str)
```

**POST** `/api/entityGroup/{entityGroupId}/{userGroupId}/{roleId}/share`

Share the Entity Group with User group (shareEntityGroupToChildOwnerUserGroup)

Share the entity group with specified user group using specified role.   Available for users with 'TENANT_ADMIN' or 'CUSTOMER_USER' authority. Security check is performed to verify that the user has 'WRITE' permission for specified group.


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **entity_group_id** | **str** | A string value representing the Entity Group Id that you would like to share. For example, '784f394c-42b6-435a-983c-b7beff2784f9' | |
| **user_group_id** | **str** | A string value representing the Entity(User) Group Id that you would like to share with. For example, '784f394c-42b6-435a-983c-b7beff2784f9' | |
| **role_id** | **str** | A string value representing the Role Id that describes set of permissions you would like to share (read, write, etc). For example, '784f394c-42b6-435a-983c-b7beff2784f9' | |

### Return type

None (empty response body)


## unassign_entity_group_from_edge

```python
EntityGroup client.unassign_entity_group_from_edge(edge_id: str, group_type: str, entity_group_id: str)
```

**DELETE** `/api/edge/{edgeId}/entityGroup/{entityGroupId}/{groupType}`

Unassign entity group from edge (unassignEntityGroupFromEdge)

Clears assignment of the entity group to the edge. Unassignment works in async way - first, 'unassign' notification event pushed to edge queue on platform. Second, remote edge service will receive an 'unassign' command to remove entity group (Edge will receive this instantly, if it's currently connected, or once it's going to be connected to platform). Third, once 'unassign' command will be delivered to edge service, it's going to remove entity group and entities inside this group locally.  Available for users with 'TENANT_ADMIN' or 'CUSTOMER_USER' authority. Security check is performed to verify that the user has 'WRITE' permission for the entity (entities).


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **edge_id** | **str** | A string value representing the edge id. For example, '784f394c-42b6-435a-983c-b7beff2784f9' | |
| **group_type** | **str** | EntityGroup type | [enum: ASSET, DEVICE, USER, ENTITY_VIEW, DASHBOARD] |
| **entity_group_id** | **str** | A string value representing the Entity Group Id. For example, '784f394c-42b6-435a-983c-b7beff2784f9' | |

### Return type

**EntityGroup**

