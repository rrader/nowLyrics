# -*- encoding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 5
_modified_time = 1321638497.20583
_template_filename='/home/roma/Projects/lyrics_searcher/lyrics_searcher/templates/info.mako'
_template_uri='/info.mako'
_template_cache=cache.Cache(__name__, _modified_time)
_source_encoding='utf-8'
from webhelpers.html import escape
_exports = []


def render_body(context,**pageargs):
    context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        c = context.get('c', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 1
        __M_writer(u'<p>\n\u0414\u043b\u044f \u043f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u044f ')
        # SOURCE LINE 2
        __M_writer(escape(c.luser))
        __M_writer(u' <br>\nNow playing: ')
        # SOURCE LINE 3
        __M_writer(escape(c.nowplaying))
        __M_writer(u'<br>\n<br>\n\u041d\u0430\u0439\u0434\u0435\u043d\u043e: ')
        # SOURCE LINE 5
        __M_writer(escape(c.found_count))
        __M_writer(u'<br>\n')
        # SOURCE LINE 6
        if c.found_count>0:
            # SOURCE LINE 7
            __M_writer(u'\n<ol>\n')
            # SOURCE LINE 9
            for current_lyrics in c.lyricses:
                # SOURCE LINE 10
                __M_writer(u'<li> <pre>\n')
                # SOURCE LINE 11
                __M_writer(escape(current_lyrics))
                __M_writer(u'\n</pre>\n</li>\n')
                pass
            # SOURCE LINE 15
            __M_writer(u'</ol>\n')
            pass
        # SOURCE LINE 17
        __M_writer(u'</p>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


