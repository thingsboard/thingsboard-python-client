# AdminControllerApi

`ThingsboardClient` methods:

```python
bool client.auto_commit_settings_exists()  # Check auto commit settings exists (autoCommitSettingsExists)
None client.check_repository_access(repository_settings: RepositorySettings)  # Check repository access (checkRepositoryAccess)
UpdateMessage client.check_updates()  # Check for new Platform Releases (checkUpdates)
None client.delete_auto_commit_settings()  # Delete auto commit settings (deleteAutoCommitSettings)
None client.delete_repository_settings()  # Delete repository settings (deleteRepositorySettings)
AdminSettings client.get_admin_settings(key: str, system_by_default: Optional[bool] = None)  # Get the Administration Settings object using key (getAdminSettings)
Dict[str, AutoVersionCreateConfig] client.get_auto_commit_settings()  # Get auto commit settings (getAutoCommitSettings)
FeaturesInfo client.get_features_info()  # Get features info (getFeaturesInfo)
JwtSettings client.get_jwt_settings()  # Get the JWT Settings object (getJwtSettings)
LicenseUsageInfo client.get_license_usage_info()  # Get license usage info (getLicenseUsageInfo)
str client.get_mail_o_auth2_authorization_url()  # Redirect user to mail provider login page. 
str client.get_mail_processing_url()  # Get OAuth2 log in processing URL (getMailProcessingUrl)
RepositorySettings client.get_repository_settings()  # Get repository settings (getRepositorySettings)
RepositorySettingsInfo client.get_repository_settings_info()  # getRepositorySettingsInfo
SecuritySettings client.get_security_settings()  # Get the Security Settings object (getSecuritySettings)
SystemInfo client.get_system_info()  # Get system info (getSystemInfo)
None client.handle_mail_o_auth2_callback(code: str, state: str)  # handleMailOAuth2Callback
bool client.repository_settings_exists()  # Check repository settings exists (repositorySettingsExists)
AdminSettings client.save_admin_settings(admin_settings: AdminSettings)  # Creates or Updates the Administration Settings (saveAdminSettings)
Dict[str, AutoVersionCreateConfig] client.save_auto_commit_settings(request_body: Dict[str, AutoVersionCreateConfig])  # Creates or Updates the auto commit settings (saveAutoCommitSettings)
JwtPair client.save_jwt_settings(jwt_settings: JwtSettings)  # Update JWT Settings (saveJwtSettings)
RepositorySettings client.save_repository_settings(repository_settings: RepositorySettings)  # Creates or Updates the repository settings (saveRepositorySettings)
SecuritySettings client.save_security_settings(security_settings: SecuritySettings)  # Update Security Settings (saveSecuritySettings)
None client.send_test_mail(admin_settings: AdminSettings)  # Send test email (sendTestMail)
None client.send_test_sms(test_sms_request: TestSmsRequest)  # Send test sms (sendTestSms)
```


## auto_commit_settings_exists

```python
bool client.auto_commit_settings_exists()
```

**GET** `/api/admin/autoCommitSettings/exists`

Check auto commit settings exists (autoCommitSettingsExists)

Check whether the auto commit settings exists.   Available for users with 'TENANT_ADMIN' authority.

### Return type

**bool**


## check_repository_access

```python
None client.check_repository_access(repository_settings: RepositorySettings)
```

**POST** `/api/admin/repositorySettings/checkAccess`

Check repository access (checkRepositoryAccess)

Attempts to check repository access.   Available for users with 'TENANT_ADMIN' authority.


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **repository_settings** | **RepositorySettings** |  | |

### Return type

None (empty response body)


## check_updates

```python
UpdateMessage client.check_updates()
```

**GET** `/api/admin/updates`

Check for new Platform Releases (checkUpdates)

Check notifications about new platform releases.   Available for users with 'SYS_ADMIN' authority.

### Return type

**UpdateMessage**


## delete_auto_commit_settings

```python
None client.delete_auto_commit_settings()
```

**DELETE** `/api/admin/autoCommitSettings`

Delete auto commit settings (deleteAutoCommitSettings)

Deletes the auto commit settings.  Available for users with 'TENANT_ADMIN' authority.

### Return type

None (empty response body)


## delete_repository_settings

```python
None client.delete_repository_settings()
```

**DELETE** `/api/admin/repositorySettings`

Delete repository settings (deleteRepositorySettings)

Deletes the repository settings.  Available for users with 'TENANT_ADMIN' authority.

### Return type

None (empty response body)


## get_admin_settings

```python
AdminSettings client.get_admin_settings(key: str, system_by_default: Optional[bool] = None)
```

**GET** `/api/admin/settings/{key}`

Get the Administration Settings object using key (getAdminSettings)

Get the Administration Settings object using specified string key. Referencing non-existing key will cause an error.  Available for users with 'SYS_ADMIN' or 'TENANT_ADMIN' authority.  Security check is performed to verify that the user has 'READ' permission for the 'ADMIN_SETTINGS' (for 'SYS_ADMIN' authority) or 'WHITE_LABELING' (for 'TENANT_ADMIN' authority) resource.


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **key** | **str** | A string value of the key (e.g. 'general' or 'mail'). | |
| **system_by_default** | **bool** | Deprecated, not used. | [optional] [default to False] |

### Return type

**AdminSettings**


## get_auto_commit_settings

```python
Dict[str, AutoVersionCreateConfig] client.get_auto_commit_settings()
```

**GET** `/api/admin/autoCommitSettings`

Get auto commit settings (getAutoCommitSettings)

Get the auto commit settings object.   Available for users with 'TENANT_ADMIN' authority.

### Return type

**Dict[str, AutoVersionCreateConfig]**


## get_features_info

```python
FeaturesInfo client.get_features_info()
```

**GET** `/api/admin/featuresInfo`

Get features info (getFeaturesInfo)

Get information about enabled/disabled features.   Available for users with 'SYS_ADMIN' authority.

### Return type

**FeaturesInfo**


## get_jwt_settings

```python
JwtSettings client.get_jwt_settings()
```

**GET** `/api/admin/jwtSettings`

Get the JWT Settings object (getJwtSettings)

Get the JWT Settings object that contains JWT token policy, etc.   Available for users with 'SYS_ADMIN' authority.

### Return type

**JwtSettings**


## get_license_usage_info

```python
LicenseUsageInfo client.get_license_usage_info()
```

**GET** `/api/admin/licenseUsageInfo`

Get license usage info (getLicenseUsageInfo)

Get license usage info.   Available for users with 'SYS_ADMIN' authority.

### Return type

**LicenseUsageInfo**


## get_mail_o_auth2_authorization_url

```python
str client.get_mail_o_auth2_authorization_url()
```

**GET** `/api/admin/mail/oauth2/authorize`

Redirect user to mail provider login page. 

After user logged in and provided accessprovider sends authorization code to specified redirect uri.)

### Return type

**str**


## get_mail_processing_url

```python
str client.get_mail_processing_url()
```

**GET** `/api/admin/mail/oauth2/loginProcessingUrl`

Get OAuth2 log in processing URL (getMailProcessingUrl)

Returns the URL enclosed in double quotes. After successful authentication with OAuth2 provider and user consent for requested scope, it makes a redirect to this path so that the platform can do further log in processing and generating access tokens.   Available for users with 'SYS_ADMIN' authority.

### Return type

**str**


## get_repository_settings

```python
RepositorySettings client.get_repository_settings()
```

**GET** `/api/admin/repositorySettings`

Get repository settings (getRepositorySettings)

Get the repository settings object.   Available for users with 'TENANT_ADMIN' authority.

### Return type

**RepositorySettings**


## get_repository_settings_info

```python
RepositorySettingsInfo client.get_repository_settings_info()
```

**GET** `/api/admin/repositorySettings/info`

getRepositorySettingsInfo

### Return type

**RepositorySettingsInfo**


## get_security_settings

```python
SecuritySettings client.get_security_settings()
```

**GET** `/api/admin/securitySettings`

Get the Security Settings object (getSecuritySettings)

Get the Security Settings object that contains password policy, etc.  Available for users with 'SYS_ADMIN' authority.  Security check is performed to verify that the user has 'READ' permission for the 'ADMIN_SETTINGS' (for 'SYS_ADMIN' authority) or 'WHITE_LABELING' (for 'TENANT_ADMIN' authority) resource.

### Return type

**SecuritySettings**


## get_system_info

```python
SystemInfo client.get_system_info()
```

**GET** `/api/admin/systemInfo`

Get system info (getSystemInfo)

Get main information about system.   Available for users with 'SYS_ADMIN' authority.

### Return type

**SystemInfo**


## handle_mail_o_auth2_callback

```python
None client.handle_mail_o_auth2_callback(code: str, state: str)
```

**GET** `/api/admin/mail/oauth2/code`

handleMailOAuth2Callback


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **code** | **str** |  | |
| **state** | **str** |  | |

### Return type

None (empty response body)


## repository_settings_exists

```python
bool client.repository_settings_exists()
```

**GET** `/api/admin/repositorySettings/exists`

Check repository settings exists (repositorySettingsExists)

Check whether the repository settings exists.   Available for users with 'TENANT_ADMIN' authority.

### Return type

**bool**


## save_admin_settings

```python
AdminSettings client.save_admin_settings(admin_settings: AdminSettings)
```

**POST** `/api/admin/settings`

Creates or Updates the Administration Settings (saveAdminSettings)

Creates or Updates the Administration Settings. Platform generates random Administration Settings Id during settings creation. The Administration Settings Id will be present in the response. Specify the Administration Settings Id when you would like to update the Administration Settings. Referencing non-existing Administration Settings Id will cause an error.  Available for users with 'SYS_ADMIN' or 'TENANT_ADMIN' authority.  Security check is performed to verify that the user has 'WRITE' permission for the 'ADMIN_SETTINGS' (for 'SYS_ADMIN' authority) or 'WHITE_LABELING' (for 'TENANT_ADMIN' authority) resource.


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **admin_settings** | **AdminSettings** | A JSON value representing the Administration Settings. | |

### Return type

**AdminSettings**


## save_auto_commit_settings

```python
Dict[str, AutoVersionCreateConfig] client.save_auto_commit_settings(request_body: Dict[str, AutoVersionCreateConfig])
```

**POST** `/api/admin/autoCommitSettings`

Creates or Updates the auto commit settings (saveAutoCommitSettings)

Creates or Updates the auto commit settings object.   Available for users with 'TENANT_ADMIN' authority.


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **request_body** | **Dict[str, AutoVersionCreateConfig]** |  | |

### Return type

**Dict[str, AutoVersionCreateConfig]**


## save_jwt_settings

```python
JwtPair client.save_jwt_settings(jwt_settings: JwtSettings)
```

**POST** `/api/admin/jwtSettings`

Update JWT Settings (saveJwtSettings)

Updates the JWT Settings object that contains JWT token policy, etc. The tokenSigningKey field is a Base64 encoded string.  Available for users with 'SYS_ADMIN' authority.


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **jwt_settings** | **JwtSettings** |  | |

### Return type

**JwtPair**


## save_repository_settings

```python
RepositorySettings client.save_repository_settings(repository_settings: RepositorySettings)
```

**POST** `/api/admin/repositorySettings`

Creates or Updates the repository settings (saveRepositorySettings)

Creates or Updates the repository settings object.   Available for users with 'TENANT_ADMIN' authority.


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **repository_settings** | **RepositorySettings** |  | |

### Return type

**RepositorySettings**


## save_security_settings

```python
SecuritySettings client.save_security_settings(security_settings: SecuritySettings)
```

**POST** `/api/admin/securitySettings`

Update Security Settings (saveSecuritySettings)

Updates the Security Settings object that contains password policy, etc.  Available for users with 'SYS_ADMIN' authority.  Security check is performed to verify that the user has 'WRITE' permission for the 'ADMIN_SETTINGS' (for 'SYS_ADMIN' authority) or 'WHITE_LABELING' (for 'TENANT_ADMIN' authority) resource.


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **security_settings** | **SecuritySettings** |  | |

### Return type

**SecuritySettings**


## send_test_mail

```python
None client.send_test_mail(admin_settings: AdminSettings)
```

**POST** `/api/admin/settings/testMail`

Send test email (sendTestMail)

Attempts to send test email using Mail Settings provided as a parameter. Email is sent to the address specified in the profile of user who is performing the requestYou may change the 'To' email in the user profile of the System/Tenant Administrator.   Available for users with 'SYS_ADMIN' or 'TENANT_ADMIN' authority.  Security check is performed to verify that the user has 'READ' permission for the 'ADMIN_SETTINGS' (for 'SYS_ADMIN' authority) or 'WHITE_LABELING' (for 'TENANT_ADMIN' authority) resource.


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **admin_settings** | **AdminSettings** |  | |

### Return type

None (empty response body)


## send_test_sms

```python
None client.send_test_sms(test_sms_request: TestSmsRequest)
```

**POST** `/api/admin/settings/testSms`

Send test sms (sendTestSms)

Attempts to send test sms to the System Administrator User using SMS Settings and phone number provided as a parameters of the request.   Available for users with 'SYS_ADMIN' or 'TENANT_ADMIN' authority.  Security check is performed to verify that the user has 'READ' permission for the 'ADMIN_SETTINGS' (for 'SYS_ADMIN' authority) or 'WHITE_LABELING' (for 'TENANT_ADMIN' authority) resource.


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **test_sms_request** | **TestSmsRequest** |  | |

### Return type

None (empty response body)

