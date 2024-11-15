# Copyright 2024 Binhex (http://binhex.cloud/)
# @author: Rolando Pérez <rolando.perez@binhex.cloud>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

import logging

from odoo import SUPERUSER_ID, api

logger = logging.getLogger(__name__)


def set_rate_type_on_built_in_taxes(env, company):
    tax_templates = (
        env["account.tax.template"]
        .with_context(active_test=False)
        .search(
            [
                ("l10n_ve_rate_type", "!=", False),
                ("chart_template_id.country_id", "=", company.country_id.id),
            ]
        )
    )
    tax_template_external_ids = tax_templates.get_external_id()
    for tax_template in tax_templates:
        external_id = tax_template_external_ids.get(tax_template.id)
        if external_id:
            tax_external_id = (
                f"{external_id.split('.')[0]}.{company.id}_{external_id.split('.')[-1]}"
            )
            tax = env.ref(tax_external_id, raise_if_not_found=False)
            if tax:
                tax.l10n_ve_rate_type = tax_template.l10n_ve_rate_type


def post_init_hook(cr, registry):
    env = api.Environment(cr, SUPERUSER_ID, {})
    companies = env["res.company"].search([])
    for company in companies.filtered(lambda c: c.country_id == env.ref("base.ve")):
        logger.info(
            "Updating rate types according to venezuelan law for built-in taxes on\
                 company %s ID %d",
            company.display_name,
            company.id,
        )
        set_rate_type_on_built_in_taxes(env, company)

    return
