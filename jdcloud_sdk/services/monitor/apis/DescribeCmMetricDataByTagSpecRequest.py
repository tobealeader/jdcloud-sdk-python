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


class DescribeCmMetricDataByTagSpecRequest(JDCloudRequest):
    """
    查询自定义监控项数据
    """

    def __init__(self, parameters, header=None, version="v1"):
        super(DescribeCmMetricDataByTagSpecRequest, self).__init__(
            '/regions/{regionId}/cm/namespaces/{namespace}/metrics/{metric}/metricData', 'GET', header, version)
        self.parameters = parameters


class DescribeCmMetricDataByTagSpecParameters(object):

    def __init__(self, regionId, namespace, metric, ):
        """
        :param regionId: 地域 Id
        :param namespace: namespace
        :param metric: 监控项英文标识(id)，监控项名称
        """

        self.regionId = regionId
        self.namespace = namespace
        self.metric = metric
        self.aggrType = None
        self.downSampleType = None
        self.startTime = None
        self.endTime = None
        self.timeInterval = None
        self.tags = None
        self.groupBy = None

    def setAggrType(self, aggrType):
        """
        :param aggrType: (Optional) 指标聚合方式，每个指标都有默认的聚合方式， 可选值包括：sum,avg.max.min；多个对象的数据如何合并(resourceId -> cluster)
        """
        self.aggrType = aggrType

    def setDownSampleType(self, downSampleType):
        """
        :param downSampleType: (Optional) 指标采样方式，默认avg， 可选值包括：sum,avg,max,min,last；同一对象的数据，在改变时间点粒度时如何合并(1m->20m)
        """
        self.downSampleType = downSampleType

    def setStartTime(self, startTime):
        """
        :param startTime: (Optional) 查询时间范围的开始时间， UTC时间，格式：yyyy-MM-dd'T'HH:mm:ssZ（默认为当前时间，早于30d时，将被重置为30d）
        """
        self.startTime = startTime

    def setEndTime(self, endTime):
        """
        :param endTime: (Optional) 查询时间范围的结束时间， UTC时间，格式：2016-12- yyyy-MM-dd'T'HH:mm:ssZ（为空时，将由startTime与timeInterval计算得出）
        """
        self.endTime = endTime

    def setTimeInterval(self, timeInterval):
        """
        :param timeInterval: (Optional) 时间间隔：1h，6h，12h，1d，3d，7d，14d，固定时间间隔，timeInterval 与 endTime 至少填一项
        """
        self.timeInterval = timeInterval

    def setTags(self, tags):
        """
        :param tags: (Optional) 自定义标签
        """
        self.tags = tags

    def setGroupBy(self, groupBy):
        """
        :param groupBy: (Optional) 是否对查询的tags分组
        """
        self.groupBy = groupBy
