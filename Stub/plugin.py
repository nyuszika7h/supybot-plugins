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

# Supybot imports
from supybot import callbacks
from supybot.commands import *

try:
    from supybot import i18n
    _ = i18n.PluginInternationalization('Stub')
except ImportError:
    # Placeholder that allows to run the plugin on a bot without the
    # i18n module.

    i18n = None
    _ = lambda x: x


class Stub(callbacks.Plugin):
    """
    Plugin description
    """

    def __init__(self, irc):
        self.__parent = super(Stub, self)
        self.__parent.__init__(irc)


Class = Stub
