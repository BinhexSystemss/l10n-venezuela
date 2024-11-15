# Copyright 2024 Binhex
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).

from odoo import fields, models

from .tax_rate_types_mapping import TAX_RATE_TYPES


class AccountTaxTemplate(models.Model):
    _inherit = "account.tax.template"

    l10n_ve_rate_type = fields.Selection(selection=TAX_RATE_TYPES)

    def _get_tax_vals(self, company, tax_template_to_tax):
        val = super()._get_tax_vals(company, tax_template_to_tax)
        val["l10n_ve_rate_type"] = self.l10n_ve_rate_type
        return val
