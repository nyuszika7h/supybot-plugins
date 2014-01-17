# Copyright 2014, nyuszika7h <nyuszika7h@cadoth.net>
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

"""
Plugin description
"""

# Standard library imports
from imp import reload

# Supybot imports
import supybot
from supybot import world

# Local imports
from . import config, plugin

__version__ = '1.0.0'

__author__ = supybot.Author('nyuszika7h', 'nyuszika7h',
                            'nyuszika7h@cadoth.net')

__contributors__ = {}

__url__ = ''

# In case we're being reloaded.
reload(config)
reload(plugin)

if world.testing:
    from . import test

Class = plugin.Class
configure = config.configure
