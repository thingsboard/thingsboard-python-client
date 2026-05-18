# SolutionExportImportControllerApi

`ThingsboardClient` methods:

```python
SolutionExportResponse client.export_solution(solution_export_request: SolutionExportRequest)  # Export Solution (exportSolution)
SolutionImportResult client.import_solution(solution_data: SolutionData)  # Import Solution (importSolution)
SolutionValidationResult client.validate_solution(solution_data: SolutionData)  # Validate Solution (validateSolution)
```


## export_solution

```python
SolutionExportResponse client.export_solution(solution_export_request: SolutionExportRequest)
```

**POST** `/api/solution/export`

Export Solution (exportSolution)

Exports a set of entities as a portable solution package. The request specifies entity IDs to include and optional export settings (relations, attributes, credentials). All specified entities must belong to the current tenant. The response contains the solution data (entities grouped by type) and any dependency warnings (e.g. when an exported device profile references a rule chain that was not included in the export). The solution data can later be imported into the same or a different tenant via the import endpoint.  Available for users with 'TENANT_ADMIN' authority. Requires VERSION_CONTROL WRITE permission.


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **solution_export_request** | **SolutionExportRequest** | Export request with entity IDs and optional settings. | |

### Return type

**SolutionExportResponse**


## import_solution

```python
SolutionImportResult client.import_solution(solution_data: SolutionData)
```

**POST** `/api/solution/import`

Import Solution (importSolution)

Imports a solution package into the current tenant. Before importing, the endpoint checks for name conflicts with existing entities in the tenant. If name conflicts are detected, the import is rejected with HTTP 409 (Conflict). The import is transactional — if any entity fails to import, all changes are rolled back (all-or-nothing). Entities are imported in dependency order with a two-pass resolution for circular references (e.g. rule chains referencing each other).  Available for users with 'TENANT_ADMIN' authority. Requires VERSION_CONTROL WRITE permission.


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **solution_data** | **SolutionData** | Solution data exported via the export endpoint. | |

### Return type

**SolutionImportResult**


## validate_solution

```python
SolutionValidationResult client.validate_solution(solution_data: SolutionData)
```

**POST** `/api/solution/validate`

Validate Solution (validateSolution)

Performs a dry-run validation of a solution without modifying any data. Detects duplicate entities within the solution, identifies name conflicts with existing entities in the current tenant, and reports missing dependency references (e.g. a device profile referencing an absent rule chain). The result indicates whether the solution is safe to import (valid=true) and lists any conflicts or warnings.  Available for users with 'TENANT_ADMIN' authority. Requires VERSION_CONTROL WRITE permission.


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **solution_data** | **SolutionData** | Solution data to validate. | |

### Return type

**SolutionValidationResult**

