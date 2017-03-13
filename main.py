#!/usr/bin/python3
# -*- coding: utf-8 -*-

import connexion

def dupa(show=None):
    if show:
        return 'sam jesteś dupa'
    return 'dupa'

if __name__ == '__main__':
    app = connexion.App(__name__, specification_dir='swagger/')
    app.add_api('my_api.yaml')
    app.run(server='tornado', port=8080)

