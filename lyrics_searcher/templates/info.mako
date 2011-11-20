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
<table border="0" width="100%">
<tr>

<td width="60%" valign=top>
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
<br>
<a href="http://google.com/search?q=${c.lyrics_query}">Искать в Google</a><br>
<a href="http://yandex.ru/yandsearch?text=${c.lyrics_query}">Искать в Yandex</a><br>
</td>

<td valign=top width="*">
% for current_translate in c.trans:
<a href="${current_translate[0]}">Перевод на ${current_translate[1]}</a>
<br>
% endfor
<br>
<a href="http://google.com/search?q=${c.trans_query}">Искать перевод в Google</a><br>
<a href="http://yandex.ru/yandsearch?text=${c.trans_query}">Искать перевод в Yandex</a><br>
</td>
</tr>
</table>
</p>
