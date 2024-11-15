{
    "name": "Requerimientos Fiscales Seniat Venezuela",
    "author": "Binhex," "Odoo Community Association (OCA)",
    "website": "https://github.com/OCA/l10n-venezuela",
    "license": "AGPL-3",
    "category": "Localization",
    "version": "16.0.1.0.0",
    "depends": [
        "account",
        "base_vat",
        "l10n_ve",
        "account_invoice_supplier_ref_unique",
    ],
    "data": [
        "data/ir_sequence_data.xml",
        "data/account_tax_template_data.xml",
        "views/account_tax_views.xml",
        "views/account_move_views.xml",
    ],
    "post_init_hook": "post_init_hook",
}
