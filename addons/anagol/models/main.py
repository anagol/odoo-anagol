from odoo import fields, models, api


class AnagolMain(models.Model):
    _name = 'anagol.main'
    _description = 'Anagol'

    name = fields.Char(compute='_compute_name')
    first_name = fields.Char(string='Имя')
    last_name = fields.Char(string='Фамилия')
    dob = fields.Date(string='Дата рождения')

    def _compute_name(self):
        for rec in self:
            rec.name = "{first_name} {last_name}".format(first_name=self.first_name, last_name=self.last_name)
