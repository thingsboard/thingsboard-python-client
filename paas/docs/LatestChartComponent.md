
# LatestChartComponent

`tb_paas_client.models.LatestChartComponent`

**Extends:** **ReportComponent**

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **data_sources** | [**List[DataSource]**](DataSource.md) |  | [optional] |
| **margins** | [**Insets**](Insets.md) |  | [optional] |
| **paddings** | [**Insets**](Insets.md) |  | [optional] |
| **background** | **str** |  | [optional] |
| **border_width** | **int** |  | [optional] |
| **border_radius** | **int** |  | [optional] |
| **border_color** | **str** |  | [optional] |
| **width_type** | [**ImageWidthType**](ImageWidthType.md) |  | [optional] |
| **custom_width** | **int** |  | [optional] |
| **alignment** | [**ImageAlignment**](ImageAlignment.md) |  | [optional] |
| **height** | **int** |  | [optional] |
| **latest_chart_settings** | [**ReportLatestChartSettings**](ReportLatestChartSettings.md) |  | [optional] |



## Referenced Types

> **EntityId types** (`AdminSettingsId`, `AiModelId`, `AlarmId`, `ApiKeyId`, `ApiUsageStateId`, `AssetId`, `AssetProfileId`, `BillingCustomerId`, `BlobEntityId`, `CalculatedFieldId`, `ConverterId`, `CouponId`, `CustomerId`, `DashboardId`, `DeviceId`, `DeviceProfileId`, `DomainId`, `EdgeId`, `EntityGroupId`, `EntityViewId`, `GroupPermissionId`, `IntegrationId`, `JobId`, `MobileAppBundleId`, `MobileAppId`, `NotificationId`, `NotificationRequestId`, `NotificationRuleId`, `NotificationTargetId`, `NotificationTemplateId`, `OAuth2ClientId`, `OtaPackageId`, `ProductId`, `QueueId`, `QueueStatsId`, `ReportId`, `ReportTemplateId`, `RoleId`, `RpcId`, `RuleChainId`, `RuleNodeId`, `SchedulerEventId`, `SecretId`, `SubscriptionAddonId`, `SubscriptionId`, `SubscriptionPlanId`, `TbResourceId`, `TenantId`, `TenantProfileId`, `UserId`, `WidgetTypeId`, `WidgetsBundleId`, etc.): `{entity_type: EntityType, id: UUID}` — all EntityId subtypes share this structure.

#### ReportComponent
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| sub_type | ReportComponentSubType |  |  |
| type | ReportComponentType |  |  |

#### DataSource
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| type | DataSourceType |  | [optional] |
| device_id | str |  | [optional] |
| entity_alias_id | str |  | [optional] |
| filter_id | str |  | [optional] |
| data_keys | List[DataKey] |  | [optional] |
| latest_data_keys | List[DataKey] |  | [optional] |
| alarm_filter_config | AlarmFilterConfig |  | [optional] |

#### Insets
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| left | int |  | [optional] |
| right | int |  | [optional] |
| top | int |  | [optional] |
| bottom | int |  | [optional] |

#### ImageWidthType (enum)
`FITWIDTH` | `ORIGINAL` | `CUSTOM`

#### ImageAlignment (enum)
`LEFT` | `CENTER` | `RIGHT`

#### ReportLatestChartSettings
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| show_title | bool |  | [optional] |
| title | str |  | [optional] |
| title_font | Font |  | [optional] |
| title_color | str |  | [optional] |
| title_alignment | TextAlignment |  | [optional] |
| units | str |  | [optional] |
| decimals | int |  | [optional] |
| auto_scale | bool |  | [optional] |
| sort_series | bool |  | [optional] |
| show_total | bool |  | [optional] |
| show_legend | bool |  | [optional] |
| legend_position | LegendPosition |  | [optional] |
| legend_label_font | Font |  | [optional] |
| legend_label_color | str |  | [optional] |
| legend_value_font | Font |  | [optional] |
| legend_value_color | str |  | [optional] |
| legend_show_total | bool |  | [optional] |

#### ReportComponentSubType (enum)
`DOUGHNUTCHART` | `HORIZONTALDOUGHNUTCHART` | `POINTCHART` | `BARCHART` | `PIECHART` | `LINECHART` | `LATESTBARCHART` | `RANGECHART` | `BARCHARTWITHLABELS` | `STATECHART` | … (11 values total)

#### ReportComponentType (enum)
`HEADING` | `RICH_TEXT` | `ENTITY_TABLE` | `TIME_SERIES_TABLE` | `ALARM_TABLE` | `TIME_SERIES_CHART` | `LATEST_CHART` | `DASHBOARD` | `IMAGE` | `SUB_REPORT` | … (14 values total)

#### DataSourceType (enum)
`DEVICE` | `ENTITY` | `ENTITYCOUNT` | `ALARMCOUNT`

#### DataKey
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| name | str |  | [optional] |
| type | str |  | [optional] |
| label | str |  | [optional] |
| color | str |  | [optional] |
| decimals | int |  | [optional] |
| units | str |  | [optional] |
| aggregation_type | Aggregation |  | [optional] |
| timewindow | TimeWindowConfiguration |  | [optional] |
| use_post_processing | bool |  | [optional] |
| post_func_body | str |  | [optional] |
| settings | DataKeySettings |  | [optional] |

#### AlarmFilterConfig
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| type_list | List[str] |  | [optional] |
| status_list | List[AlarmSearchStatus] |  | [optional] |
| severity_list | List[AlarmSeverity] |  | [optional] |
| assignee_id | UserId |  | [optional] |
| search_propagated_alarms | bool |  | [optional] |

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

#### Aggregation (enum)
`MIN` | `MAX` | `AVG` | `SUM` | `COUNT` | `NONE`

#### TimeWindowConfiguration
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| history | History |  | [optional] |
| aggregation | AggregationConfiguration |  | [optional] |
| timezone | str |  | [optional] |

#### DataKeySettings
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| type | DataKeySettingsType | Data key settings type |  |

#### ColumnSettings  *(type=`COLUMN`)*
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| column_width | str |  | [optional] |
| header | CellSettings |  | [optional] |
| cell | CellSettings |  | [optional] |
| type | DataKeySettingsType | Data key settings type |  |

#### DefaultDataKeySettings  *(extends DataKeySettings, type=`DEFAULT`)*
*See DataKeySettings for properties.*

#### TimeSeriesChartKeySettings  *(extends DataKeySettings, type=`TIME_SERIES_CHART`)*
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| y_axis_id | str |  | [optional] |
| show_in_legend | bool |  | [optional] |
| series_type | TimeSeriesChartSeriesType |  | [optional] |
| line_settings | LineSeriesSettings |  | [optional] |
| bar_settings | BarSeriesSettings |  | [optional] |
| comparison_settings | DataKeyComparisonSettings |  | [optional] |
| yaxis_id | str |  | [optional] |

#### AlarmSearchStatus (enum)
`ANY` | `ACTIVE` | `CLEARED` | `ACK` | `UNACK`

#### AlarmSeverity (enum)
`CRITICAL` | `MAJOR` | `MINOR` | `WARNING` | `INDETERMINATE`

#### FontWeight (enum)
`NORMAL` | `BOLD` | `ENUM_500`

#### FontStyle (enum)
`NORMAL` | `ITALIC`

#### History
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| history_type | int |  | [optional] |
| interval | Interval |  | [optional] |
| timewindow_ms | int |  | [optional] |
| fixed_timewindow | FixedTimeWindow |  | [optional] |
| quick_interval | QuickTimeInterval |  | [optional] |

#### AggregationConfiguration
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| type | Aggregation |  | [optional] |
| limit | int |  | [optional] |

#### DataKeySettingsType (enum)
`COLUMN` | `TIME_SERIES_CHART` | `DEFAULT`

#### Interval
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| interval | int |  | [optional] |
| interval_type | IntervalType |  | [optional] |

#### FixedTimeWindow
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| start_time_ms | int |  | [optional] |
| end_time_ms | int |  | [optional] |

#### QuickTimeInterval (enum)
`YESTERDAY` | `DAY_BEFORE_YESTERDAY` | `THIS_DAY_LAST_WEEK` | `PREVIOUS_WEEK` | `PREVIOUS_WEEK_ISO` | `PREVIOUS_MONTH` | `PREVIOUS_QUARTER` | `PREVIOUS_HALF_YEAR` | `PREVIOUS_YEAR` | `CURRENT_HOUR` | … (24 values total)

#### CellSettings
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| font | Font |  | [optional] |
| color | str |  | [optional] |
| background_color | str |  | [optional] |
| text_alignment | TextAlignment |  | [optional] |
| vertical_alignment | VerticalAlignment |  | [optional] |

#### TimeSeriesChartSeriesType (enum)
`LINE` | `BAR`

#### LineSeriesSettings
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| show_line | bool |  | [optional] |
| step | bool |  | [optional] |
| step_type | LineSeriesStepType |  | [optional] |
| smooth | bool |  | [optional] |
| line_type | ChartLineType |  | [optional] |
| line_width | float |  | [optional] |
| show_points | bool |  | [optional] |
| show_point_label | bool |  | [optional] |
| point_label_position | ChartLabelPosition |  | [optional] |
| point_label_font | Font |  | [optional] |
| point_label_color | str |  | [optional] |
| enable_point_label_background | bool |  | [optional] |
| point_label_background | str |  | [optional] |
| point_shape | ChartShape |  | [optional] |
| point_size | float |  | [optional] |
| fill_area_settings | ChartFillSettings |  | [optional] |

#### BarSeriesSettings
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| show_border | bool |  | [optional] |
| border_width | float |  | [optional] |
| border_radius | float |  | [optional] |
| bar_width | float |  | [optional] |
| show_label | bool |  | [optional] |
| label_position | ChartLabelPosition |  | [optional] |
| label_font | Font |  | [optional] |
| label_color | str |  | [optional] |
| enable_label_background | bool |  | [optional] |
| label_background | str |  | [optional] |
| background_settings | ChartFillSettings |  | [optional] |

#### DataKeyComparisonSettings
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| show_values_for_comparison | bool |  | [optional] |
| comparison_values_label | str |  | [optional] |
| color | str |  | [optional] |

#### EntityType (enum)
`TENANT` | `CUSTOMER` | `USER` | `DASHBOARD` | `ASSET` | `DEVICE` | `ALARM` | `ENTITY_GROUP` | `CONVERTER` | `INTEGRATION` | … (52 values total)

#### IntervalType (enum)
`MILLISECONDS` | `WEEK` | `WEEK_ISO` | `MONTH` | `QUARTER`

#### VerticalAlignment (enum)
`BOTTOM` | `TOP` | `MIDDLE`

#### LineSeriesStepType (enum)
`START` | `MIDDLE` | `END`

#### ChartLineType (enum)
`SOLID` | `DASHED` | `DOTTED`

#### ChartLabelPosition (enum)
`TOP` | `BOTTOM`

#### ChartShape (enum)
`EMPTYCIRCLE` | `CIRCLE` | `RECT` | `ROUNDRECT` | `TRIANGLE` | `DIAMOND` | `PIN` | `ARROW` | `NONE`

#### ChartFillSettings
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| type | ChartFillType |  | [optional] |
| opacity | float |  | [optional] |
| gradient | ChartFillSettingsGradient |  | [optional] |

#### ChartFillType (enum)
`NONE` | `OPACITY` | `GRADIENT`

#### ChartFillSettingsGradient
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| start | float |  | [optional] |
| end | float |  | [optional] |

---

### Conventions

- **Package:** `tb_paas_client.models`
- **Attribute access:** `obj.data_sources`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `LatestChartComponent.model_validate(data)` or `LatestChartComponent.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

