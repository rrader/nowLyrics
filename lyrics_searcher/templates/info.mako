<p>
Для пользователя ${c.luser} <br>
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
