from odoo import api, fields, models, _

class Ekskul(models.Model):
	_name = 'sekolah.custom.ekskul'

	name = fields.Char(string="Ekskul")
	siswa_ids = fields.Many2many('sekolah.siswa')

	def generate_eval(self):
		siswa_list = []
		for siswa in self.siswa_ids:
			siswa_list.append([0,0, {
				'siswa_id': siswa.id
				}])

		new = self.env["sekolah.custom.evalu.wizard"].create({
				"name" : self.name,
				"siswa_ids": siswa_list,
				"ekskul_id" : self.id
			})

		return {
			'type': 'ir.actions.act_window',
	        'name': 'Generate Eval',
	        'res_model': 'sekolah.custom.evalu.wizard',
	        'view_type': 'form',
	        'res_id'    : new.id,
	        'view_mode': 'form',
	        'target': 'new',
	        'context': {'parent_obj': self.id}

		}
