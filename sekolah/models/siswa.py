from odoo import api, fields, models, _

class Siswa(models.Model):
	_name = 'sekolah.siswa'

	name = fields.Char("Name")
	kelas = fields.Selection([
        ('1', 'I'),
        ('2', 'II'), 
        ('3', 'III')], string='Kelas')
