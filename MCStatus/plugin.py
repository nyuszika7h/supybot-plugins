# vim: fileencoding=utf-8 ts=4 sw=4 sts=4 et tw=79
#
# Copyright (c) 2012-2013, nyuszika7h <nyuszika7h@cadoth.net>
#
# This software is provided 'as-is', without any express or implied
# warranty.  In no event will the authors be held liable for any damages
# arising from the use of this software.
#
# Permission is granted to anyone to use this software for any purpose,
# including commercial applications, and to alter it and redistribute it
# freely, subject to the following restrictions:
#
#   1. The origin of this software must not be misrepresented; you must not
#      claim that you wrote the original software. If you use this software
#      in a product, an acknowledgment in the product documentation would be
#      appreciated but is not required.
#
#   2. Altered source versions must be plainly marked as such, and must not be
#      misrepresented as being the original software.
#
#   3. This notice may not be removed or altered from any source distribution.

# Standard library imports
import json
import urllib2

# Supybot imports
import supybot.utils as utils
from supybot.commands import *
import supybot.plugins as plugins
import supybot.ircutils as ircutils
import supybot.callbacks as callbacks
from supybot.i18n import PluginInternationalization, internationalizeDocstring

_ = PluginInternationalization('MCStatus')

@internationalizeDocstring
class MCStatus(callbacks.Plugin):
    """This plugin provides a command to show the status of the Mojang servers.
    The output format is customizable via configuration variables."""

    def __init__(self, irc):
        self.__parent = super(MCStatus, self)
        self.__parent.__init__(irc)

    def mcstatus(self, irc, msg, args):
        """takes no arguments

        Shows the status of the Mojang servers.
        """
        prefix = self.registryValue('prefix')
        suffix = self.registryValue('suffix')

        separator = self.registryValue('separator')

        svprefix = self.registryValue('service.prefix')
        svsuffix = self.registryValue('service.suffix')

        stonline = self.registryValue('status.online')
        stoffline = self.registryValue('status.offline')


        json_data = urllib2.urlopen(self.registryValue('statusURL')).read()
        data = json.loads(json_data)
        services = []

        for pair in data:
            service, status = pair.keys()[0], pair.values()[0]
            services.append('%s%s%s%s' % (svprefix, service, svsuffix,
                                          stonline if status == 'green' else \
                                          stoffline))

        irc.reply('%s%s%s' % (prefix, separator.join(services), suffix))
    mcstatus = wrap(mcstatus)

Class = MCStatus
