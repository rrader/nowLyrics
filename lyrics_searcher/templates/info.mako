# -*- coding: utf-8 -*-
<%inherit file="/base.mako" />

<%def name="head_tags()">
  <!-- add some head tags here -->
</%def>

<p>
Для пользователя <a href="http://last.fm/user/${c.luser}">${c.luser}</a> <br>
Now playing: ${c.nowplaying}<br>
</p>
<br>
Найдено: ${c.found_count}<br>
<table border="0">
<tr>

<%
  if c.trans_count>0:
    w = "70%"
  else:
    w = "100%"
%>

<td width=${w} valign=top>
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
</td>

% if c.trans_count>0:
<td valign=top>
% for current_translate in c.trans:
<a href="${current_translate[0]}">Перевод на ${current_translate[1]}</a>
<br>
% endfor
</td>
% endif
</tr>
</table>
</p>
