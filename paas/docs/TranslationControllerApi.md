# TranslationControllerApi

`ThingsboardClient` methods:

```python
bytearray client.download_full_translation(locale_code: str)  # Download end-user all-to-one translation (downloadFullTranslation)
object client.get_available_java_locales()  # Get list of available java locales (getAvailableJavaLocales)
object client.get_available_locales()  # Get list of available locales (getAvailableLocales)
object client.get_full_translation(locale_code: str, if_none_match: Optional[str] = None, accept_encoding: Optional[str] = None)  # Get end-user all-to-one translation (getFullTranslation)
object client.get_login_page_translation(locale_code: str, if_none_match: Optional[str] = None, accept_encoding: Optional[str] = None)  # Get system translation for login page
object client.get_translation_for_basic_edit(locale_code: str)  # Get end-user multi-translation for basic edit (getTranslationForBasicEdit)
List[TranslationInfo] client.get_translation_infos()  # Get Translation info (getTranslationInfos)
```


## download_full_translation

```python
bytearray client.download_full_translation(locale_code: str)
```

**GET** `/api/translation/full/{localeCode}/download`

Download end-user all-to-one translation (downloadFullTranslation)

Fetch the end-user translation for the specified locale. The result is a json file with merged user custom translation, system language translation and default locale translation.


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **locale_code** | **str** | Locale code (e.g. 'en_US'). | |

### Return type

**bytearray**


## get_available_java_locales

```python
object client.get_available_java_locales()
```

**GET** `/api/translation/availableJavaLocales`

Get list of available java locales (getAvailableJavaLocales)

The result is map where key is locale code and value is locale language and country

### Return type

**object**


## get_available_locales

```python
object client.get_available_locales()
```

**GET** `/api/translation/availableLocales`

Get list of available locales (getAvailableLocales)

Fetch the list of customized locales from all levels  Security check is performed to verify that the user has 'READ' permission for the white labeling resource.

### Return type

**object**


## get_full_translation

```python
object client.get_full_translation(locale_code: str, if_none_match: Optional[str] = None, accept_encoding: Optional[str] = None)
```

**GET** `/api/translation/full/{localeCode}`

Get end-user all-to-one translation (getFullTranslation)

Fetch the end-user translation for specified locale. The result is the merge of user custom translation, system language translation and default locale translation.


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **locale_code** | **str** | Locale code (e.g. 'en_US'). | |
| **if_none_match** | **str** |  | [optional] |
| **accept_encoding** | **str** |  | [optional] |

### Return type

**object**


## get_login_page_translation

```python
object client.get_login_page_translation(locale_code: str, if_none_match: Optional[str] = None, accept_encoding: Optional[str] = None)
```

**GET** `/api/noauth/translation/login/{localeCode}`

Get system translation for login page

Fetch the end-user translation for specified locale.


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **locale_code** | **str** | Locale code (e.g. 'en_US'). | |
| **if_none_match** | **str** |  | [optional] |
| **accept_encoding** | **str** |  | [optional] |

### Return type

**object**


## get_translation_for_basic_edit

```python
object client.get_translation_for_basic_edit(locale_code: str)
```

**GET** `/api/translation/edit/basic/{localeCode}`

Get end-user multi-translation for basic edit (getTranslationForBasicEdit)

Fetch the translation info map where value is info object containing key translation, origin translation, translation of parent level, translation status.


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **locale_code** | **str** |  | |

### Return type

**object**


## get_translation_infos

```python
List[TranslationInfo] client.get_translation_infos()
```

**GET** `/api/translation/info`

Get Translation info (getTranslationInfos)

Fetch the list of customized locales and corresponding details such as language display name, country display name and translation progress percentage.   Response example:   ```json [   {     \"localeCode\": \"uk_UA\",     \"language\": \"Ukrainian (українська)\",     \"country\": \"Україна\",     \"progress\": 32   },   {     \"localeCode\": \"es_ES\",     \"language\": \"Spanish (español)\",     \"country\": \"España\",     \"progress\": 79   }] ```  Security check is performed to verify that the user has 'READ' permission for the white labeling resource.

### Return type

**List[TranslationInfo]**

