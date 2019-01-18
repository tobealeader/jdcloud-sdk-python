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


class SetHttpTypeRequest(JDCloudRequest):
    """
    设置http协议
    """

    def __init__(self, parameters, header=None, version="v1"):
        super(SetHttpTypeRequest, self).__init__(
            '/domain/{domain}/httpType', 'POST', header, version)
        self.parameters = parameters


class SetHttpTypeParameters(object):

    def __init__(self, domain, ):
        """
        :param domain: 用户域名
        """

        self.domain = domain
        self.httpType = None
        self.certificate = None
        self.rsaKey = None
        self.jumpType = None

    def setHttpType(self, httpType):
        """
        :param httpType: (Optional) http类型,只能为http或者https,默认为http.当设为https时,需要调用“设置通讯协议”接口上传证书和私钥
        """
        self.httpType = httpType

    def setCertificate(self, certificate):
        """
        :param certificate: (Optional) 用户证书,当Type为https时必须设置
        """
        self.certificate = certificate

    def setRsaKey(self, rsaKey):
        """
        :param rsaKey: (Optional) 证书私钥
        """
        self.rsaKey = rsaKey

    def setJumpType(self, jumpType):
        """
        :param jumpType: (Optional) 有三种类型：default、http、https
        """
        self.jumpType = jumpType
