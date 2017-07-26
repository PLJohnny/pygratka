#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import logging
from gratka.category import get_category
from gratka.offer import get_offer_information

log = logging.getLogger(__file__)

SCRAPE_LIMIT = os.environ.get('SCRAPE_LIMIT', None)

if __name__ == '__main__':
    input_dict = {'ga': 4}

    if os.getenv('PRICE_TO'):
        input_dict['maximal_price'] = os.getenv('PRICE_TO')

    parsed_category = get_category("mieszkania", "do-wynajecia", "pomorskie", "gda", **input_dict)

    log.info("Offers in that category - {0}".format(len(parsed_category)))

    if SCRAPE_LIMIT:
        parsed_category = parsed_category[:int(SCRAPE_LIMIT)]
        log.info("Scraping limit - {0}".format(len(parsed_category)))

    for offer in parsed_category:
        log.info("Scraping offer - {0}".format(offer['detail_url']))
        offer_detail = get_offer_information(offer['detail_url'], context=offer)
        log.info("Scraped offer - {0}".format(offer_detail))
