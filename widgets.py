from django.core.urlresolvers import reverse
from django.utils.safestring import mark_safe
from django.forms import widgets
from django.conf import settings

class RelatedFieldWidgetCanAdd(widgets.Select):
    def __init__(self, related_model, related_url, *args, **kw):
        super(RelatedFieldWidgetCanAdd, self).__init__(*args, **kw)
        self.related_url = related_url
    def render(self, name, value, *args, **kwargs):
        self.related_url = reverse(self.related_url)
        output = [super(RelatedFieldWidgetCanAdd, self).render(name, value, *args, **kwargs)]
        output.append(u'<a href="%s" class="add-another" id="add_id_%s" onclick="return showAddAnotherPopup(this); return false;"> ' % \
            (self.related_url, name))
        output.append(u'+</a>')                                                                                                                               
        return mark_safe(u''.join(output))
