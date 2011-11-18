# -*- encoding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 5
_modified_time = 1321633402.627812
_template_filename='/home/roma/Projects/lyrics_searcher/lyrics_searcher/templates/input.mako'
_template_uri='/input.mako'
_template_cache=cache.Cache(__name__, _modified_time)
_source_encoding='utf-8'
from webhelpers.html import escape
_exports = []


def render_body(context,**pageargs):
    context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        __M_writer = context.writer()
        # SOURCE LINE 1
        __M_writer(u'<p>\n<form name="user" method="GET" action="/lastfm_lyrics/username">\nUsername on Last.FM: <input type="text" name="user">\n               <input type="submit" name="submit" value="Submit" />\n</form>\n</p>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


