
# ReportTemplateConfig

`tb_paas_client.models.ReportTemplateConfig`

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **name_pattern** | **str** |  | [optional] |
| **time_data_pattern** | **str** |  | [optional] |
| **format** | [**TbReportFormat**](TbReportFormat.md) | Report format | |
| **entity_aliases** | [**List[EntityAlias]**](EntityAlias.md) |  | [optional] |
| **filters** | [**List[Filter]**](Filter.md) |  | [optional] |
| **components** | [**List[ReportComponent]**](ReportComponent.md) |  | [optional] |



## Subtypes

#### CsvReportTemplateConfig  *(format=`CSV`)*
*(no additional properties)*

#### PdfReportTemplateConfig  *(format=`PDF`)*
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| footer | HeaderFooter |  | [optional] |
| header | HeaderFooter |  | [optional] |
| page_background | str |  | [optional] |
| page_margins | Insets |  | [optional] |
| page_orientation | PageOrientation |  | [optional] |
| page_size | PageSize |  | [optional] |

## Referenced Types

> **EntityId types** (`AdminSettingsId`, `AiModelId`, `AlarmId`, `ApiKeyId`, `ApiUsageStateId`, `AssetId`, `AssetProfileId`, `BillingCustomerId`, `BlobEntityId`, `CalculatedFieldId`, `ConverterId`, `CouponId`, `CustomerId`, `DashboardId`, `DeviceId`, `DeviceProfileId`, `DomainId`, `EdgeId`, `EntityGroupId`, `EntityViewId`, `GroupPermissionId`, `IntegrationId`, `JobId`, `MobileAppBundleId`, `MobileAppId`, `NotificationId`, `NotificationRequestId`, `NotificationRuleId`, `NotificationTargetId`, `NotificationTemplateId`, `OAuth2ClientId`, `OtaPackageId`, `ProductId`, `QueueId`, `QueueStatsId`, `ReportId`, `ReportTemplateId`, `RoleId`, `RpcId`, `RuleChainId`, `RuleNodeId`, `SchedulerEventId`, `SecretId`, `SubscriptionAddonId`, `SubscriptionId`, `SubscriptionPlanId`, `TbResourceId`, `TenantId`, `TenantProfileId`, `UserId`, `WidgetTypeId`, `WidgetsBundleId`, etc.): `{entity_type: EntityType, id: UUID}` — all EntityId subtypes share this structure.

#### TbReportFormat (enum)
`PDF` | `CSV`

#### EntityAlias
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| id | str |  | [optional] |
| alias | str |  | [optional] |
| filter | EntityFilter |  | [optional] |

#### Filter
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| id | str |  | [optional] |
| filter | str |  | [optional] |
| key_filters | List[KeyFilter] |  | [optional] |

#### ReportComponent
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| sub_type | ReportComponentSubType |  |  |
| type | ReportComponentType |  |  |

#### AlarmTableComponent  *(extends ReportComponent, type=`ALARM_TABLE`)*
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| margins | Insets |  | [optional] |
| paddings | Insets |  | [optional] |
| background | str |  | [optional] |
| border_width | int |  | [optional] |
| border_radius | int |  | [optional] |
| border_color | str |  | [optional] |
| show_table_heading | bool |  | [optional] |
| table_heading | Heading |  | [optional] |
| table_sort_order | TableSortOrder |  | [optional] |
| alarm_source | DataSource |  | [optional] |
| timewindow | TimeWindowConfiguration |  | [optional] |

#### DashboardComponent  *(extends ReportComponent, type=`DASHBOARD`)*
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| data_sources | List[DataSource] |  | [optional] |
| margins | Insets |  | [optional] |
| paddings | Insets |  | [optional] |
| background | str |  | [optional] |
| border_width | int |  | [optional] |
| border_radius | int |  | [optional] |
| border_color | str |  | [optional] |
| width_type | ImageWidthType |  | [optional] |
| custom_width | int |  | [optional] |
| alignment | ImageAlignment |  | [optional] |
| config | DashboardReportConfig | Dashboard report configuration. |  |

#### DividerComponent  *(extends ReportComponent, type=`DIVIDER`)*
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| margins | Insets |  | [optional] |
| paddings | Insets |  | [optional] |
| background | str |  | [optional] |
| border_width | int |  | [optional] |
| border_radius | int |  | [optional] |
| border_color | str |  | [optional] |
| length | BorderLength |  | [optional] |
| border_type | BorderType |  | [optional] |
| width_px | int |  | [optional] |
| color | str |  | [optional] |

#### EntityTableComponent  *(extends ReportComponent, type=`ENTITY_TABLE`)*
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| data_sources | List[DataSource] |  | [optional] |
| margins | Insets |  | [optional] |
| paddings | Insets |  | [optional] |
| background | str |  | [optional] |
| border_width | int |  | [optional] |
| border_radius | int |  | [optional] |
| border_color | str |  | [optional] |
| show_table_heading | bool |  | [optional] |
| table_heading | Heading |  | [optional] |
| table_sort_order | TableSortOrder |  | [optional] |

#### ErrorComponent  *(extends ReportComponent, type=`ERROR`)*
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| error_message | str |  | [optional] |
| exception | ErrorComponentAllOfException |  | [optional] |

#### HeadingComponent  *(extends ReportComponent, type=`HEADING`)*
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| data_sources | List[DataSource] |  | [optional] |
| margins | Insets |  | [optional] |
| paddings | Insets |  | [optional] |
| background | str |  | [optional] |
| border_width | int |  | [optional] |
| border_radius | int |  | [optional] |
| border_color | str |  | [optional] |
| value | str |  | [optional] |
| font | Font |  | [optional] |
| color | str |  | [optional] |
| text_alignment | TextAlignment |  | [optional] |
| vertical_alignment | VerticalAlignment |  | [optional] |
| height | int |  | [optional] |

#### ImageComponent  *(extends ReportComponent, type=`IMAGE`)*
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| data_sources | List[DataSource] |  | [optional] |
| margins | Insets |  | [optional] |
| paddings | Insets |  | [optional] |
| background | str |  | [optional] |
| border_width | int |  | [optional] |
| border_radius | int |  | [optional] |
| border_color | str |  | [optional] |
| width_type | ImageWidthType |  | [optional] |
| custom_width | int |  | [optional] |
| alignment | ImageAlignment |  | [optional] |
| source_type | ImageSourceType |  | [optional] |
| image_url | str |  | [optional] |

#### LatestChartComponent  *(extends ReportComponent, type=`LATEST_CHART`)*
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| data_sources | List[DataSource] |  | [optional] |
| margins | Insets |  | [optional] |
| paddings | Insets |  | [optional] |
| background | str |  | [optional] |
| border_width | int |  | [optional] |
| border_radius | int |  | [optional] |
| border_color | str |  | [optional] |
| width_type | ImageWidthType |  | [optional] |
| custom_width | int |  | [optional] |
| alignment | ImageAlignment |  | [optional] |
| height | int |  | [optional] |
| latest_chart_settings | ReportLatestChartSettings |  | [optional] |

#### PageBreakComponent  *(extends ReportComponent, type=`PAGE_BREAK`)*
*See ReportComponent for properties.*

#### RichTextComponent  *(extends ReportComponent, type=`RICH_TEXT`)*
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| data_sources | List[DataSource] |  | [optional] |
| margins | Insets |  | [optional] |
| paddings | Insets |  | [optional] |
| background | str |  | [optional] |
| border_width | int |  | [optional] |
| border_radius | int |  | [optional] |
| border_color | str |  | [optional] |
| value | str |  | [optional] |

#### SplitViewComponent  *(extends ReportComponent, type=`SPLIT_VIEW`)*
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| margins | Insets |  | [optional] |
| paddings | Insets |  | [optional] |
| background | str |  | [optional] |
| border_width | int |  | [optional] |
| border_radius | int |  | [optional] |
| border_color | str |  | [optional] |
| left_view | ReportComponent |  | [optional] |
| right_view | ReportComponent |  | [optional] |
| split_position | float |  | [optional] |
| split_gap | int |  | [optional] |
| left_vertical_alignment | VerticalAlignment |  | [optional] |
| right_vertical_alignment | VerticalAlignment |  | [optional] |

#### SubReportComponent  *(extends ReportComponent, type=`SUB_REPORT`)*
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| data_sources | List[DataSource] |  | [optional] |
| template_id | ReportTemplateId |  | [optional] |
| avoid_page_break_inside | bool |  | [optional] |

#### TimeseriesChartComponent  *(extends ReportComponent, type=`TIME_SERIES_CHART`)*
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| data_sources | List[DataSource] |  | [optional] |
| margins | Insets |  | [optional] |
| paddings | Insets |  | [optional] |
| background | str |  | [optional] |
| border_width | int |  | [optional] |
| border_radius | int |  | [optional] |
| border_color | str |  | [optional] |
| width_type | ImageWidthType |  | [optional] |
| custom_width | int |  | [optional] |
| alignment | ImageAlignment |  | [optional] |
| height | int |  | [optional] |
| timewindow | TimeWindowConfiguration |  | [optional] |
| time_series_chart_settings | ReportTimeSeriesChartSettings |  | [optional] |

#### TimeseriesTableComponent  *(extends ReportComponent, type=`TIME_SERIES_TABLE`)*
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| data_sources | List[DataSource] |  | [optional] |
| margins | Insets |  | [optional] |
| paddings | Insets |  | [optional] |
| background | str |  | [optional] |
| border_width | int |  | [optional] |
| border_radius | int |  | [optional] |
| border_color | str |  | [optional] |
| show_table_heading | bool |  | [optional] |
| table_heading | Heading |  | [optional] |
| table_sort_order | TableSortOrder |  | [optional] |
| timewindow | TimeWindowConfiguration |  | [optional] |
| show_timestamp | bool |  | [optional] |
| timestamp_label | str |  | [optional] |
| timestamp_pattern | str |  | [optional] |
| timestamp_column_settings | ColumnSettings |  | [optional] |

#### HeaderFooter
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| enabled | bool |  | [optional] |
| components | List[ReportComponent] |  |  |
| first_page | object |  | [optional] |

#### Insets
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| left | int |  | [optional] |
| right | int |  | [optional] |
| top | int |  | [optional] |
| bottom | int |  | [optional] |

#### PageOrientation (enum)
`PORTRAIT` | `LANDSCAPE`

#### PageSize (enum)
`A4` | `LETTER` | `LEGAL` | `A5` | `A3` | `TABLOID`

#### EntityFilter
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| type | str |  |  |

#### ApiUsageStateFilter  *(extends EntityFilter, type=`apiUsageState`)*
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| customer_id | CustomerId |  | [optional] |

#### AssetSearchQueryFilter  *(extends EntityFilter, type=`assetSearchQuery`)*
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| root_entity | AliasEntityId |  | [optional] |
| relation_type | str |  | [optional] |
| direction | EntitySearchDirection |  | [optional] |
| max_level | int |  | [optional] |
| fetch_last_level_only | bool |  | [optional] |
| root_state_entity | bool |  | [optional] |
| default_state_entity | AliasEntityId |  | [optional] |
| asset_types | List[str] |  | [optional] |

#### AssetTypeFilter  *(extends EntityFilter, type=`assetType`)*
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| asset_types | List[str] |  | [optional] |
| asset_name_filter | str |  | [optional] |
| asset_type | str |  | [optional] |

#### DeviceSearchQueryFilter  *(extends EntityFilter, type=`deviceSearchQuery`)*
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| root_entity | AliasEntityId |  | [optional] |
| relation_type | str |  | [optional] |
| direction | EntitySearchDirection |  | [optional] |
| max_level | int |  | [optional] |
| fetch_last_level_only | bool |  | [optional] |
| root_state_entity | bool |  | [optional] |
| default_state_entity | AliasEntityId |  | [optional] |
| device_types | List[str] |  | [optional] |

#### DeviceTypeFilter  *(extends EntityFilter, type=`deviceType`)*
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| device_types | List[str] |  | [optional] |
| device_name_filter | str |  | [optional] |
| device_type | str |  | [optional] |

#### EdgeSearchQueryFilter  *(extends EntityFilter, type=`edgeSearchQuery`)*
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| root_entity | AliasEntityId |  | [optional] |
| relation_type | str |  | [optional] |
| direction | EntitySearchDirection |  | [optional] |
| max_level | int |  | [optional] |
| fetch_last_level_only | bool |  | [optional] |
| root_state_entity | bool |  | [optional] |
| default_state_entity | AliasEntityId |  | [optional] |
| edge_types | List[str] |  | [optional] |

#### EdgeTypeFilter  *(extends EntityFilter, type=`edgeType`)*
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| edge_types | List[str] |  | [optional] |
| edge_name_filter | str |  | [optional] |
| edge_type | str |  | [optional] |

#### EntitiesByGroupNameFilter  *(extends EntityFilter, type=`entitiesByGroupName`)*
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| group_type | EntityType |  | [optional] |
| owner_id | EntityId |  | [optional] |
| entity_group_name_filter | str |  | [optional] |
| group_state_entity | bool |  | [optional] |
| state_entity_param_name | str |  | [optional] |

#### EntityGroupFilter  *(extends EntityFilter, type=`entityGroup`)*
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| group_type | EntityType |  | [optional] |
| entity_group | str |  | [optional] |
| group_state_entity | bool |  | [optional] |
| default_state_group_type | EntityType |  | [optional] |
| default_state_entity_group | str |  | [optional] |

#### EntityGroupListFilter  *(extends EntityFilter, type=`entityGroupList`)*
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| group_type | EntityType |  | [optional] |
| entity_group_list | List[str] |  | [optional] |

#### EntityGroupNameFilter  *(extends EntityFilter, type=`entityGroupName`)*
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| group_type | EntityType |  | [optional] |
| entity_group_name_filter | str |  | [optional] |

#### EntityListFilter  *(extends EntityFilter, type=`entityList`)*
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| entity_type | EntityType |  | [optional] |
| entity_list | List[str] |  | [optional] |

#### EntityNameFilter  *(extends EntityFilter, type=`entityName`)*
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| entity_type | EntityType |  | [optional] |
| entity_name_filter | str |  | [optional] |

#### EntityTypeFilter  *(extends EntityFilter, type=`entityType`)*
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| entity_type | EntityType |  | [optional] |

#### EntityViewSearchQueryFilter  *(extends EntityFilter, type=`entityViewSearchQuery`)*
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| root_entity | AliasEntityId |  | [optional] |
| relation_type | str |  | [optional] |
| direction | EntitySearchDirection |  | [optional] |
| max_level | int |  | [optional] |
| fetch_last_level_only | bool |  | [optional] |
| root_state_entity | bool |  | [optional] |
| default_state_entity | AliasEntityId |  | [optional] |
| entity_view_types | List[str] |  | [optional] |

#### EntityViewTypeFilter  *(extends EntityFilter, type=`entityViewType`)*
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| entity_view_types | List[str] |  | [optional] |
| entity_view_name_filter | str |  | [optional] |
| entity_view_type | str |  | [optional] |

#### RelationsQueryFilter  *(extends EntityFilter, type=`relationsQuery`)*
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| root_entity | AliasEntityId |  | [optional] |
| multi_root | bool |  | [optional] |
| multi_root_entities_type | EntityType |  | [optional] |
| multi_root_entity_ids | List[str] |  | [optional] |
| direction | EntitySearchDirection |  | [optional] |
| filters | List[RelationEntityTypeFilter] |  | [optional] |
| max_level | int |  | [optional] |
| fetch_last_level_only | bool |  | [optional] |
| negate | bool |  | [optional] |
| root_state_entity | bool |  | [optional] |
| default_state_entity | AliasEntityId |  | [optional] |

#### SchedulerEventFilter  *(extends EntityFilter, type=`schedulerEvent`)*
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| originator | AliasEntityId |  | [optional] |
| event_type | str |  | [optional] |
| originator_state_entity | bool |  | [optional] |
| default_state_entity | AliasEntityId |  | [optional] |

#### SingleEntityFilter  *(extends EntityFilter, type=`singleEntity`)*
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| single_entity | AliasEntityId |  | [optional] |

#### StateEntityFilter  *(extends EntityFilter, type=`stateEntity`)*
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| default_state_entity | AliasEntityId |  | [optional] |

#### StateEntityOwnerFilter  *(extends EntityFilter, type=`stateEntityOwner`)*
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| single_entity | AliasEntityId |  | [optional] |
| default_state_entity | AliasEntityId |  | [optional] |

#### KeyFilter
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| key | EntityKey |  | [optional] |
| value_type | EntityKeyValueType |  | [optional] |
| predicate | KeyFilterPredicate |  | [optional] |

#### ReportComponentSubType (enum)
`DOUGHNUTCHART` | `HORIZONTALDOUGHNUTCHART` | `POINTCHART` | `BARCHART` | `PIECHART` | `LINECHART` | `LATESTBARCHART` | `RANGECHART` | `BARCHARTWITHLABELS` | `STATECHART` | … (11 values total)

#### ReportComponentType (enum)
`HEADING` | `RICH_TEXT` | `ENTITY_TABLE` | `TIME_SERIES_TABLE` | `ALARM_TABLE` | `TIME_SERIES_CHART` | `LATEST_CHART` | `DASHBOARD` | `IMAGE` | `SUB_REPORT` | … (14 values total)

#### EntityKey
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| type | EntityKeyType |  | [optional] |
| key | str |  | [optional] |

#### EntityKeyValueType (enum)
`STRING` | `NUMERIC` | `BOOLEAN` | `DATE_TIME`

#### KeyFilterPredicate
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| type | str |  |  |

#### BooleanFilterPredicate  *(extends KeyFilterPredicate, type=`BOOLEAN`)*
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| operation | BooleanOperation |  | [optional] |
| value | FilterPredicateValueBoolean | The value associated with the filter predicate | [optional] |

#### ComplexFilterPredicate  *(extends KeyFilterPredicate, type=`COMPLEX`)*
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| operation | ComplexOperation |  | [optional] |
| predicates | List[KeyFilterPredicate] |  | [optional] |

#### NumericFilterPredicate  *(extends KeyFilterPredicate, type=`NUMERIC`)*
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| operation | NumericOperation |  | [optional] |
| value | FilterPredicateValueDouble | The value associated with the filter predicate | [optional] |

#### StringFilterPredicate  *(extends KeyFilterPredicate, type=`STRING`)*
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| operation | StringOperation |  | [optional] |
| value | FilterPredicateValueString | The value associated with the filter predicate | [optional] |
| ignore_case | bool |  | [optional] |

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

#### Font
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| size | float |  | [optional] |
| weight | FontWeight |  | [optional] |
| style | FontStyle |  | [optional] |
| family | str |  | [optional] |

#### TextAlignment (enum)
`CENTER` | `RIGHT` | `LEFT` | `JUSTIFY`

#### VerticalAlignment (enum)
`BOTTOM` | `TOP` | `MIDDLE`

#### Heading
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| text | str |  | [optional] |
| font | Font |  | [optional] |
| color | str |  | [optional] |
| text_alignment | TextAlignment |  | [optional] |
| vertical_alignment | VerticalAlignment |  | [optional] |
| height | int |  | [optional] |

#### TableSortOrder
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| column | str |  | [optional] |
| direction | TableSortDirection |  | [optional] |

#### TimeWindowConfiguration
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| history | History |  | [optional] |
| aggregation | AggregationConfiguration |  | [optional] |
| timezone | str |  | [optional] |

#### ImageWidthType (enum)
`FITWIDTH` | `ORIGINAL` | `CUSTOM`

#### ImageAlignment (enum)
`LEFT` | `CENTER` | `RIGHT`

#### ReportTimeSeriesChartSettings
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| show_title | bool |  | [optional] |
| title | str |  | [optional] |
| title_font | Font |  | [optional] |
| title_color | str |  | [optional] |
| title_alignment | TextAlignment |  | [optional] |
| thresholds | List[TimeSeriesChartThreshold] |  | [optional] |
| stack | bool |  | [optional] |
| grid | TimeSeriesChartGridSettings |  | [optional] |
| y_axes | Dict[str, TimeSeriesChartYAxisSettings] |  | [optional] |
| x_axis | TimeSeriesChartXAxisSettings |  | [optional] |
| bar_width_settings | TimeSeriesChartBarWidthSettings |  | [optional] |
| no_aggregation_bar_width_settings | TimeSeriesChartNoAggregationBarWidthSettings |  | [optional] |
| states | List[TimeSeriesChartStateSettings] |  | [optional] |
| comparison_enabled | bool |  | [optional] |
| time_for_comparison | ComparisonDuration |  | [optional] |
| comparison_custom_interval_value | int |  | [optional] |
| comparison_x_axis | TimeSeriesChartXAxisSettings |  | [optional] |
| show_legend | bool |  | [optional] |
| legend_column_title_font | Font |  | [optional] |
| legend_column_title_color | str |  | [optional] |
| legend_label_font | Font |  | [optional] |
| legend_label_color | str |  | [optional] |
| legend_value_font | Font |  | [optional] |
| legend_value_color | str |  | [optional] |
| legend_config | LegendConfig |  | [optional] |
| xaxis | TimeSeriesChartXAxisSettings |  | [optional] |
| yaxes | Dict[str, TimeSeriesChartYAxisSettings] |  | [optional] |

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

#### DashboardReportConfig
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| base_url | str | Base URL of ThingsBoard UI that should be accessible by Web Report Server. |  |
| dashboard_id | str | A string value representing the dashboard id. |  |
| state | str | Target dashboard state for dashboard report generation. | [optional] |
| timezone | str | Timezone in which target dashboard will be presented in dashboard report. |  |
| use_dashboard_timewindow | bool | If set, timewindow configured in the target dashboard will be used during dashboard report generation. | [optional] |
| timewindow | object | Specific dashboard timewindow that will be used during dashboard report generation. | [optional] |
| name_pattern | str | If set, timewindow configured in the target dashboard will be used during dashboard report generation. |  |
| type | str | Dashboard report file type, can be PDF | PNG |
| use_current_user_credentials | bool | If set, credentials of user created this dashboard report configuration will be used to open dashboard UI during dashboard report generation. | [optional] |
| user_id | str | A string value representing the user id. |  |

#### ImageSourceType (enum)
`IMAGE` | `ENTITYKEY`

#### ErrorComponentAllOfException
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| cause | ErrorComponentAllOfExceptionCause |  | [optional] |
| stack_trace | List[ErrorComponentAllOfExceptionCauseStackTrace] |  | [optional] |
| message | str |  | [optional] |
| suppressed | List[ErrorComponentAllOfExceptionCause] |  | [optional] |
| localized_message | str |  | [optional] |

#### BorderLength (enum)
`LONG` | `SHORT`

#### BorderType (enum)
`SOLID` | `DASHED` | `DOTTED`

#### AliasEntityId
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| alias_entity_type | AliasEntityType |  | [optional] |
| entity_type | EntityType |  |  |
| id | UUID | ID of the entity, time-based UUID v1 |  |

#### EntityType (enum)
`TENANT` | `CUSTOMER` | `USER` | `DASHBOARD` | `ASSET` | `DEVICE` | `ALARM` | `ENTITY_GROUP` | `CONVERTER` | `INTEGRATION` | … (52 values total)

#### EntitySearchDirection (enum)
`FROM` | `TO`

#### RelationEntityTypeFilter
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| relation_type | str | Type of the relation between root entity and other entity (e.g. 'Contains' or 'Manages'). | [optional] |
| entity_types | List[EntityType] | Array of entity types to filter the related entities (e.g. 'DEVICE', 'ASSET'). | [optional] |
| negate | bool | Negate relation type between root entity and other entity. | [optional] |

#### EntityKeyType (enum)
`ATTRIBUTE` | `CLIENT_ATTRIBUTE` | `SHARED_ATTRIBUTE` | `SERVER_ATTRIBUTE` | `TIME_SERIES` | `ENTITY_FIELD` | `ALARM_FIELD`

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

#### FontWeight (enum)
`NORMAL` | `BOLD` | `ENUM_500`

#### FontStyle (enum)
`NORMAL` | `ITALIC`

#### TableSortDirection (enum)
`ASC` | `DESC`

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

#### CellSettings
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| font | Font |  | [optional] |
| color | str |  | [optional] |
| background_color | str |  | [optional] |
| text_alignment | TextAlignment |  | [optional] |
| vertical_alignment | VerticalAlignment |  | [optional] |

#### DataKeySettingsType (enum)
`COLUMN` | `TIME_SERIES_CHART` | `DEFAULT`

#### TimeSeriesChartThreshold
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| type | ValueSourceType |  | [optional] |
| value | float |  | [optional] |
| latest_key_type | str |  | [optional] |
| latest_key | str |  | [optional] |
| entity_key_type | str |  | [optional] |
| entity_alias | str |  | [optional] |
| entity_key | str |  | [optional] |
| y_axis_id | str |  | [optional] |
| units | str |  | [optional] |
| decimals | int |  | [optional] |
| line_color | str |  | [optional] |
| line_type | ChartLineType |  | [optional] |
| line_width | float |  | [optional] |
| start_symbol | ChartShape |  | [optional] |
| start_symbol_size | float |  | [optional] |
| end_symbol | ChartShape |  | [optional] |
| end_symbol_size | float |  | [optional] |
| show_label | bool |  | [optional] |
| label_position | ThresholdLabelPosition |  | [optional] |
| label_font | Font |  | [optional] |
| label_color | str |  | [optional] |
| enable_label_background | bool |  | [optional] |
| label_background | str |  | [optional] |
| yaxis_id | str |  | [optional] |

#### TimeSeriesChartGridSettings
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| show | bool |  | [optional] |
| background_color | str |  | [optional] |
| border_width | float |  | [optional] |
| border_color | str |  | [optional] |

#### TimeSeriesChartYAxisSettings
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| show | bool |  | [optional] |
| label | str |  | [optional] |
| label_font | Font |  | [optional] |
| label_color | str |  | [optional] |
| position | AxisPosition |  | [optional] |
| show_tick_labels | bool |  | [optional] |
| tick_label_font | Font |  | [optional] |
| tick_label_color | str |  | [optional] |
| show_ticks | bool |  | [optional] |
| ticks_color | str |  | [optional] |
| show_line | bool |  | [optional] |
| line_color | str |  | [optional] |
| show_split_lines | bool |  | [optional] |
| split_lines_color | str |  | [optional] |
| id | str |  | [optional] |
| order | int |  | [optional] |
| units | str |  | [optional] |
| decimals | int |  | [optional] |
| interval | float |  | [optional] |
| split_number | int |  | [optional] |
| min | float |  | [optional] |
| max | float |  | [optional] |

#### TimeSeriesChartXAxisSettings
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| show | bool |  | [optional] |
| label | str |  | [optional] |
| label_font | Font |  | [optional] |
| label_color | str |  | [optional] |
| position | AxisPosition |  | [optional] |
| show_tick_labels | bool |  | [optional] |
| tick_label_font | Font |  | [optional] |
| tick_label_color | str |  | [optional] |
| show_ticks | bool |  | [optional] |
| ticks_color | str |  | [optional] |
| show_line | bool |  | [optional] |
| line_color | str |  | [optional] |
| show_split_lines | bool |  | [optional] |
| split_lines_color | str |  | [optional] |
| ticks_format | Dict[str, str] |  | [optional] |

#### TimeSeriesChartBarWidthSettings
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| bar_gap | float |  | [optional] |
| interval_gap | float |  | [optional] |

#### TimeSeriesChartNoAggregationBarWidthSettings
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| strategy | TimeSeriesChartNoAggregationBarWidthStrategy |  | [optional] |
| group_width | TimeSeriesChartBarWidth |  | [optional] |
| bar_width | TimeSeriesChartBarWidth |  | [optional] |

#### TimeSeriesChartStateSettings
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| label | str |  | [optional] |
| value | float |  | [optional] |
| source_type | TimeSeriesChartStateSourceType |  | [optional] |
| source_value | object |  | [optional] |
| source_range_from | float |  | [optional] |
| source_range_to | float |  | [optional] |

#### ComparisonDuration (enum)
`PREVIOUSINTERVAL` | `DAYS` | `WEEKS` | `MONTHS` | `YEARS` | `CUSTOMINTERVAL`

#### LegendConfig
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| position | LegendPosition |  | [optional] |
| sort_data_keys | bool |  | [optional] |
| show_min | bool |  | [optional] |
| show_max | bool |  | [optional] |
| show_avg | bool |  | [optional] |
| show_total | bool |  | [optional] |
| show_latest | bool |  | [optional] |

#### LegendPosition (enum)
`TOP` | `BOTTOM` | `LEFT` | `RIGHT`

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
| native_method | bool |  | [optional] |
| class_name | str |  | [optional] |

#### AliasEntityType (enum)
`CURRENT_CUSTOMER` | `CURRENT_TENANT` | `CURRENT_USER` | `CURRENT_USER_OWNER`

#### StringOperation (enum)
`EQUAL` | `NOT_EQUAL` | `STARTS_WITH` | `ENDS_WITH` | `CONTAINS` | `NOT_CONTAINS` | `IN` | `NOT_IN`

#### FilterPredicateValueString
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| default_value | str |  | [optional] |
| user_value | str |  | [optional] |
| dynamic_value | DynamicValueString |  | [optional] |

#### NumericOperation (enum)
`EQUAL` | `NOT_EQUAL` | `GREATER` | `LESS` | `GREATER_OR_EQUAL` | `LESS_OR_EQUAL`

#### FilterPredicateValueDouble
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| default_value | float |  | [optional] |
| user_value | float |  | [optional] |
| dynamic_value | DynamicValueDouble |  | [optional] |

#### BooleanOperation (enum)
`EQUAL` | `NOT_EQUAL`

#### FilterPredicateValueBoolean
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| default_value | bool |  | [optional] |
| user_value | bool |  | [optional] |
| dynamic_value | DynamicValueBoolean |  | [optional] |

#### ComplexOperation (enum)
`AND` | `OR`

#### Aggregation (enum)
`MIN` | `MAX` | `AVG` | `SUM` | `COUNT` | `NONE`

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

#### ValueSourceType (enum)
`CONSTANT` | `LATESTKEY` | `ENTITY`

#### ChartLineType (enum)
`SOLID` | `DASHED` | `DOTTED`

#### ChartShape (enum)
`EMPTYCIRCLE` | `CIRCLE` | `RECT` | `ROUNDRECT` | `TRIANGLE` | `DIAMOND` | `PIN` | `ARROW` | `NONE`

#### ThresholdLabelPosition (enum)
`START` | `MIDDLE` | `END` | `INSIDESTART` | `INSIDESTARTTOP` | `INSIDESTARTBOTTOM` | `INSIDEMIDDLE` | `INSIDEMIDDLETOP` | `INSIDEMIDDLEBOTTOM` | `INSIDEEND` | … (12 values total)

#### AxisPosition (enum)
`LEFT` | `RIGHT` | `TOP` | `BOTTOM`

#### TimeSeriesChartNoAggregationBarWidthStrategy (enum)
`GROUP` | `SEPARATE`

#### TimeSeriesChartBarWidth
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| relative | bool |  | [optional] |
| relative_width | float |  | [optional] |
| absolute_width | float |  | [optional] |

#### TimeSeriesChartStateSourceType (enum)
`CONSTANT` | `RANGE`

#### DynamicValueString
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| resolved_value | str |  | [optional] |
| source_type | DynamicValueSourceType |  | [optional] |
| source_attribute | str |  | [optional] |
| inherit | bool |  | [optional] |

#### DynamicValueDouble
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| resolved_value | float |  | [optional] |
| source_type | DynamicValueSourceType |  | [optional] |
| source_attribute | str |  | [optional] |
| inherit | bool |  | [optional] |

#### DynamicValueBoolean
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| resolved_value | bool |  | [optional] |
| source_type | DynamicValueSourceType |  | [optional] |
| source_attribute | str |  | [optional] |
| inherit | bool |  | [optional] |

#### IntervalType (enum)
`MILLISECONDS` | `WEEK` | `WEEK_ISO` | `MONTH` | `QUARTER`

#### DynamicValueSourceType (enum)
`CURRENT_TENANT` | `CURRENT_CUSTOMER` | `CURRENT_USER` | `CURRENT_DEVICE`

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

#### LineSeriesStepType (enum)
`START` | `MIDDLE` | `END`

#### ChartLabelPosition (enum)
`TOP` | `BOTTOM`

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
- **Attribute access:** `obj.name_pattern`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `ReportTemplateConfig.model_validate(data)` or `ReportTemplateConfig.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

