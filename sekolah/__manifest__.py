{
	'name': "Sekolah",
	'version': '12.0.0.0.1',
	'depends': ['base'],
	'author': "ramadea10@gmail.com",
	'category': "Education",
	'website': 'http://www.vitraining.com',
	'description': """\
	Sekolah
	
	""",

	'data': [
		'security/sekolah_security.xml',
		'security/ir.model.access.csv',
		'views/menu.xml',
		'views/siswa.xml',
		'views/matapelajaran.xml',
		'views/t_ujian.xml',
		'views/t_ujian_det.xml',
		'views/edit_kelas_wizard.xml',
		'views/tambah_ekskul_wizard.xml',
	]
}