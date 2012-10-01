
from django.template import Library
register=Library()
@register.filter(name='repspaces')
def repspaces(value):
	return value.replace(" ","_")
register.filter('repspaces',repspaces)
@register.filter(name='key')
def key(d, key_name):
	return d[key_name]
register.filter('key',key)
