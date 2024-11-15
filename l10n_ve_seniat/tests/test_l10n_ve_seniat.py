# Copyright 2024 Binhex
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo.exceptions import ValidationError
from odoo.tests import tagged

from odoo.addons.account.tests.common import AccountTestInvoicingCommon


@tagged("post_install", "-at_install")
class TestL10nVeSeniat(AccountTestInvoicingCommon):
    @classmethod
    def setUpClass(cls, chart_template_ref="l10n_ve.ve_chart_template_amd"):
        super().setUpClass(chart_template_ref=chart_template_ref)

    @classmethod
    def setup_company_data(cls, company_name, chart_template):
        # OVERRIDE
        # to force the company to be venezuelan
        res = super().setup_company_data(
            company_name,
            chart_template=chart_template,
            country_id=cls.env.ref("base.ve").id,
        )
        return res

    def test_check_unique_l10n_ve_control_number_insensitive(self):
        # A new invoice instance with an existing l10n_ve_control_number
        invoice = self.create_invoice()
        control_number = invoice.l10n_ve_control_number
        invoice_2 = self.create_invoice()
        with self.assertRaises(ValidationError):
            invoice_2.write({"l10n_ve_control_number": control_number})
