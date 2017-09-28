class ExcelObject(object):
    name = ''
    price = 0
    url = ''
    vendor = ''

    def __init__(self, name, price, url, vendor):
        self.name = name
        self.price = price
        self.url = url
        self.vendor = vendor