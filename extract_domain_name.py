import re


def domain_name(url):
    return re.sub(
        '\..*$',
        '',
        url.replace("https://", "").replace("http://", "").replace("www.", "")
    )
