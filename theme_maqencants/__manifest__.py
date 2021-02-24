# -*- encoding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'MaqEncants Theme',
    'description': 'MaqEncants Theme',
    'category': 'Theme/Corporate',
    'version': '1.0',
    'depends': ['website', 'website_sale', 'website_theme_install', 'website_cookie_notice'],
    'data': [
        'views/assets.xml',
        'views/layout.xml',
        'views/store.xml',
        'views/website.xml',
    ],
    'images': [
        'static/description/bootswatch.png',
        'static/description/bootswatch_screenshot.jpg',
    ],
}
