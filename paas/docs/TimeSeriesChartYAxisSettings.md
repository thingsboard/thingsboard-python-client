
# TimeSeriesChartYAxisSettings

`tb_paas_client.models.TimeSeriesChartYAxisSettings`

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **show** | **bool** |  | [optional] |
| **label** | **str** |  | [optional] |
| **label_font** | [**Font**](Font.md) |  | [optional] |
| **label_color** | **str** |  | [optional] |
| **position** | [**AxisPosition**](AxisPosition.md) |  | [optional] |
| **show_tick_labels** | **bool** |  | [optional] |
| **tick_label_font** | [**Font**](Font.md) |  | [optional] |
| **tick_label_color** | **str** |  | [optional] |
| **show_ticks** | **bool** |  | [optional] |
| **ticks_color** | **str** |  | [optional] |
| **show_line** | **bool** |  | [optional] |
| **line_color** | **str** |  | [optional] |
| **show_split_lines** | **bool** |  | [optional] |
| **split_lines_color** | **str** |  | [optional] |
| **id** | **str** |  | [optional] |
| **order** | **int** |  | [optional] |
| **units** | **str** |  | [optional] |
| **decimals** | **int** |  | [optional] |
| **interval** | **float** |  | [optional] |
| **split_number** | **int** |  | [optional] |
| **min** | [**SimpleValueSourceConfig**](SimpleValueSourceConfig.md) |  | [optional] |
| **max** | [**SimpleValueSourceConfig**](SimpleValueSourceConfig.md) |  | [optional] |



## Referenced Types

#### Font
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| size | float |  | [optional] |
| weight | FontWeight |  | [optional] |
| style | FontStyle |  | [optional] |
| family | str |  | [optional] |

#### AxisPosition (enum)
`LEFT` | `RIGHT` | `TOP` | `BOTTOM`

#### SimpleValueSourceConfig
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| type | ValueSourceType |  | [optional] |
| value | float |  | [optional] |
| latest_key_type | str |  | [optional] |
| latest_key | str |  | [optional] |
| entity_key_type | str |  | [optional] |
| entity_alias | str |  | [optional] |
| entity_key | str |  | [optional] |

#### FontWeight (enum)
`NORMAL` | `BOLD` | `ENUM_500`

#### FontStyle (enum)
`NORMAL` | `ITALIC`

#### ValueSourceType (enum)
`CONSTANT` | `LATESTKEY` | `ENTITY`

---

### Conventions

- **Package:** `tb_paas_client.models`
- **Attribute access:** `obj.show`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `TimeSeriesChartYAxisSettings.model_validate(data)` or `TimeSeriesChartYAxisSettings.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

