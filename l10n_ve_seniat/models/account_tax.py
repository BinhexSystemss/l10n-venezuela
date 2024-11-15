from odoo import fields, models

from .tax_rate_types_mapping import TAX_RATE_TYPES


class AccountTax(models.Model):
    _inherit = "account.tax"

    l10n_ve_rate_type = fields.Selection(
        TAX_RATE_TYPES,
        string="Rate Type",
        help="Specify the type of rate according to Venezuelan tax law.",
        default="general",
    )
