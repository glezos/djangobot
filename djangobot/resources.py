"""
Store the various IRC channels and their settings here.
"""

class BotResource:
    """Something to store the relevant URLs for various resources.
    
    Store URLs with a single %s in them. Eg.:

       ticket = "http://example.com/tickets/%s"
    """
    
    ATTRS = ['ticket', 'changeset', 'person', 'irc_spotted']
    def __init__(self, **kwargs):
        for kw in kwargs:
            if kw in ATTRS:
                self.kw = kw
                del kwargs[kw]

##

RESOURCES = {}

RESOURCES['#django'] = BotResource(
    ticket="http://code.djangoproject.com/ticket/%s",
    changeset="http://code.djangoproject.com/changeset/%s",
    person="http://djangopeople.net/api/irc_lookup/%s/",
    irc_spotted="http://djangopeople.net/api/irc_spotted/%s/",
)

RESOURCES['#django-hotclub'] = RESOURCES['#django']
RESOURCES['#django-hotclub'].ticket = "http://code.google.com/p/django-hotclub/issues/detail?id=%s"
RESOURCES['#django-hotclub'].changeset = "http://code.google.com/p/django-hotclub/source/detail?r=%s"

RESOURCES['#transifex'] = RESOURCES['#django']
RESOURCES['#transifex'].ticket = "code.transifex.org/ticket/%s"
RESOURCES['#transifex'].changeset = "http://code.transifex.org/changeset/%s"

##

def replace_by_resource(self, context, text, resource_type):
    """Replace a url based on the context (eg. IRC channel)."""
    if context in RESOURCES.keys():
        base_url = RESOURCES.get(self.channel.name, resource_type)
        try:
            return base_url % ticket
        except TypeError:
            return

