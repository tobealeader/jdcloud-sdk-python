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


class AddLiveStreamAppTranscodeRequest(JDCloudRequest):
    """
    添加APP转码配置
    """

    def __init__(self, parameters, header=None, version="v1"):
        super(AddLiveStreamAppTranscodeRequest, self).__init__(
            '/transcodeApps:config', 'POST', header, version)
        self.parameters = parameters


class AddLiveStreamAppTranscodeParameters(object):

    def __init__(self, publishDomain, template, appName):
        """
        :param publishDomain: 直播的推流域名
        :param template: 转码模版
        :param appName: 直播流所属应用名称
        """

        self.publishDomain = publishDomain
        self.template = template
        self.appName = appName

