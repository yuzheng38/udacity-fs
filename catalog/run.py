#!/usr/bin/env python
from catalog_app import app


if __name__ == '__main__':
    app.debug = True
    app.run(host='127.0.0.1', port=5000)