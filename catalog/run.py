#!/usr/bin/env python
from catalog_app import app


if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=5000)