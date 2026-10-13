# ReportTemplateControllerApi

`ThingsboardClient` methods:

```python
None client.delete_report_template(report_template_id: str)  # Delete Report Template (deleteReportTemplate)
PageDataReportTemplateInfo client.get_all_report_template_infos(page_size: int, page: int, type_list: Optional[List[str]] = None, format_list: Optional[List[str]] = None, include_customers: Optional[bool] = None, text_search: Optional[str] = None, sort_property: Optional[str] = None, sort_order: Optional[str] = None)  # Get All Report Templates for current user (getAllReportTemplateInfos)
ReportTemplate client.get_report_template_by_id(report_template_id: str)  # Get Report Template (getReportTemplateById)
ReportTemplateInfo client.get_report_template_info_by_id(report_template_id: str)  # Get Report Template Info (getReportTemplateInfoById)
List[ReportTemplateInfo] client.get_report_templates_by_ids(report_template_ids: List[str])  # Get report templates by Report Template Ids (getReportTemplatesByIds)
ReportTemplate client.save_report_template(report_template: ReportTemplate)  # Save Report Template (saveReportTemplate)
```


## delete_report_template

```python
None client.delete_report_template(report_template_id: str)
```

**DELETE** `/api/reportTemplate/{reportTemplateId}`

Delete Report Template (deleteReportTemplate)

Deletes the report template. Referencing non-existing Report Template Id will cause 'Not Found' error.   Security check is performed to verify that the user has 'DELETE' permission for the entity (entities).


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **report_template_id** | **str** | A string value representing the report template id. For example, '784f394c-42b6-435a-983c-b7beff2784f9' | |

### Return type

None (empty response body)


## get_all_report_template_infos

```python
PageDataReportTemplateInfo client.get_all_report_template_infos(page_size: int, page: int, type_list: Optional[List[str]] = None, format_list: Optional[List[str]] = None, include_customers: Optional[bool] = None, text_search: Optional[str] = None, sort_property: Optional[str] = None, sort_order: Optional[str] = None)
```

**GET** `/api/reportTemplateInfos/all`

Get All Report Templates for current user (getAllReportTemplateInfos)

Returns a page of report template info objects owned by the tenant or the customer of a current user. Report Templates allows you to create reports according to the report template configuration. Report service uses report template configuration to generate report. See the 'Model' tab of the Response Class for more details.  You can specify parameters to filter the results. The result is wrapped with PageData object that allows you to iterate over result set using pagination. See response schema for more details.   Available for users with 'TENANT_ADMIN' or 'CUSTOMER_USER' authority. Security check is performed to verify that the user has 'READ' permission for the entity (entities).


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **page_size** | **int** | Maximum amount of entities in a one page | |
| **page** | **int** | Sequence number of page starting from 0 | |
| **type_list** | **List[str]** | A list of string values separated by comma ',' representing one of the ReportTemplateType enumeration value. | [optional] [enum: REPORT, SUB_REPORT] |
| **format_list** | **List[str]** | A list of string values separated by comma ',' representing one of the TbReportFormat enumeration value. | [optional] [enum: PDF, CSV] |
| **include_customers** | **bool** | Include customer or sub-customer entities. For tenant administrator: when true, includes entities for all customers; when false (default), only own entities are returned. For customer user: when true, includes entities for all sub-customers. | [optional] |
| **text_search** | **str** | The case insensitive 'substring' filter based on the report template name or customer title. | [optional] |
| **sort_property** | **str** | Property of entity to sort by | [optional] [enum: createdTime, name, ownerName] |
| **sort_order** | **str** | Sort order. ASC (ASCENDING) or DESC (DESCENDING) | [optional] [enum: ASC, DESC] |

### Return type

**PageDataReportTemplateInfo**


## get_report_template_by_id

```python
ReportTemplate client.get_report_template_by_id(report_template_id: str)
```

**GET** `/api/reportTemplate/{reportTemplateId}`

Get Report Template (getReportTemplateById)

Fetch the ReportTemplate object based on the provided report template Id. Report Template extends Report Template Info object and adds 'configuration' - a JSON structure of report template configuration. See the 'Model' tab of the Response Class for more details. Referencing non-existing Report Template Id will cause 'Not Found' error.  Available for users with 'TENANT_ADMIN' or 'CUSTOMER_USER' authority.   Security check is performed to verify that the user has 'READ' permission for the entity (entities).


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **report_template_id** | **str** | A string value representing the report template id. For example, '784f394c-42b6-435a-983c-b7beff2784f9' | |

### Return type

**ReportTemplate**


## get_report_template_info_by_id

```python
ReportTemplateInfo client.get_report_template_info_by_id(report_template_id: str)
```

**GET** `/api/reportTemplate/info/{reportTemplateId}`

Get Report Template Info (getReportTemplateInfoById)

Fetch the ReportTemplateInfo object based on the provided report template Id. Report Templates allows you to create reports according to the report template configuration. Report service uses report template configuration to generate report. See the 'Model' tab of the Response Class for more details. Referencing non-existing Report Template Id will cause 'Not Found' error.  Available for users with 'TENANT_ADMIN' or 'CUSTOMER_USER' authority.   Security check is performed to verify that the user has 'READ' permission for the entity (entities).


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **report_template_id** | **str** | A string value representing the report template id. For example, '784f394c-42b6-435a-983c-b7beff2784f9' | |

### Return type

**ReportTemplateInfo**


## get_report_templates_by_ids

```python
List[ReportTemplateInfo] client.get_report_templates_by_ids(report_template_ids: List[str])
```

**GET** `/api/reportTemplates`

Get report templates by Report Template Ids (getReportTemplatesByIds)

Returns a list of ReportTemplateInfo objects based on the provided ids. Filters the list based on the user permissions.   Available for users with 'TENANT_ADMIN' or 'CUSTOMER_USER' authority. Security check is performed to verify that the user has 'READ' permission for the entity (entities).


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **report_template_ids** | **List[str]** | A list of report template ids, separated by comma ',' | |

### Return type

**List[ReportTemplateInfo]**


## save_report_template

```python
ReportTemplate client.save_report_template(report_template: ReportTemplate)
```

**POST** `/api/reportTemplate`

Save Report Template (saveReportTemplate)

Creates or Updates report template. Report Template extends Report Template Info object and adds 'configuration' - a JSON structure of report template configuration. See the 'Model' tab of the Response Class for more details. When creating report template, platform generates report template Id as [time-based UUID](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_1_(date-time_and_MAC_address)). The newly created report template id will be present in the response. Specify existing report template id to update the report template. Referencing non-existing report template Id will cause 'Not Found' error. Remove 'id', 'tenantId' and optionally 'customerId' from the request body example (below) to create new Report Template entity.   Available for users with 'TENANT_ADMIN' or 'CUSTOMER_USER' authority.   Security check is performed to verify that the user has 'WRITE' permission for the entity (entities).


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **report_template** | **ReportTemplate** |  | |

### Return type

**ReportTemplate**

