
# PageDataDashboardInfo

`tb_pe_client.models.PageDataDashboardInfo`

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **data** | [**List[DashboardInfo]**](DashboardInfo.md) | Array of the entities | [optional] |
| **total_pages** | **int** | Total number of available pages. Calculated based on the 'pageSize' request parameter and total number of entities that match search criteria | [optional] [readonly] |
| **total_elements** | **int** | Total number of elements in all available pages | [optional] [readonly] |
| **has_next** | **bool** | 'false' value indicates the end of the result set | [optional] [readonly] |



## Referenced Types

> **EntityId types** (`AdminSettingsId`, `AiModelId`, `AlarmId`, `ApiKeyId`, `ApiUsageStateId`, `AssetId`, `AssetProfileId`, `BlobEntityId`, `CalculatedFieldId`, `ConverterId`, `CustomerId`, `DashboardId`, `DeviceId`, `DeviceProfileId`, `DomainId`, `EdgeId`, `EntityGroupId`, `EntityViewId`, `GroupPermissionId`, `IntegrationId`, `JobId`, `MobileAppBundleId`, `MobileAppId`, `NotificationId`, `NotificationRequestId`, `NotificationRuleId`, `NotificationTargetId`, `NotificationTemplateId`, `OAuth2ClientId`, `OtaPackageId`, `QueueId`, `QueueStatsId`, `ReportId`, `ReportTemplateId`, `RoleId`, `RpcId`, `RuleChainId`, `RuleNodeId`, `SchedulerEventId`, `SecretId`, `TbResourceId`, `TenantId`, `TenantProfileId`, `UserId`, `WidgetTypeId`, `WidgetsBundleId`, etc.): `{entity_type: EntityType, id: UUID}` — all EntityId subtypes share this structure.

#### DashboardInfo
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| id | DashboardId | JSON object with the dashboard Id. Specify existing dashboard Id to update the dashboard. Referencing non-existing dashboard id will cause error. Omit this field to create new dashboard. | [optional] |
| created_time | int | Timestamp of the dashboard creation, in milliseconds | [optional] [readonly] |
| tenant_id | TenantId | JSON object with Tenant Id. Tenant Id of the dashboard can't be changed. | [optional] [readonly] |
| customer_id | CustomerId | JSON object with Customer Id. | [optional] |
| owner_id | EntityId | JSON object with Customer or Tenant Id | [optional] [readonly] |
| title | str | Title of the dashboard. | [optional] |
| name | str | Same as title of the dashboard. Read-only field. Update the 'title' to change the 'name' of the dashboard. | [optional] [readonly] |
| image | str | Thumbnail picture for rendering of the dashboards in a grid view on mobile devices. | [optional] [readonly] |
| assigned_customers | List[ShortCustomerInfo] | List of assigned customers with their info. | [optional] |
| mobile_hide | bool | Hide dashboard from mobile devices. Useful if the dashboard is not designed for small screens. | [optional] [readonly] |
| mobile_order | int | Order on mobile devices. Useful to adjust sorting of the dashboards for mobile applications | [optional] [readonly] |
| configuration | object | JSON object with main configuration of the dashboard: layouts, widgets, aliases, etc. The JSON structure of the dashboard configuration is quite complex. The easiest way to learn it is to export existing dashboard to JSON. | [optional] |
| resources | List[ResourceExportData] |  | [optional] |
| version | int |  | [optional] |
| groups | List[EntityInfo] | Groups | [optional] |
| owner_name | str | Owner name | [optional] [readonly] |

#### ShortCustomerInfo
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| customer_id | CustomerId | JSON object with the customer Id. | [optional] |
| title | str | Title of the customer. | [optional] |
| public | bool | Indicates special 'Public' customer used to embed dashboards on public websites. | [optional] |

#### ResourceExportData
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| link | str |  | [optional] |
| title | str |  | [optional] |
| type | ResourceType |  | [optional] |
| sub_type | ResourceSubType |  | [optional] |
| resource_key | str |  | [optional] |
| file_name | str |  | [optional] |
| public_resource_key | str |  | [optional] |
| media_type | str |  | [optional] |
| data | str |  | [optional] |
| is_public | bool |  | [optional] |
| public | bool |  | [optional] |

#### EntityInfo
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| id | EntityId | JSON object with the entity Id. | [optional] |
| name | str | Entity Name | [optional] |

#### EntityType (enum)
`TENANT` | `CUSTOMER` | `USER` | `DASHBOARD` | `ASSET` | `DEVICE` | `ALARM` | `ENTITY_GROUP` | `CONVERTER` | `INTEGRATION` | … (46 values total)

#### ResourceType (enum)
`LWM2_M_MODEL` | `JKS` | `PKCS_12` | `JS_MODULE` | `IMAGE` | `DASHBOARD` | `GENERAL`

#### ResourceSubType (enum)
`IMAGE` | `SCADA_SYMBOL` | `EXTENSION` | `MODULE`

---

### Conventions

- **Package:** `tb_pe_client.models`
- **Attribute access:** `obj.data`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `PageDataDashboardInfo.model_validate(data)` or `PageDataDashboardInfo.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

