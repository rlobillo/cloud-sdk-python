# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.

import unittest

from openstack.tests.functional import base


@unittest.skipUnless(base.service_exists(service_type="metering"),
                     "Metering service does not exist")
class TestResource(base.BaseFunctionalTest):

    def test_list(self):
        ids = [o.resource_id for o in self.conn.telemetry.resources()]
        self.assertNotEqual(0, len(ids))
