from django import template

register = template.Library()


@register.filter(name='display_able')
def display_able(timeDeltaObject):
    """Convert a datetime.timedelta object into Days, Hours, Minutes, Seconds."""
    seconds = timeDeltaObject.total_seconds()
    time = ''

    if seconds > 3600:
        hours = seconds // 3600
        time += " {}h".format(int(hours))
        seconds = seconds - hours*3600

    if seconds > 60:
        mins = seconds // 60
        time += " {}m".format(int(mins))
        seconds = seconds - mins*60

    if seconds > 0:
        time += " {}s".format(int(seconds))
    return time
