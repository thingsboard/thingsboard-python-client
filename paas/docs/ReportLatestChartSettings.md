
# ReportLatestChartSettings

`tb_paas_client.models.ReportLatestChartSettings`

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **show_title** | **bool** |  | [optional] |
| **title** | **str** |  | [optional] |
| **title_font** | [**Font**](Font.md) |  | [optional] |
| **title_color** | **str** |  | [optional] |
| **title_alignment** | [**TextAlignment**](TextAlignment.md) |  | [optional] |
| **units** | **str** |  | [optional] |
| **decimals** | **int** |  | [optional] |
| **auto_scale** | **bool** |  | [optional] |
| **sort_series** | **bool** |  | [optional] |
| **show_total** | **bool** |  | [optional] |
| **show_legend** | **bool** |  | [optional] |
| **legend_position** | [**LegendPosition**](LegendPosition.md) |  | [optional] |
| **legend_label_font** | [**Font**](Font.md) |  | [optional] |
| **legend_label_color** | **str** |  | [optional] |
| **legend_value_font** | [**Font**](Font.md) |  | [optional] |
| **legend_value_color** | **str** |  | [optional] |
| **legend_show_total** | **bool** |  | [optional] |



## Referenced Types

#### Font
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| size | float |  | [optional] |
| weight | FontWeight |  | [optional] |
| style | FontStyle |  | [optional] |
| family | str |  | [optional] |

#### TextAlignment (enum)
`CENTER` | `RIGHT` | `LEFT` | `JUSTIFY`

#### LegendPosition (enum)
`TOP` | `BOTTOM` | `LEFT` | `RIGHT`

#### FontWeight (enum)
`NORMAL` | `BOLD` | `ENUM_500`

#### FontStyle (enum)
`NORMAL` | `ITALIC`

---

### Conventions

- **Package:** `tb_paas_client.models`
- **Attribute access:** `obj.show_title`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `ReportLatestChartSettings.model_validate(data)` or `ReportLatestChartSettings.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

