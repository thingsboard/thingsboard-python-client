
# ThingsboardCredentialsExpiredResponse

`tb_paas_client.models.ThingsboardCredentialsExpiredResponse`

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **error_code** | [**ThingsboardErrorCode**](ThingsboardErrorCode.md) |  | [optional] |
| **message** | **str** | Error message | [optional] [readonly] |
| **reset_token** | **str** | Password reset token | [optional] [readonly] |
| **status** | **int** | HTTP Response Status Code | [optional] [readonly] |
| **subscription_entry** | [**SubscriptionEntry**](SubscriptionEntry.md) |  | [optional] |
| **subscription_error_code** | [**SubscriptionExceptionErrorCode**](SubscriptionExceptionErrorCode.md) |  | [optional] |
| **subscription_value** | **object** |  | [optional] |
| **timestamp** | **int** | Timestamp | [optional] [readonly] |



## Referenced Types

#### ThingsboardErrorCode (enum)
`NUMBER_2` | `NUMBER_10` | `NUMBER_11` | `NUMBER_15` | `NUMBER_20` | `NUMBER_30` | `NUMBER_31` | `NUMBER_32` | `NUMBER_33` | `NUMBER_34` | … (16 values total)

#### SubscriptionEntry (enum)
`NUMBER_1` | `NUMBER_2` | `NUMBER_3` | `NUMBER_4` | `NUMBER_5` | `NUMBER_6` | `NUMBER_7` | `NUMBER_8` | `NUMBER_9` | `NUMBER_10` | … (13 values total)

#### SubscriptionExceptionErrorCode (enum)
`NUMBER_1` | `NUMBER_2` | `NUMBER_3` | `NUMBER_4` | `NUMBER_5` | `NUMBER_6`

---

### Conventions

- **Package:** `tb_paas_client.models`
- **Attribute access:** `obj.error_code`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `ThingsboardCredentialsExpiredResponse.model_validate(data)` or `ThingsboardCredentialsExpiredResponse.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

