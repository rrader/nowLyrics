<%inherit file="/base.mako" />

<%def name="head_tags()">
  <!-- add some head tags here -->
</%def>

<p>
<form name="user" method="GET" action="/lastfm_lyrics/username">
Username on Last.FM: <input type="text" name="user">
               <input type="submit" name="submit" value="Submit" />
</form>
</p>
