# coding=utf8

# Copyright 2018-2025 JDCLOUD.COM
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http:#www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import unittest
from jdcloud_sdk.core.credential import Credential
from jdcloud_sdk.core.config import Config
from jdcloud_sdk.core.const import SCHEME_HTTP
from jdcloud_sdk.services.oss.client.OssClient import OssClient
from jdcloud_sdk.services.oss.apis.HeadBucketRequest import *


class OssTest(unittest.TestCase):

    # without regionId
    def testHeadBucket(self):
        access_key = 'ak'
        secret_key = 'sk'
        credential = Credential(access_key, secret_key)
        client = OssClient(credential)

        params = HeadBucketParameters('cn-north-1', 'bucke01')
        request = HeadBucketRequest(params)
        resp = client.send(request)
        self.assertTrue(resp.error is None)
        print resp.requestId

