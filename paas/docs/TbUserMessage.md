
# TbUserMessage

`tb_paas_client.models.TbUserMessage`

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **contents** | [**List[TbContent]**](TbContent.md) | A list of content parts that make up the complete user prompt | |



## Referenced Types

#### TbContent
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| content_type | str |  |  |

#### TbTextContent  *(extends TbContent, content_type=`TEXT`)*
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| text | str | The text content |  |

---

### Conventions

- **Package:** `tb_paas_client.models`
- **Attribute access:** `obj.contents`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `TbUserMessage.model_validate(data)` or `TbUserMessage.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

