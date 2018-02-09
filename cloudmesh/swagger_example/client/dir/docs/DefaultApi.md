# swagger_client.DefaultApi

All URIs are relative to *http://localhost:8080/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**dir_get**](DefaultApi.md#dir_get) | **GET** /dir | 
[**get_file_by_id**](DefaultApi.md#get_file_by_id) | **GET** /dir/{id} | 


# **dir_get**
> LOF dir_get()



Returns list of files under root directory

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()

try:
    api_response = api_instance.dir_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->dir_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**LOF**](LOF.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_file_by_id**
> LOF get_file_by_id(id)



Returns list of files under given directory

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
id = 'id_example' # str | ID of directory to fetch

try:
    api_response = api_instance.get_file_by_id(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_file_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of directory to fetch | 

### Return type

[**LOF**](LOF.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

