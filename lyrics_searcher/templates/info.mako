# -*- coding: utf-8 -*-
<%inherit file="/base.mako" />

<%def name="head_tags()">
  <!-- add some head tags here -->
</%def>

<p>
Для пользователя <a href="http://last.fm/user/${c.luser}">${c.luser}</a> <br>
Now playing: ${c.nowplaying}<br>

<br>
Найдено: ${c.found_count}<br>
% if c.found_count>0:

<ol>
% for current_lyrics in c.lyricses:
<li> <pre>
${current_lyrics}
</pre>
</li>
% endfor
</ol>
% endif
</p>
