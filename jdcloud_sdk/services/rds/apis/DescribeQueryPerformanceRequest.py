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


class DescribeQueryPerformanceRequest(JDCloudRequest):
    """
    根据用户定义的查询条件，获取SQL执行的性能统计信息，例如慢SQL等。用户可以根据这些信息查找与SQL执行相关的性能瓶颈，并进行优化。<br>- 仅支持SQL Server
    """

    def __init__(self, parameters, header=None, version="v1"):
        super(DescribeQueryPerformanceRequest, self).__init__(
            '/regions/{regionId}/instances/{instanceId}/performance:describeQueryPerformance', 'POST', header, version)
        self.parameters = parameters


class DescribeQueryPerformanceParameters(object):

    def __init__(self, regionId, instanceId, queryType, ):
        """
        :param regionId: 地域代码，取值范围参见[《各地域及可用区对照表》](../Enum-Definitions/Regions-AZ.md)
        :param instanceId: RDS 实例ID，唯一标识一个RDS实例
        :param queryType: 查询类型，不同的查询类型按照相应的字段从高到低返回结果。<br>支持如下类型：<br>ExecutionCount：执行次数<br>LastRows：上次返回行数<br>ElapsedTime：平均执行时间<br>CPUTime：平均CPU时间<br>LogicalReads：平均逻辑读<br>LogicalWrites：平均逻辑写<br>PhysicalReads：平均物理读<br>
        """

        self.regionId = regionId
        self.instanceId = instanceId
        self.queryType = queryType
        self.threshold = None
        self.pageNumber = None
        self.pageSize = None

    def setThreshold(self, threshold):
        """
        :param threshold: (Optional) 只返回查询条件大于等于threshold的记录，默认为0
        """
        self.threshold = threshold

    def setPageNumber(self, pageNumber):
        """
        :param pageNumber: (Optional) 显示数据的页码，默认为1，取值范围：[-1,1000]。pageNumber为-1时，返回所有数据页码；超过总页数时，显示最后一页。
        """
        self.pageNumber = pageNumber

    def setPageSize(self, pageSize):
        """
        :param pageSize: (Optional) 每页显示的数据条数，默认为50，取值范围：[1,100]，只能为10的倍数，用于查询列表的接口
        """
        self.pageSize = pageSize

