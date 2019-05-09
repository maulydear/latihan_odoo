from odoo import api, fields, models, _

class Matapelajaran(models.Model):
	_name = 'sekolah.matapelajaran'
	_rec_name = 'name'

	name = fields.Char("Name")