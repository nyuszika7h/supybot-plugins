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

"""
This plugin provides a command to show the status of the Mojang servers.
The output format is customizable via configuration variables.
"""

import supybot
import supybot.world as world

# Use this for the version of this plugin.  You may wish to put a CVS keyword
# in here if you're keeping the plugin in CVS or some similar system.
__version__ = '1.0.2'

# Replace this with an appropriate author or supybot.Author instance.
__author__ = supybot.Author('nyuszika7h', 'nyuszika7h',
                            'nyuszika7h@cadoth.net')

# This is a dictionary mapping supybot.Author instances to lists of
# contributions.
__contributors__ = {}

# This is a URL where the most recent plugin package can be downloaded.
__url__ = ''

import config
import plugin
reload(plugin) # In case we're being reloaded.
# Add more reloads here if you add third-party modules and want them to be
# reloaded when this plugin is reloaded.  Don't forget to import them as well!

if world.testing:
    import test

Class = plugin.Class
configure = config.configure
