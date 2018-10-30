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


class GetUserViewIPRequest(JDCloudRequest):
    """
    查询域名的自定义解析线路的IP段
    """

    def __init__(self, parameters, header=None, version="v1"):
        super(GetUserViewIPRequest, self).__init__(
            '/regions/{regionId}/userview/getUserViewIP', 'GET', header, version)
        self.parameters = parameters


class GetUserViewIPParameters(object):

    def __init__(self, regionId, domainId, viewId, pageNumber, pageSize):
        """
        :param regionId: 地域ID
        :param domainId: 主域名ID
        :param viewId: 自定义线路ID
        :param pageNumber: 分页参数，页的序号, 默认为1
        :param pageSize: 分页参数，每页含有的结果的数目，默认为10
        """

        self.regionId = regionId
        self.domainId = domainId
        self.viewId = viewId
        self.viewName = None
        self.pageNumber = pageNumber
        self.pageSize = pageSize

    def setViewName(self, viewName):
        """
        :param viewName: (Optional) 自定义线路名称, 最多64个字符
        """
        self.viewName = viewName
