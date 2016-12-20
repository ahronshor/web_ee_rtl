# -*- coding: utf-8 -*-

from odoo import models, tools


class QWeb(models.AbstractModel):
    _name = 'ir.qweb'
    _inherit = 'ir.qweb'

    def render(self, id_or_xml_id, values=None):

        lang_obj = self.env['res.lang']
        lang = self._context.get('lang', None)

        lang_directions = lang_obj.get_languages_dir()
        lang_direction = lang_directions.get(lang, 'ltr')
        values['lang_direction'] = values.get('lang_direction', None) or lang_direction
        return super(QWeb, self).render(id_or_xml_id, values=values)


class res_lang(models.Model):
    _name = 'res.lang'
    _inherit = 'res.lang'

    @tools.ormcache(skiparg=3)
    def _get_languages_dir(self):
        langs = self.search([('active', '=', True)])
        return dict([(lg.code, lg.direction) for lg in langs])

    def get_languages_dir(self):
        return self._get_languages_dir()

