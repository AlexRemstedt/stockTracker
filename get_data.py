# -*- coding: utf-8 -*-
"""
stocktracker.get_data
~~~~~~~~~~~~~~~~~~~~~

Get data from shares.

:author: Alex Remstedt
:date: July 2021
"""
import requests


class Share():
    """Get data from shares."""    

    token = 'pk_dae64b222a3a401da19fa29c020c0897'  # publishable
    base_url = 'https://cloud.iexapis.com/'

    def __init__(self, code) -> None:
        self.code = code
        self.url = 'https://cloud.iexapis.com/stable/stock/' \
            f'{self.code}/quote?token={self.token}'
        pass

    def get_data(self):
        """Empty docs."""
        r = requests.get(self.url).json()
        return r

        
if __name__ == "__main__":
    apple = Share('AAPL')
    print(apple.get_data())
