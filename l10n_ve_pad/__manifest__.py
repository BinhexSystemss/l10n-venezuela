# Copyright 2024 Binhex - Rolando Pérez
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).

{
    "name": "Estados y municipios venezolanos",
    "version": "16.0.1.0.0",
    "author": "Binhex, " "Odoo Community Association (OCA)",
    "website": "https://github.com/OCA/l10n-venezuela",
    "category": "Localization",
    "depends": ["base_address_extended", "l10n_ve"],
    "license": "AGPL-3",
    "data": [
        "data/res.country.state.csv",
        "data/res.city.csv",
        "views/res_partner_views.xml",
        "data/res_country_data.xml",
    ],
}