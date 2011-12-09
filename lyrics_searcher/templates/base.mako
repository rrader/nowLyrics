# -*- coding: utf-8 -*-
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN"
"http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html>
  <head>
    <title>nowLyrics</title>
    <meta name="description" content="Last.fm NowPlaying Music Lyrics Receiver" />
    <meta name="keywords" content="Lyrics,Music,Lastfm" />
    <meta name="author" content="Roman Rader (Antigluk)" />
    <meta http-equiv="content-type" content="text/html;charset=UTF-8" />
    ${self.head_tags()}

    <!-- G+1 -->
    <script type="text/javascript" src="https://apis.google.com/js/plusone.js"></script>
    <!-- /G+1 -->
        
    <!-- Вконтакте -->
    <script type="text/javascript" src="http://userapi.com/js/api/openapi.js?45"></script>

    <script type="text/javascript">
      VK.init({apiId: 2694628, onlyWidgets: true});
    </script>
    <!-- /Вконтакте -->
  </head>
  <body>
  
<!-- facebook like -->
<div id="fb-root"></div>
<script>(function(d, s, id) {
  var js, fjs = d.getElementsByTagName(s)[0];
  if (d.getElementById(id)) {return;}
  js = d.createElement(s); js.id = id;
  js.src = "//connect.facebook.net/en_US/all.js#xfbml=1";
  fjs.parentNode.insertBefore(js, fjs);
}(document, 'script', 'facebook-jssdk'));</script>
<!-- /facebook like -->

    <H1><a href="/"><font color="#002244">nowLyrics</font></a></H1>
    ${self.body()}
    <hr>
    Created by <a href="http://www.google.com/profiles/antigluk">Antigluk (c)</a>
    <script type="text/javascript">

      var _gaq = _gaq || [];
      _gaq.push(['_setAccount', 'UA-6152823-8']);
      _gaq.push(['_trackPageview']);

      (function() {
        var ga = document.createElement('script'); ga.type = 'text/javascript'; ga.async = true;
        ga.src = ('https:' == document.location.protocol ? 'https://ssl' : 'http://www') + '.google-analytics.com/ga.js';
        var s = document.getElementsByTagName('script')[0]; s.parentNode.insertBefore(ga, s);
      })();

    </script>
  </body>
</html>

<%def name="social()">
<g:plusone annotation="inline" href="http://nowlyrics.pp.ua/"></g:plusone><br><br>
<a href="https://twitter.com/share" class="twitter-share-button" data-url="http://nowlyrics.pp.ua" data-text="Ищи текст песни &quot;now playing&quot; на #lastfm с помощью nowLyrics!" data-count="horizontal" data-lang="ru">Твитнуть</a><script type="text/javascript" src="//platform.twitter.com/widgets.js"></script><br><br>
<div class="fb-like" data-href="http://nowlyrics.pp.ua" data-send="false" data-width="450" data-show-faces="true"></div><br><br>

<div id="vk_like"></div>
<script type="text/javascript">
VK.Widgets.Like("vk_like", {type: "full", pageUrl: "http://nowlyrics.pp.ua/"});
</script>

<!-- VK Widget -->
<div id="vk_groups"></div>
<script type="text/javascript">
VK.Widgets.Group("vk_groups", {mode: 0, width: "200", height: "290"}, 32958049);
</script>
</%def>
