# ReportControllerApi

`ThingsboardClient` methods:

```python
Report client.create_report(create_report_request: Optional[CreateReportRequest] = None)  # createReport
None client.delete_report(report_id: str)  # Delete Report (deleteReport)
bytearray client.download_report(report_id: UUID)  # downloadReport
bytearray client.download_report_by_public_key(public_key: str)  # Download report by public key (downloadReportByPublicKey)
Report client.get_report_by_id(report_id: str)  # Get Report (getReportById)
PageDataReportInfo client.get_report_infos(page_size: int, page: int, report_template_id: Optional[UUID] = None, user_id: Optional[UUID] = None, include_customers: Optional[bool] = None, text_search: Optional[str] = None, sort_property: Optional[str] = None, sort_order: Optional[str] = None)  # getReportInfos
List[ReportInfo] client.get_report_infos_by_ids(str_report_ids: List[str])  # getReportInfosByIds
PageDataReport client.get_reports(page_size: int, page: int, text_search: Optional[str] = None, sort_property: Optional[str] = None, sort_order: Optional[str] = None, include_customers: Optional[bool] = None)  # getReports
Job client.request_report(report_request: ReportRequest)  # requestReport
bytearray client.test_report_and_download(report_request: ReportRequest)  # Download test report (testReportAndDownload)
Report client.update_report_public_status(report_id: UUID, is_public: bool)  # Update Report public status (updateReportPublicStatus)
```


## create_report

```python
Report client.create_report(create_report_request: Optional[CreateReportRequest] = None)
```

**POST** `/api/v2/report`

createReport


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **create_report_request** | **CreateReportRequest** |  | [optional] |

### Return type

**Report**


## delete_report

```python
None client.delete_report(report_id: str)
```

**DELETE** `/api/v2/report/{reportId}`

Delete Report (deleteReport)

Deletes the report. Referencing non-existing Report Id will cause 'Not Found' error.   Security check is performed to verify that the user has 'DELETE' permission for the entity (entities).


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **report_id** | **str** | A string value representing the report id. For example, '784f394c-42b6-435a-983c-b7beff2784f9' | |

### Return type

None (empty response body)


## download_report

```python
bytearray client.download_report(report_id: UUID)
```

**GET** `/api/v2/report/{reportId}/download`

downloadReport


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **report_id** | **UUID** |  | |

### Return type

**bytearray**


## download_report_by_public_key

```python
bytearray client.download_report_by_public_key(public_key: str)
```

**GET** `/api/v2/report/public/{publicKey}/download`

Download report by public key (downloadReportByPublicKey)

Downloads the report identified by its public key. This endpoint is intentionally public: it requires no authentication and is accessible to anyone in possession of the report's random public key. It only returns data for reports that have been explicitly made public (see updateReportPublicStatus).


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **public_key** | **str** | The random public key of the report | |

### Return type

**bytearray**


## get_report_by_id

```python
Report client.get_report_by_id(report_id: str)
```

**GET** `/api/v2/report/{reportId}`

Get Report (getReportById)

Fetch the Report object based on the provided report Id. The platform uses Report to store generated reports information.Referencing non-existing Report Id will cause 'Not Found' error.  Available for users with 'TENANT_ADMIN' or 'CUSTOMER_USER' authority.   Security check is performed to verify that the user has 'READ' permission for the entity (entities).


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **report_id** | **str** | A string value representing the report id. For example, '784f394c-42b6-435a-983c-b7beff2784f9' | |

### Return type

**Report**


## get_report_infos

```python
PageDataReportInfo client.get_report_infos(page_size: int, page: int, report_template_id: Optional[UUID] = None, user_id: Optional[UUID] = None, include_customers: Optional[bool] = None, text_search: Optional[str] = None, sort_property: Optional[str] = None, sort_order: Optional[str] = None)
```

**GET** `/api/v2/reportInfos/all`

getReportInfos


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **page_size** | **int** | Maximum amount of entities in a one page | |
| **page** | **int** | Sequence number of page starting from 0 | |
| **report_template_id** | **UUID** | Report template id | [optional] |
| **user_id** | **UUID** | The user used for report generation. | [optional] |
| **include_customers** | **bool** | Include customer or sub-customer entities. For tenant administrator: when true, includes entities for all customers; when false (default), only own entities are returned. For customer user: when true, includes entities for all sub-customers. | [optional] |
| **text_search** | **str** | Case-insensitive 'substring' filter based on report's name or customer title | [optional] |
| **sort_property** | **str** | Property of entity to sort by | [optional] |
| **sort_order** | **str** | Sort order. ASC (ASCENDING) or DESC (DESCENDING) | [optional] |

### Return type

**PageDataReportInfo**


## get_report_infos_by_ids

```python
List[ReportInfo] client.get_report_infos_by_ids(str_report_ids: List[str])
```

**GET** `/api/v2/reportInfos`

getReportInfosByIds


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **str_report_ids** | **List[str]** | A list of report ids, separated by comma ',' | |

### Return type

**List[ReportInfo]**


## get_reports

```python
PageDataReport client.get_reports(page_size: int, page: int, text_search: Optional[str] = None, sort_property: Optional[str] = None, sort_order: Optional[str] = None, include_customers: Optional[bool] = None)
```

**GET** `/api/v2/reports`

getReports


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **page_size** | **int** | Maximum amount of entities in a one page | |
| **page** | **int** | Sequence number of page starting from 0 | |
| **text_search** | **str** | Case-insensitive 'substring' filter based on report's name or customer title | [optional] |
| **sort_property** | **str** | Property of entity to sort by | [optional] |
| **sort_order** | **str** | Sort order. ASC (ASCENDING) or DESC (DESCENDING) | [optional] |
| **include_customers** | **bool** | Include customer or sub-customer entities. For tenant administrator: when true, includes entities for all customers; when false (default), only own entities are returned. For customer user: when true, includes entities for all sub-customers. | [optional] |

### Return type

**PageDataReport**


## request_report

```python
Job client.request_report(report_request: ReportRequest)
```

**POST** `/api/v2/report/request`

requestReport


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **report_request** | **ReportRequest** |  | |

### Return type

**Job**


## test_report_and_download

```python
bytearray client.test_report_and_download(report_request: ReportRequest)
```

**POST** `/api/v2/report/test`

Download test report (testReportAndDownload)

Generate and download test report.  Available for users with 'TENANT_ADMIN' or 'CUSTOMER_USER' authority.


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **report_request** | **ReportRequest** |  | |

### Return type

**bytearray**


## update_report_public_status

```python
Report client.update_report_public_status(report_id: UUID, is_public: bool)
```

**PUT** `/api/v2/report/{reportId}/public/{isPublic}`

Update Report public status (updateReportPublicStatus)

Updates the public status of the report. When public, the report can be downloaded without authentication via the public link.   Available for users with 'TENANT_ADMIN' or 'CUSTOMER_USER' authority.


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **report_id** | **UUID** | A string value representing the report id. For example, '784f394c-42b6-435a-983c-b7beff2784f9' | |
| **is_public** | **bool** | Whether the report should be publicly downloadable without authentication | |

### Return type

**Report**

