import re

import config
import models


def get_blacklist_urls() -> list[str]:
    return [i.value for i in models.BlacklistUrl.get_docs()]


def allowed(url: str) -> bool:
    if url in get_blacklist_urls():
        return False

    for regexp in config.BLACKLIST_URL_REGEXPS:
        if re.search(regexp, url):
            return False

    return True
