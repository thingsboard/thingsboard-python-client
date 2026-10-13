
# ErrorComponent

`tb_pe_client.models.ErrorComponent`

**Extends:** **ReportComponent**

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **error_message** | **str** |  | [optional] |
| **exception** | [**ErrorComponentAllOfException**](ErrorComponentAllOfException.md) |  | [optional] |



## Referenced Types

#### ReportComponent
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| sub_type | ReportComponentSubType |  |  |
| type | ReportComponentType |  |  |

#### ErrorComponentAllOfException
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| cause | ErrorComponentAllOfExceptionCause |  | [optional] |
| stack_trace | List[ErrorComponentAllOfExceptionCauseStackTrace] |  | [optional] |
| message | str |  | [optional] |
| suppressed | List[ErrorComponentAllOfExceptionCause] |  | [optional] |
| localized_message | str |  | [optional] |

#### ReportComponentSubType (enum)
`DOUGHNUTCHART` | `HORIZONTALDOUGHNUTCHART` | `POINTCHART` | `BARCHART` | `PIECHART` | `LINECHART` | `LATESTBARCHART` | `RANGECHART` | `BARCHARTWITHLABELS` | `STATECHART` | … (11 values total)

#### ReportComponentType (enum)
`HEADING` | `RICH_TEXT` | `ENTITY_TABLE` | `TIME_SERIES_TABLE` | `ALARM_TABLE` | `TIME_SERIES_CHART` | `LATEST_CHART` | `DASHBOARD` | `IMAGE` | `SUB_REPORT` | … (14 values total)

#### ErrorComponentAllOfExceptionCause
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| stack_trace | List[ErrorComponentAllOfExceptionCauseStackTrace] |  | [optional] |
| message | str |  | [optional] |
| localized_message | str |  | [optional] |

#### ErrorComponentAllOfExceptionCauseStackTrace
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| class_loader_name | str |  | [optional] |
| module_name | str |  | [optional] |
| module_version | str |  | [optional] |
| method_name | str |  | [optional] |
| file_name | str |  | [optional] |
| line_number | int |  | [optional] |
| class_name | str |  | [optional] |
| native_method | bool |  | [optional] |

---

### Conventions

- **Package:** `tb_pe_client.models`
- **Attribute access:** `obj.error_message`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `ErrorComponent.model_validate(data)` or `ErrorComponent.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

