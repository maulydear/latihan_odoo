from odoo import api, fields, models, _

class Trainer(models.Model):
	_name = 'sekolah.custom.trainer'

	name = fields.Char(string="Name")
