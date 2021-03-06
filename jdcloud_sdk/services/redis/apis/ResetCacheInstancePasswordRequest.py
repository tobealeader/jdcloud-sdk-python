# coding=utf8

# Copyright 2018 JDCLOUD.COM
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
# NOTE: This class is auto generated by the jdcloud code generator program.

from jdcloud_sdk.core.jdcloudrequest import JDCloudRequest


class ResetCacheInstancePasswordRequest(JDCloudRequest):
    """
    重置缓存Redis实例密码，支持免密操作
    """

    def __init__(self, parameters, header=None, version="v1"):
        super(ResetCacheInstancePasswordRequest, self).__init__(
            '/regions/{regionId}/cacheInstance/{cacheInstanceId}:resetCacheInstancePassword', 'POST', header, version)
        self.parameters = parameters


class ResetCacheInstancePasswordParameters(object):

    def __init__(self, regionId, cacheInstanceId, ):
        """
        :param regionId: 缓存Redis实例所在区域的Region ID。目前缓存Redis有华北、华南、华东区域，对应Region ID为cn-north-1、cn-south-1、cn-east-2
        :param cacheInstanceId: 缓存Redis实例ID，是访问实例的唯一标识。
        """

        self.regionId = regionId
        self.cacheInstanceId = cacheInstanceId
        self.password = None

    def setPassword(self, password):
        """
        :param password: (Optional) 密码，为空即为免密，包含且只支持字母及数字，不少于8字符不超过16字符
        """
        self.password = password

