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


class Product(object):

    def __init__(self, id=None, name=None, url=None, parentNavigationId=None, navigationId=None, createTime=None, updateTime=None, lang=None, txtVoList=None):
        """
        :param id: (Optional) 主键id
        :param name: (Optional) 名称
        :param url: (Optional) url
        :param parentNavigationId: (Optional) 父导航id
        :param navigationId: (Optional) 导航id
        :param createTime: (Optional) 修改时间
        :param updateTime: (Optional) 修改时间
        :param lang: (Optional) 语言：中文cn；英文en
        :param txtVoList: (Optional) 产品数据
        """

        self.id = id
        self.name = name
        self.url = url
        self.parentNavigationId = parentNavigationId
        self.navigationId = navigationId
        self.createTime = createTime
        self.updateTime = updateTime
        self.lang = lang
        self.txtVoList = txtVoList
