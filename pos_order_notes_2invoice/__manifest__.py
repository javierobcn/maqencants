# -*- coding: utf-8 -*-
{
  "name"                 :  "POS Order Notes to Invoice",
  "summary"              :  "The module allows print the notes to individual orderlines in Invoices.",
  "category"             :  "Point Of Sale",
  "version"              :  "1.0",
  "sequence"             :  1,
  "author"               :  "Sugestionweb",
  "license"              :  "Other proprietary",
  "website"              :  "https://sugestionweb.com",
  "description"          :  """https://sugestionweb.com""",
  "live_test_url"        :  "",
  "depends"              :  ['point_of_sale','pos_order_notes'],
  "data"                 :  [
                             'views/pos_config_view.xml',
                            ],
  "qweb"                 :  ['static/src/xml/pos_order_note.xml'],
  "images"               :  ['static/description/Banner.png'],
  "application"          :  True,
  "installable"          :  True,
  "auto_install"         :  False,
  "price"                :  0,
  "currency"             :  "EUR",
  "pre_init_hook"        :  "pre_init_check",
}
