# Helper functions for results app

def is_allowed(user):
    """ check if provided user is in admin or staff group """
    allowed_group = set(['admin', 'staff'])
    usr = User.objects.get(username=user)
    groups = [ x.name for x in usr.groups.all()]
    if allowed_group.intersection(set(groups)):
       return True
    return False