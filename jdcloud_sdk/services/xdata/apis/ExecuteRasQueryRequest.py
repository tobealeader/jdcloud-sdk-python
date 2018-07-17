# coding=utf8

# Copyright 2018 JDCLOUD.COM
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http:#www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
# NOTE: This class is auto generated by the jdcloud code generator program.

from jdcloud_sdk.core.jdcloudrequest import JDCloudRequest


class ExecuteRasQueryRequest(JDCloudRequest):
    """
    执行Spark SQL
    """

    def __init__(self, parameters, header=None, version="v1"):
        super(ExecuteRasQueryRequest, self).__init__(
            '/regions/{regionId}/dwQuery:executeRasQuery', 'POST', header, version)
        self.parameters = parameters


class ExecuteRasQueryParameters(object):

    def __init__(self, regionId, sql, userName, instanceName, ):
        """
        :param regionId: 地域ID
        :param sql: sql脚本
        :param userName: 用户名称
        :param instanceName: 实例名称
        """

        self.regionId = regionId
        self.databaseName = None
        self.sql = sql
        self.userName = userName
        self.queueName = None
        self.source = None
        self.callBackURL = None
        self.instanceName = instanceName
        self.instanceOwnerName = None
        self.isExplain = None

    def setDatabaseName(self, databaseName):
        """
        :param databaseName: (Optional) 数据库名称
        """
        self.databaseName = databaseName

    def setQueueName(self, queueName):
        """
        :param queueName: (Optional) 队列名称
        """
        self.queueName = queueName

    def setSource(self, source):
        """
        :param source: (Optional) 资源名称
        """
        self.source = source

    def setCallBackURL(self, callBackURL):
        """
        :param callBackURL: (Optional) 回调地址名称
        """
        self.callBackURL = callBackURL

    def setInstanceOwnerName(self, instanceOwnerName):
        """
        :param instanceOwnerName: (Optional) 实例拥有者名称
        """
        self.instanceOwnerName = instanceOwnerName

    def setIsExplain(self, isExplain):
        """
        :param isExplain: (Optional) 是否需要解释
        """
        self.isExplain = isExplain
