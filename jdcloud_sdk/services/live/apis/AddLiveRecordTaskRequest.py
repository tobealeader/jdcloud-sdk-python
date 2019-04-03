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


class AddLiveRecordTaskRequest(JDCloudRequest):
    """
    添加打点录制任务
- 您可以调用此接口精确提取已录制的文件中所需要的部分

    """

    def __init__(self, parameters, header=None, version="v1"):
        super(AddLiveRecordTaskRequest, self).__init__(
            '/records/{publishDomain}/appNames/{appName}/streamNames/{streamName}/task', 'POST', header, version)
        self.parameters = parameters


class AddLiveRecordTaskParameters(object):

    def __init__(self, publishDomain, appName, streamName, recordTimes, saveBucket, saveEndpoint, recordFileType, ):
        """
        :param publishDomain: 推流域名
        :param appName: 应用名称
        :param streamName: 流名称
        :param recordTimes: 录制时间集合 - 最大支持10段,多段合并成一个文件 - 多段时间跨度最小不能小于10s - 多段时间跨度最大不能超过8小时
        :param saveBucket: 存储桶
        :param saveEndpoint: 存储地址
        :param recordFileType: 录制文件类型:
- 取值: ts,flv,mp4 (多种类型之前用;隔开)
- 不区分大小写

        """

        self.publishDomain = publishDomain
        self.appName = appName
        self.streamName = streamName
        self.recordTimes = recordTimes
        self.saveBucket = saveBucket
        self.saveEndpoint = saveEndpoint
        self.recordFileType = recordFileType
        self.saveObject = None

    def setSaveObject(self, saveObject):
        """
        :param saveObject: (Optional) 录制文件存储路径:
- 默认地址: record/{Date}/{ServerId}/{AppName}/{StreamName}/{StartTime}_{EndTime}.{format}

        """
        self.saveObject = saveObject

