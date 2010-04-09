from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes import generic
from datetime import datetime
import os

class Audio(models.Model):
    """
    An audio clip that can be generically related to any model.
    """
    
    file = models.FileField("Audio", upload_to='content/audio/', help_text='Only MP3 files are supported at this time.')
    pub_date = models.DateTimeField("Date published", default=datetime.now)
    title = models.CharField(max_length=100)
    slug = models.SlugField()
    summary = models.TextField()
    content_type = models.ForeignKey(ContentType)
    object_id = models.PositiveIntegerField()
    content_object = generic.GenericForeignKey('content_type', 'object_id')
    
    def __unicode__(self):
        return self.title
    
    def get_absolute_url(self):
        #TODO add reverse url lookup once urls.py is defined
        pass
    
    def doc_dir(self):
        return os.path.dirname(self.get_file_filename())
    
    def remove_dirs(self):
        if os.path.isdir(self.doc_dir()):
            if os.listdir(self.doc_dir()) == []:
                os.removedirs(self.doc_dir())
    
    def delete(self):
        super(Audio, self).delete()
