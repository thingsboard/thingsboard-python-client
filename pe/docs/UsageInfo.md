
# UsageInfo

`tb_pe_client.models.UsageInfo`

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **devices** | **int** |  | [optional] |
| **max_devices** | **int** |  | [optional] |
| **assets** | **int** |  | [optional] |
| **max_assets** | **int** |  | [optional] |
| **customers** | **int** |  | [optional] |
| **max_customers** | **int** |  | [optional] |
| **users** | **int** |  | [optional] |
| **max_users** | **int** |  | [optional] |
| **dashboards** | **int** |  | [optional] |
| **max_dashboards** | **int** |  | [optional] |
| **edges** | **int** |  | [optional] |
| **max_edges** | **int** |  | [optional] |
| **transport_messages** | **int** |  | [optional] |
| **max_transport_messages** | **int** |  | [optional] |
| **js_executions** | **int** |  | [optional] |
| **tbel_executions** | **int** |  | [optional] |
| **max_js_executions** | **int** |  | [optional] |
| **max_tbel_executions** | **int** |  | [optional] |
| **emails** | **int** |  | [optional] |
| **max_emails** | **int** |  | [optional] |
| **sms** | **int** |  | [optional] |
| **max_sms** | **int** |  | [optional] |
| **sms_enabled** | **bool** |  | [optional] |
| **alarms** | **int** |  | [optional] |
| **max_alarms** | **int** |  | [optional] |
| **reports** | **int** |  | [optional] |
| **max_reports** | **int** |  | [optional] |
| **ai_credits** | **int** |  | [optional] |
| **max_ai_credits** | **int** |  | [optional] |



---

### Conventions

- **Package:** `tb_pe_client.models`
- **Attribute access:** `obj.devices`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `UsageInfo.model_validate(data)` or `UsageInfo.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

