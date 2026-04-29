
# CloudDomainInfo

`tb_paas_client.models.CloudDomainInfo`

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **id** | [**CloudDomainId**](CloudDomainId.md) |  | [optional] |
| **created_time** | **int** | Entity creation timestamp in milliseconds since Unix epoch | [optional] [readonly] |
| **tenant_id** | [**TenantId**](TenantId.md) |  | [optional] |
| **customer_id** | [**CustomerId**](CustomerId.md) |  | [optional] |
| **domain_name** | **str** |  | [optional] |
| **acme_certificate_id** | [**AcmeCertificateId**](AcmeCertificateId.md) |  | [optional] |
| **certificate** | [**CertificateInfo**](CertificateInfo.md) |  | [optional] |



## Referenced Types

> **EntityId types** (`AdminSettingsId`, `AiModelId`, `AlarmId`, `ApiKeyId`, `ApiUsageStateId`, `AssetId`, `AssetProfileId`, `BillingCustomerId`, `BlobEntityId`, `CalculatedFieldId`, `ConverterId`, `CouponId`, `CustomerId`, `DashboardId`, `DeviceId`, `DeviceProfileId`, `DomainId`, `EdgeId`, `EntityGroupId`, `EntityViewId`, `GroupPermissionId`, `IntegrationId`, `JobId`, `MobileAppBundleId`, `MobileAppId`, `NotificationId`, `NotificationRequestId`, `NotificationRuleId`, `NotificationTargetId`, `NotificationTemplateId`, `OAuth2ClientId`, `OtaPackageId`, `ProductId`, `QueueId`, `QueueStatsId`, `ReportId`, `ReportTemplateId`, `RoleId`, `RpcId`, `RuleChainId`, `RuleNodeId`, `SchedulerEventId`, `SecretId`, `SubscriptionAddonId`, `SubscriptionId`, `SubscriptionPlanId`, `TbResourceId`, `TenantId`, `TenantProfileId`, `UserId`, `WidgetTypeId`, `WidgetsBundleId`, etc.): `{entity_type: EntityType, id: UUID}` — all EntityId subtypes share this structure.

#### CloudDomainId
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| id | UUID | string |  |

#### AcmeCertificateId
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| id | UUID | string |  |

#### CertificateInfo
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| status | CertificateStatus |  | [optional] |
| domain_name | str |  | [optional] |
| serial_number | str |  | [optional] |
| not_before | int |  | [optional] |
| not_after | int |  | [optional] |
| requested_at | int |  | [optional] |
| issued_at | int |  | [optional] |
| acme_certificate_id | AcmeCertificateId |  | [optional] |

#### CertificateStatus (enum)
`PENDING_VALIDATION` | `ISSUED` | `INACTIVE` | `EXPIRED` | `VALIDATION_TIMED_OUT` | `REVOKED` | `FAILED` | `UNKNOWN`

#### EntityType (enum)
`TENANT` | `CUSTOMER` | `USER` | `DASHBOARD` | `ASSET` | `DEVICE` | `ALARM` | `ENTITY_GROUP` | `CONVERTER` | `INTEGRATION` | … (52 values total)

---

### Conventions

- **Package:** `tb_paas_client.models`
- **Attribute access:** `obj.id`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `CloudDomainInfo.model_validate(data)` or `CloudDomainInfo.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

