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


class Topic(object):

    def __init__(self, topicId=None, topicName=None, description=None, createTime=None, lastUpdateTime=None, topicStatus=None, subscriptionCount=None, messageLifeTimeInHours=None, topicConfig=None, own=None, authorizedPermission=None, tags=None):
        """
        :param topicId: (Optional) topic Id
        :param topicName: (Optional) topic名称
        :param description: (Optional) 描述
        :param createTime: (Optional) 创建时间
        :param lastUpdateTime: (Optional) 更新时间
        :param topicStatus: (Optional) topicStatus
        :param subscriptionCount: (Optional) 自己创建的订阅数
        :param messageLifeTimeInHours: (Optional) 消息生命周期时长小时
        :param topicConfig: (Optional) 配置信息
        :param own: (Optional) 是否是自己的topic
        :param authorizedPermission: (Optional) 被授权的权限[PUB,SUB,PUBSUB,READ_ONLY,ADMIN]
        :param tags: (Optional) 标签信息
        """

        self.topicId = topicId
        self.topicName = topicName
        self.description = description
        self.createTime = createTime
        self.lastUpdateTime = lastUpdateTime
        self.topicStatus = topicStatus
        self.subscriptionCount = subscriptionCount
        self.messageLifeTimeInHours = messageLifeTimeInHours
        self.topicConfig = topicConfig
        self.own = own
        self.authorizedPermission = authorizedPermission
        self.tags = tags