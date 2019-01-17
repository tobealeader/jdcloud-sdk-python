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


class ReverseDeploymentInfo(object):

    def __init__(self, name=None, description=None, version=None, readOnly=None, resources=None):
        """
        :param name: (Optional) 模板名称
        :param description: (Optional) 描述
        :param version: (Optional) 版本
        :param readOnly: (Optional) 是否只读 0：否 1：是
        :param resources: (Optional) 
        """

        self.name = name
        self.description = description
        self.version = version
        self.readOnly = readOnly
        self.resources = resources
