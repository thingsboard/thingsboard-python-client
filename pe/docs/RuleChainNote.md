
# RuleChainNote

`tb_pe_client.models.RuleChainNote`

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **id** | **str** | Unique identifier of the note on the canvas | [optional] |
| **x** | **int** | Horizontal position of the note on the canvas, in pixels | [optional] |
| **y** | **int** | Vertical position of the note on the canvas, in pixels | [optional] |
| **width** | **int** | Width of the note, in pixels | [optional] |
| **height** | **int** | Height of the note, in pixels | [optional] |
| **content** | **str** | Markdown or HTML content of the note | [optional] |
| **background_color** | **str** | Background color of the note in CSS hex format, e.g. '#FFF9C4' | [optional] |
| **border_color** | **str** | Border color of the note in CSS hex format, e.g. '#E6C800' | [optional] |
| **border_width** | **int** | Border width of the note in pixels | [optional] |
| **apply_default_markdown_style** | **bool** | Whether to apply the default markdown stylesheet to the note content | [optional] |
| **markdown_css** | **str** | Custom CSS styles applied to the note content | [optional] |



---

### Conventions

- **Package:** `tb_pe_client.models`
- **Attribute access:** `obj.id`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `RuleChainNote.model_validate(data)` or `RuleChainNote.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

