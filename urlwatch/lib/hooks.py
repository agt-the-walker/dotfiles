#
# Example hooks file for urlwatch
#
# Copyright (c) 2008-2015 Thomas Perl <thp.io/about>
# All rights reserved.
# 
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions
# are met:
# 1. Redistributions of source code must retain the above copyright
#    notice, this list of conditions and the following disclaimer.
# 2. Redistributions in binary form must reproduce the above copyright
#    notice, this list of conditions and the following disclaimer in the
#    documentation and/or other materials provided with the distribution.
# 3. The name of the author may not be used to endorse or promote products
#    derived from this software without specific prior written permission.
# 
# THIS SOFTWARE IS PROVIDED BY THE AUTHOR ``AS IS'' AND ANY EXPRESS OR
# IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES
# OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED.
# IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR ANY DIRECT, INDIRECT,
# INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT
# NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
# DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
# THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF
# THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
#


# You can decide which filter you want to apply using the "url"
# parameter and you can use the "re" module to search for the
# content that you want to filter, so the noise is removed.


# Needed for regular expression substitutions
import re

# Additional modules installed with urlwatch
from urlwatch import ical2txt
from urlwatch import html2txt


def filter(url, data):
    if url == 'http://brainking.com/en/Profile?u=78167&p=2':
        m = re.search("Agt the Walker's turn in \\d+ games?", data)
        return m.group(0) if m else 'N/A'
    elif url == 'http://salsaddictos.ch/agenda/':
        data = re.sub('\<!-- .*? --\>', '', data)
        data = re.sub('\?ver=\w+', '', data)
        data = re.sub('/e-\d{6}\.js', '', data)
        return re.sub('<body class=".*?">', '<body>', data)
    elif url == 'http://www.planetasalsa.ch/gallery3/index.php/':
        return re.sub('Betrachtungen: \d+', '', data)

    # In some cases, it might be necessary to decode the data from
    # bytes to unicode. We don't always know the encoding of the
    # remote file, so pick the right encoding (maybe depending on
    # the remote URL), like so:

    if type(data) == bytes:
        data = data.decode('utf-8')

    # The next line is optional - if the filter function returns
    # None (or no value at all), the input data will be taken as
    # the result -> None as return value means "don't filter".
    return data
