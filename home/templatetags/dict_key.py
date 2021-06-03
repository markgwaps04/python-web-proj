from django import template
import locale

locale.setlocale(locale.LC_ALL, '')

register = template.Library()

def is_number(string):
    try:
        float(string)
        return True
    except ValueError:
        return False

def of_buget_get(d, k, key):
    if d[k][key] == None : return  0
    if not is_number(d[k][key]) : return d[k][key]
    round_val = round(float(d[k][key]) or 0,2)
    return locale.format("%.2f", round_val, grouping=True)
    pass

@register.filter(name='dict_key')
def dict_key(d, k):
    '''Returns the given key from a dictionary.'''
    return d[k]

@register.filter(name="is_subkey")
def is_subkey(d, k):
    return "sub_key" in d[k]

@register.filter(name="get_weekly")
def get_weekly(d, k):
    return of_buget_get(d,k,"weekly")


@register.filter(name="get_biweekly")
def get_biweekly(d, k):
    return of_buget_get(d,k,"bi-weekly")

@register.filter(name="get_monthly")
def get_monthly(d, k):
    return of_buget_get(d,k,"monthly")


@register.filter(name="get_yearly")
def get_yearly(d, k):
    return of_buget_get(d,k,"yearly")

@register.filter(name="get_items")
def get_items(d,k):
    return d[k]['items']

@register.filter(name="get_code")
def get_code(d,k):
    return d[k]['code']
