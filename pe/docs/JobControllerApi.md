# JobControllerApi

`ThingsboardClient` methods:

```python
None client.cancel_job(id: UUID)  # Cancel job (cancelJob)
None client.delete_job(id: UUID)  # deleteJob
Job client.get_job_by_id(id: UUID)  # Get job by id (getJobById)
PageDataJob client.get_jobs(page_size: int, page: int, text_search: Optional[str] = None, sort_property: Optional[str] = None, sort_order: Optional[str] = None, types: Optional[List[str]] = None, statuses: Optional[List[str]] = None, entities: Optional[List[str]] = None, start_time: Optional[int] = None, end_time: Optional[int] = None, include_customers: Optional[bool] = None)  # Get jobs (getJobs)
None client.reprocess_job(id: UUID)  # Reprocess job (reprocessJob)
```


## cancel_job

```python
None client.cancel_job(id: UUID)
```

**POST** `/api/job/{id}/cancel`

Cancel job (cancelJob)

Cancels the job. The status of the job must be QUEUED, PENDING or RUNNING.  For a running job, all the tasks not yet processed will be discarded.  See the example of a cancelled job result in getJobById method description.  Available for users with 'TENANT_ADMIN' or 'CUSTOMER_USER' authority.


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **UUID** |  | |

### Return type

None (empty response body)


## delete_job

```python
None client.delete_job(id: UUID)
```

**DELETE** `/api/job/{id}`

deleteJob


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **UUID** |  | |

### Return type

None (empty response body)


## get_job_by_id

```python
Job client.get_job_by_id(id: UUID)
```

**GET** `/api/job/{id}`

Get job by id (getJobById)

Fetches job info by id.  Example of a RUNNING CF_REPROCESSING job response: ```json {   \"id\": {     \"entityType\": \"JOB\",     \"id\": \"475e94e0-2f2d-11f0-8240-91e99922a704\"   },   \"createdTime\": 1747053196590,   \"tenantId\": {     \"entityType\": \"TENANT\",     \"id\": \"46859a00-2f2d-11f0-8240-91e99922a704\"   },   \"type\": \"CF_REPROCESSING\",   \"key\": \"474e4130-2f2d-11f0-8240-91e99922a704\",   \"entityId\": {     \"entityType\": \"DEVICE_PROFILE\",     \"id\": \"9fd41f20-31a1-11f0-933e-27998d6db02e\"    },   \"status\": \"RUNNING\",   \"configuration\": {     \"type\": \"CF_REPROCESSING\",     \"calculatedFieldId\": {       \"entityType\": \"CALCULATED_FIELD\",       \"id\": \"474e4130-2f2d-11f0-8240-91e99922a704\"     },     \"startTs\": 1747051995760,     \"endTs\": 1747052895760,     \"tasksKey\": \"c3cdbd42-799e-4d3a-9aad-9310f767aa36\",     \"toReprocess\": null   },   \"result\": {     \"jobType\": \"CF_REPROCESSING\",     \"successfulCount\": 1,     \"failedCount\": 0,     \"discardedCount\": 0,     \"totalCount\": 2,     \"results\": [],     \"generalError\": null,     \"startTs\": 1747323069445,     \"finishTs\": 1747323070585,     \"cancellationTs\": 0   } }  ```  Example of a CF_REPROCESSING job with failures: ```json {   ...,   \"status\": \"FAILED\",   ...,   \"result\": {     \"jobType\": \"CF_REPROCESSING\",     \"successfulCount\": 0,     \"failedCount\": 2,     \"discardedCount\": 0,     \"totalCount\": 2,     \"results\": [       {         \"jobType\": \"CF_REPROCESSING\",         \"key\": \"c3cdbd42-799e-4d3a-9aad-9310f767aa36\",         \"success\": false,         \"discarded\": false,         \"failure\": {           \"error\": \"Failed to fetch temperature: Failed to fetch timeseries data\",           \"entityInfo\": {             \"id\": {               \"entityType\": \"DEVICE\",               \"id\": \"9fd41f20-31a1-11f0-933e-27998d6db02e\"             },             \"name\": \"Test device 1\"           }         }       },       {         \"jobType\": \"CF_REPROCESSING\",         \"key\": \"c3cdbd42-799e-4d3a-9aad-9310f767aa36\",         \"success\": false,         \"discarded\": false,         \"failure\": {           \"error\": \"Failed to fetch temperature: Failed to fetch timeseries data\",           \"entityInfo\": {             \"id\": {               \"entityType\": \"DEVICE\",               \"id\": \"9ffc4090-31a1-11f0-933e-27998d6db02e\"             },             \"name\": \"Test device 2\"           }         }       }     ],     \"generalError\": null,     \"startTs\": 1747323069445,     \"finishTs\": 1747323070585,     \"cancellationTs\": 0   } }  ```  Example of a FAILED job result with general error: ```json {   ...,   \"status\": \"FAILED\",   ...,   \"result\": {     \"jobType\": \"CF_REPROCESSING\",     \"successfulCount\": 1,     \"failedCount\": 0,     \"discardedCount\": 0,     \"totalCount\": null,     \"results\": [],     \"generalError\": \"Timeout to find devices by profile\",     \"cancellationTs\": 0   } }  ```  Example of a CANCELLED job result: ```json {   ...,   \"status\": \"CANCELLED\",   ...,   \"result\": {     \"jobType\": \"CF_REPROCESSING\",     \"successfulCount\": 15,     \"failedCount\": 0,     \"discardedCount\": 85,     \"totalCount\": 100,     \"results\": [],     \"generalError\": null,     \"cancellationTs\": 1747065908414   } }  ```  Available for users with 'TENANT_ADMIN' or 'CUSTOMER_USER' authority.


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **UUID** |  | |

### Return type

**Job**


## get_jobs

```python
PageDataJob client.get_jobs(page_size: int, page: int, text_search: Optional[str] = None, sort_property: Optional[str] = None, sort_order: Optional[str] = None, types: Optional[List[str]] = None, statuses: Optional[List[str]] = None, entities: Optional[List[str]] = None, start_time: Optional[int] = None, end_time: Optional[int] = None, include_customers: Optional[bool] = None)
```

**GET** `/api/jobs`

Get jobs (getJobs)

Returns the page of jobs.  You can specify parameters to filter the results. The result is wrapped with PageData object that allows you to iterate over result set using pagination. See response schema for more details.   Available for users with 'TENANT_ADMIN' or 'CUSTOMER_USER' authority.


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **page_size** | **int** | Maximum amount of entities in a one page | |
| **page** | **int** | Sequence number of page starting from 0 | |
| **text_search** | **str** | Case-insensitive 'substring' filter based on job's description | [optional] |
| **sort_property** | **str** | Property of entity to sort by | [optional] |
| **sort_order** | **str** | Sort order. ASC (ASCENDING) or DESC (DESCENDING) | [optional] |
| **types** | **List[str]** | Comma-separated list of job types to include. If empty - all job types are included. | [optional] |
| **statuses** | **List[str]** | Comma-separated list of job statuses to include. If empty - all job statuses are included. | [optional] |
| **entities** | **List[str]** | Comma-separated list of entity ids. If empty - jobs for all entities are included. | [optional] |
| **start_time** | **int** | To only include jobs created after this timestamp. | [optional] |
| **end_time** | **int** | To only include jobs created before this timestamp. | [optional] |
| **include_customers** | **bool** | Include customer or sub-customer entities. For tenant administrator: when true, includes entities for all customers; when false (default), only own entities are returned. For customer user: when true, includes entities for all sub-customers. | [optional] |

### Return type

**PageDataJob**


## reprocess_job

```python
None client.reprocess_job(id: UUID)
```

**POST** `/api/job/{id}/reprocess`

Reprocess job (reprocessJob)

Reprocesses the job. Failures are located at job.result.results list. Platform iterates over this list and submits new tasks for them. Doesn't create new job entity but updates the existing one. Successfully reprocessed job will look the same as completed one.  Available for users with 'TENANT_ADMIN' or 'CUSTOMER_USER' authority.


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **UUID** |  | |

### Return type

None (empty response body)

