# AiSolutionControllerApi

`ThingsboardClient` methods:

```python
object client.chat(solution_id: UUID, step: SolutionStep, body: str)  # chat
None client.clear_step(solution_id: UUID, step: SolutionStep)  # clearStep
object client.create_solution(solution_id: UUID)  # createSolution
None client.delete_solution(solution_id: UUID)  # deleteSolution
object client.get_solution(solution_id: UUID)  # getSolution
object client.get_solutions()  # getSolutions
object client.install_solution(solution_id: UUID, x_authorization: str)  # installSolution
object client.start_new()  # startNew
object client.uninstall_solution(solution_id: UUID, x_authorization: str)  # uninstallSolution
object client.update_data(solution_id: UUID, data_key: str, body: object)  # updateData
```


## chat

```python
object client.chat(solution_id: UUID, step: SolutionStep, body: str)
```

**POST** `/api/ai/solution/{solutionId}/{step}/chat`

chat


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **solution_id** | **UUID** |  | |
| **step** | **SolutionStep** |  | [enum: INITIAL_CONFIGURATION, DASHBOARDS_CONFIGURATION] |
| **body** | **str** |  | |

### Return type

**object**


## clear_step

```python
None client.clear_step(solution_id: UUID, step: SolutionStep)
```

**DELETE** `/api/ai/solution/{solutionId}/{step}/clear`

clearStep


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **solution_id** | **UUID** |  | |
| **step** | **SolutionStep** |  | [enum: INITIAL_CONFIGURATION, DASHBOARDS_CONFIGURATION] |

### Return type

None (empty response body)


## create_solution

```python
object client.create_solution(solution_id: UUID)
```

**POST** `/api/ai/solution/{solutionId}/create`

createSolution


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **solution_id** | **UUID** |  | |

### Return type

**object**


## delete_solution

```python
None client.delete_solution(solution_id: UUID)
```

**DELETE** `/api/ai/solution/{solutionId}`

deleteSolution


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **solution_id** | **UUID** |  | |

### Return type

None (empty response body)


## get_solution

```python
object client.get_solution(solution_id: UUID)
```

**GET** `/api/ai/solution/{solutionId}`

getSolution


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **solution_id** | **UUID** |  | |

### Return type

**object**


## get_solutions

```python
object client.get_solutions()
```

**GET** `/api/ai/solution/infos`

getSolutions

### Return type

**object**


## install_solution

```python
object client.install_solution(solution_id: UUID, x_authorization: str)
```

**POST** `/api/ai/solution/{solutionId}/install`

installSolution


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **solution_id** | **UUID** |  | |
| **x_authorization** | **str** |  | |

### Return type

**object**


## start_new

```python
object client.start_new()
```

**POST** `/api/ai/solution/start`

startNew

### Return type

**object**


## uninstall_solution

```python
object client.uninstall_solution(solution_id: UUID, x_authorization: str)
```

**DELETE** `/api/ai/solution/{solutionId}/uninstall`

uninstallSolution


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **solution_id** | **UUID** |  | |
| **x_authorization** | **str** |  | |

### Return type

**object**


## update_data

```python
object client.update_data(solution_id: UUID, data_key: str, body: object)
```

**PUT** `/api/ai/solution/{solutionId}/{dataKey}`

updateData


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **solution_id** | **UUID** |  | |
| **data_key** | **str** |  | |
| **body** | **object** |  | |

### Return type

**object**

