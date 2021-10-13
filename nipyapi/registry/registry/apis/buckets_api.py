# coding: utf-8

"""
    Apache NiFi Registry REST API

    The REST API provides an interface to a registry with operations for saving, versioning, reading NiFi flows and components.

    OpenAPI spec version: 0.8.0
    Contact: dev@nifi.apache.org
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import sys
import os
import re

# python 2 and python 3 compatibility library
from six import iteritems

from ..configuration import Configuration
from ..api_client import ApiClient


class BucketsApi(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        config = Configuration()
        if api_client:
            self.api_client = api_client
        else:
            if not config.api_client:
                config.api_client = ApiClient()
            self.api_client = config.api_client

    def create_bucket(self, body, **kwargs):
        """
        Create bucket
        
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.create_bucket(body, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param Bucket body: The bucket to create (required)
        :return: Bucket
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.create_bucket_with_http_info(body, **kwargs)
        else:
            (data) = self.create_bucket_with_http_info(body, **kwargs)
            return data

    def create_bucket_with_http_info(self, body, **kwargs):
        """
        Create bucket
        
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.create_bucket_with_http_info(body, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param Bucket body: The bucket to create (required)
        :return: Bucket
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_bucket" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params) or (params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `create_bucket`")


        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = ['tokenAuth', 'Authorization']

        return self.api_client.call_api('/buckets', 'POST',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='Bucket',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def delete_bucket(self, version, bucket_id, **kwargs):
        """
        Delete bucket
        Deletes the bucket with the given id, along with all objects stored in the bucket
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.delete_bucket(version, bucket_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str version: The version is used to verify the client is working with the latest version of the entity. (required)
        :param str bucket_id: The bucket identifier (required)
        :param str client_id: If the client id is not specified, new one will be generated. This value (whether specified or generated) is included in the response.
        :return: Bucket
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.delete_bucket_with_http_info(version, bucket_id, **kwargs)
        else:
            (data) = self.delete_bucket_with_http_info(version, bucket_id, **kwargs)
            return data

    def delete_bucket_with_http_info(self, version, bucket_id, **kwargs):
        """
        Delete bucket
        Deletes the bucket with the given id, along with all objects stored in the bucket
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.delete_bucket_with_http_info(version, bucket_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str version: The version is used to verify the client is working with the latest version of the entity. (required)
        :param str bucket_id: The bucket identifier (required)
        :param str client_id: If the client id is not specified, new one will be generated. This value (whether specified or generated) is included in the response.
        :return: Bucket
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['version', 'bucket_id', 'client_id']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_bucket" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'version' is set
        if ('version' not in params) or (params['version'] is None):
            raise ValueError("Missing the required parameter `version` when calling `delete_bucket`")
        # verify the required parameter 'bucket_id' is set
        if ('bucket_id' not in params) or (params['bucket_id'] is None):
            raise ValueError("Missing the required parameter `bucket_id` when calling `delete_bucket`")


        collection_formats = {}

        path_params = {}
        if 'bucket_id' in params:
            path_params['bucketId'] = params['bucket_id']

        query_params = []
        if 'version' in params:
            query_params.append(('version', params['version']))
        if 'client_id' in params:
            query_params.append(('clientId', params['client_id']))

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['*/*'])

        # Authentication setting
        auth_settings = ['tokenAuth', 'Authorization']

        return self.api_client.call_api('/buckets/{bucketId}', 'DELETE',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='Bucket',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def get_available_bucket_fields(self, **kwargs):
        """
        Get bucket fields
        Retrieves bucket field names for searching or sorting on buckets.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_available_bucket_fields(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :return: Fields
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.get_available_bucket_fields_with_http_info(**kwargs)
        else:
            (data) = self.get_available_bucket_fields_with_http_info(**kwargs)
            return data

    def get_available_bucket_fields_with_http_info(self, **kwargs):
        """
        Get bucket fields
        Retrieves bucket field names for searching or sorting on buckets.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_available_bucket_fields_with_http_info(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :return: Fields
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = []
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_available_bucket_fields" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['*/*'])

        # Authentication setting
        auth_settings = ['tokenAuth', 'Authorization']

        return self.api_client.call_api('/buckets/fields', 'GET',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='Fields',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def get_bucket(self, bucket_id, **kwargs):
        """
        Get bucket
        Gets the bucket with the given id.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_bucket(bucket_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str bucket_id: The bucket identifier (required)
        :return: Bucket
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.get_bucket_with_http_info(bucket_id, **kwargs)
        else:
            (data) = self.get_bucket_with_http_info(bucket_id, **kwargs)
            return data

    def get_bucket_with_http_info(self, bucket_id, **kwargs):
        """
        Get bucket
        Gets the bucket with the given id.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_bucket_with_http_info(bucket_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str bucket_id: The bucket identifier (required)
        :return: Bucket
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['bucket_id']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_bucket" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'bucket_id' is set
        if ('bucket_id' not in params) or (params['bucket_id'] is None):
            raise ValueError("Missing the required parameter `bucket_id` when calling `get_bucket`")


        collection_formats = {}

        path_params = {}
        if 'bucket_id' in params:
            path_params['bucketId'] = params['bucket_id']

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['*/*'])

        # Authentication setting
        auth_settings = ['tokenAuth', 'Authorization']

        return self.api_client.call_api('/buckets/{bucketId}', 'GET',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='Bucket',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def get_buckets(self, **kwargs):
        """
        Get all buckets
        The returned list will include only buckets for which the user is authorized.If the user is not authorized for any buckets, this returns an empty list.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_buckets(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :return: list[Bucket]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.get_buckets_with_http_info(**kwargs)
        else:
            (data) = self.get_buckets_with_http_info(**kwargs)
            return data

    def get_buckets_with_http_info(self, **kwargs):
        """
        Get all buckets
        The returned list will include only buckets for which the user is authorized.If the user is not authorized for any buckets, this returns an empty list.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_buckets_with_http_info(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :return: list[Bucket]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = []
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_buckets" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['*/*'])

        # Authentication setting
        auth_settings = ['tokenAuth', 'Authorization']

        return self.api_client.call_api('/buckets', 'GET',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='list[Bucket]',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def update_bucket(self, bucket_id, body, **kwargs):
        """
        Update bucket
        Updates the bucket with the given id.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.update_bucket(bucket_id, body, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str bucket_id: The bucket identifier (required)
        :param Bucket body: The updated bucket (required)
        :return: Bucket
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.update_bucket_with_http_info(bucket_id, body, **kwargs)
        else:
            (data) = self.update_bucket_with_http_info(bucket_id, body, **kwargs)
            return data

    def update_bucket_with_http_info(self, bucket_id, body, **kwargs):
        """
        Update bucket
        Updates the bucket with the given id.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.update_bucket_with_http_info(bucket_id, body, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str bucket_id: The bucket identifier (required)
        :param Bucket body: The updated bucket (required)
        :return: Bucket
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['bucket_id', 'body']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_bucket" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'bucket_id' is set
        if ('bucket_id' not in params) or (params['bucket_id'] is None):
            raise ValueError("Missing the required parameter `bucket_id` when calling `update_bucket`")
        # verify the required parameter 'body' is set
        if ('body' not in params) or (params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `update_bucket`")


        collection_formats = {}

        path_params = {}
        if 'bucket_id' in params:
            path_params['bucketId'] = params['bucket_id']

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = ['tokenAuth', 'Authorization']

        return self.api_client.call_api('/buckets/{bucketId}', 'PUT',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='Bucket',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)
