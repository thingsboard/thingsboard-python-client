# AiChatControllerApi

`ThingsboardClient` methods:

```python
object client.create_chat(body: object)  # createChat
None client.delete_chat(chat_id: UUID)  # deleteChat
object client.get_chat_messages(chat_id: UUID)  # getChatMessages
object client.list_chats(chat_type: ChatType)  # listChats
List[object] client.send_chat_message(chat_id: UUID, x_authorization: str, body: str, accept_language: Optional[str] = None)  # sendChatMessage
None client.update_chat(chat_id: UUID, body: object)  # updateChat
```


## create_chat

```python
object client.create_chat(body: object)
```

**POST** `/api/ai/chats`

createChat


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **body** | **object** |  | |

### Return type

**object**


## delete_chat

```python
None client.delete_chat(chat_id: UUID)
```

**DELETE** `/api/ai/chats/{chatId}`

deleteChat


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **chat_id** | **UUID** |  | |

### Return type

None (empty response body)


## get_chat_messages

```python
object client.get_chat_messages(chat_id: UUID)
```

**GET** `/api/ai/chats/{chatId}/messages`

getChatMessages


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **chat_id** | **UUID** |  | |

### Return type

**object**


## list_chats

```python
object client.list_chats(chat_type: ChatType)
```

**GET** `/api/ai/chats/{chatType}`

listChats


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **chat_type** | **ChatType** |  | [enum: GENERIC, SOLUTION_BUILDER] |

### Return type

**object**


## send_chat_message

```python
List[object] client.send_chat_message(chat_id: UUID, x_authorization: str, body: str, accept_language: Optional[str] = None)
```

**POST** `/api/ai/chats/{chatId}/messages`

sendChatMessage


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **chat_id** | **UUID** |  | |
| **x_authorization** | **str** |  | |
| **body** | **str** |  | |
| **accept_language** | **str** |  | [optional] |

### Return type

**List[object]**


## update_chat

```python
None client.update_chat(chat_id: UUID, body: object)
```

**PATCH** `/api/ai/chats/{chatId}`

updateChat


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **chat_id** | **UUID** |  | |
| **body** | **object** |  | |

### Return type

None (empty response body)

