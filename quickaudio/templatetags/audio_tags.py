from django.conf import settings
from django import template
from django.contrib.sites.models import Site
from django.contrib.contenttypes.models import ContentType
from quickaudio.models import Audio

register = template.Library()

@register.simple_tag
def audio_player_for_object(content_object):
    """
    """
    content_type = ContentType.objects.get_for_model(content_object)

    try:
        audio_obj = Audio.objects.get(content_type=content_type, object_id=content_object.id)

        player_html = """
                        <div class="audio">
                        <object type="application/x-shockwave-flash" data="%sswf/template_mini_0.3.0/template_mini/player_mp3_mini.swf" width="200" height="20">
                            <param name="movie" value="%sswf/template_mini_0.3.0/template_mini/player_mp3_mini.swf" />
                            <param name="bgcolor" value="#333333" />
                            <param name="FlashVars" value="mp3=%s%s" />
                        </object>
                        <p class="caption">%s</p>
                        </div>
                      """ % (settings.STATIC_URL, settings.STATIC_URL, settings.MEDIA_URL, audio_obj.file, audio_obj.title)

        return player_html
    except Audio.DoesNotExist:
        return ''