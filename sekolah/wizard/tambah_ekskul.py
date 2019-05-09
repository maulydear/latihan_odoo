from odoo import api, fields, models, _

class CreateTambahEkskulWizard(models.TransientModel):
	_name = 'sekolah.create.tambah.ekskul.wizard'

	def get_default(self):
		context= self.env.context
		obj = self.env['sekolah.siswa'].search([("id","in", context.get('active_ids', False))])
		return obj

	ekskul_id = fields.Many2one("sekolah.custom.ekskul", string="Ekskul", required=False)
	siswa_ids = fields.One2many("sekolah.tambah.ekskul.wizard", "wizard_id", string="Siswa", required=False, default= get_default)

	def add_ekskul(self):
		siswa_list = []
		for siswa in self.siswa_ids:
			siswa_list.append([0,0, {
				'siswa_id': siswa.id
				}])

		new = self.env["sekolah.custom.ekskul"].search([("id","in", context.get('active_ids', False))])
		new.create({
				"siswa_ids": siswa_list
			})


class TambahEkskulWizard(models.TransientModel):
	_name = 'sekolah.tambah.ekskul.wizard'

	name = fields.Char("Name")
	wizard_id = fields.Many2one(comodel_name = "sekolah.create.tambah.ekskul.wizard", required=False)
	siswa_id = fields.Many2one("sekolah.siswa")