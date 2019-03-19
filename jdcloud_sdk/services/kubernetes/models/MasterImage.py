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


class MasterImage(object):

    def __init__(self, code=None, imageId=None, mainVersion=None, innerVersion=None, isDefault=None, visibility=None, defaultNodeImageCode=None, nodeImages=None):
        """
        :param code: (Optional) 镜像编码
        :param imageId: (Optional) 虚机镜像id
        :param mainVersion: (Optional) 主版本号
        :param innerVersion: (Optional) 内部版本号
        :param isDefault: (Optional) 是否默认镜像
        :param visibility: (Optional) 可见度:0：所有人可见；1：授权用户可见；2：只有白名单用户可见
        :param defaultNodeImageCode: (Optional) 默认ndoe镜像编码
        :param nodeImages: (Optional) node 节点的配置
        """

        self.code = code
        self.imageId = imageId
        self.mainVersion = mainVersion
        self.innerVersion = innerVersion
        self.isDefault = isDefault
        self.visibility = visibility
        self.defaultNodeImageCode = defaultNodeImageCode
        self.nodeImages = nodeImages