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


class JmrPlanViewModel(object):

    def __init__(self, planId=None, planName=None, planType=None, planStatus=None, failurePolicy=None, createTime=None, modifyTime=None, dataCenter=None, jobGroup=None, jobTrigger=None, cronExpression=None, isSync=None, description=None, jobIds=None, clusterId=None, clusterName=None, orderBy=None):
        """
        :param planId: (Optional) 任务调度id
        :param planName: (Optional) 
        :param planType: (Optional) 
        :param planStatus: (Optional) 
        :param failurePolicy: (Optional) 任务调度失败时采用的策略
        :param createTime: (Optional) 创建时间
        :param modifyTime: (Optional) 修改时间
        :param dataCenter: (Optional) 数据中心，即regionId
        :param jobGroup: (Optional) 
        :param jobTrigger: (Optional) 触发器
        :param cronExpression: (Optional) formatt后的时间
        :param isSync: (Optional) 
        :param description: (Optional) 
        :param jobIds: (Optional) 
        :param clusterId: (Optional) 
        :param clusterName: (Optional) 
        :param orderBy: (Optional) 
        """

        self.planId = planId
        self.planName = planName
        self.planType = planType
        self.planStatus = planStatus
        self.failurePolicy = failurePolicy
        self.createTime = createTime
        self.modifyTime = modifyTime
        self.dataCenter = dataCenter
        self.jobGroup = jobGroup
        self.jobTrigger = jobTrigger
        self.cronExpression = cronExpression
        self.isSync = isSync
        self.description = description
        self.jobIds = jobIds
        self.clusterId = clusterId
        self.clusterName = clusterName
        self.orderBy = orderBy