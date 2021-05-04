#!/usr/bin/env python3
__version__ = "0.1.0"

import argparse
import logzero
import settings
import xml.etree.ElementTree as etree

class Main:
    def __init__(self):
        logzero.logfile(
            settings.settings_dict['logfile'],
            loglevel=20,
            maxBytes=1e6,
            backupCount=3
        )
        self.logger = logzero.logger

    def main(self, args):
        self.logger.info(args)
        self.logger.info(f'import {settings.kindle_xml}')

        tag = 'ASIN'
        if args.tag is not None:
            tag = args.tag

        asin_set = set()
        for event, el in etree.iterparse(settings.kindle_xml):
            if event =='end' and el.tag == tag:
                asin_set.add(el.text)
        with open(settings.outfile, 'w', encoding='utf-8') as out:
            for x in sorted(asin_set):
                out.write(f'{x}\n')

if(__name__ == '__main__'):
    parser = argparse.ArgumentParser()
    parser.add_argument('--version', action='version', version=f'version {__version__})')
    parser.add_argument('--tag')
    args = parser.parse_args()
    Main().main(args)
