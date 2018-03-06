from pycoin_grs.version import version

try:
    import urllib2 as request
    from urllib import urlencode  # noqa
except ImportError:
    from urllib import request
    from urllib.parse import urlencode  # noqa


PYCOIN_GRS_AGENT = 'pycoin_grs/%s' % version


def urlopen(url):
    req = request.Request(url)
    req.add_header('User-agent', PYCOIN_GRS_AGENT)
    return request.urlopen(req)
