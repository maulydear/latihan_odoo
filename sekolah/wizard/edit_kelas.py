from odoo import api, fields, models, _


class KelasWizard(models.TransientModel):
    _name = 'sekolah.edit.kelas.wizard'

    kelas = fields.Selection([
        ('1', 'I'),
        ('2', 'II'), 
        ('3', 'III')], string='Kelas')

    
    @api.multi
    def change_class(self):
    	context = self.env.context
    	siswa = self.env['sekolah.siswa'].search([("id","in", context.get('active_ids', False))])
    	siswa.write({
    		"kelas" : self.kelas
    		})


