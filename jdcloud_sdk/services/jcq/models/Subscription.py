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


class Subscription(object):

    def __init__(self, consumerGroupId=None, endPoint=None, messageInvisibleTimeInSeconds=None, subscriptionType=None, tags=None, dlqEnable=None, maxRetryTimes=None, createTime=None, lastUpdateTime=None, consumerNumbers=None):
        """
        :param consumerGroupId: (Optional) consumerGroupId
        :param endPoint: (Optional) endPoint
        :param messageInvisibleTimeInSeconds: (Optional) messageInvisibleTimeInSeconds
        :param subscriptionType: (Optional) subscriptionType
        :param tags: (Optional) tags
        :param dlqEnable: (Optional) 是否开启死信队列
        :param maxRetryTimes: (Optional) 最大重试次数
        :param createTime: (Optional) 创建时间
        :param lastUpdateTime: (Optional) 最后更新时间
        :param consumerNumbers: (Optional) 在线consumer个数
        """

        self.consumerGroupId = consumerGroupId
        self.endPoint = endPoint
        self.messageInvisibleTimeInSeconds = messageInvisibleTimeInSeconds
        self.subscriptionType = subscriptionType
        self.tags = tags
        self.dlqEnable = dlqEnable
        self.maxRetryTimes = maxRetryTimes
        self.createTime = createTime
        self.lastUpdateTime = lastUpdateTime
        self.consumerNumbers = consumerNumbers
