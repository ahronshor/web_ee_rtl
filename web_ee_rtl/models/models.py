# -*- coding: utf-8 -*-

from openerp import models
import openerp

class QWeb(models.AbstractModel):
    _name = 'ir.qweb'
    _inherit = 'ir.qweb'

    def render(self, cr, uid, id_or_xml_id, qwebcontext=None, loader=None, context=None):
        context = context or {}

        if qwebcontext and qwebcontext.get('lang_direction', None):
            return super(QWeb, self).render(cr, uid, id_or_xml_id, qwebcontext=qwebcontext, loader=loader, context=context)

        lang_obj = self.pool.get('res.lang')
        lang = context.get('lang', None)

        if not lang:
            if qwebcontext.get('lang', None):
                lang = qwebcontext.get('lang')
            elif uid:
                user = self.pool.get('res.users').browse(cr, uid, uid, context=context)
                lang = user.lang and user.lang or user.partner_id.lang
            else:
                lang = 'en_US'

        lang_directions = lang_obj.get_languages_dir(cr, uid, [], context=context)
        lang_direction = lang_directions.get(lang, 'ltr')
        qwebcontext['lang_direction'] = qwebcontext.get('lang_direction', None) or lang_direction
        return super(QWeb, self).render(cr, uid, id_or_xml_id, qwebcontext=qwebcontext, loader=loader, context=context)

class res_lang(models.Model):
    _name = 'res.lang'
    _inherit = 'res.lang'

    @openerp.tools.ormcache(skiparg=3)
    def _get_languages_dir(self, cr, uid, ids, context=None):
        ids = self.search(cr, uid, [('active', '=', True)], context=context)
        langs = self.browse(cr, uid, ids, context=context)
        return dict([(lg.code, lg.direction) for lg in langs])

    def get_languages_dir(self, cr, uid, ids, context=None):
        return self._get_languages_dir(cr, uid, ids, context=context)

    def write(self, cr, uid, ids, vals, context=None):
        # self._get_languages_dir.clear_cache()
        return super(res_lang, self).write(cr, uid, ids, vals, context)
