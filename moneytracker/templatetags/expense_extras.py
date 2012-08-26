
from django.template import Library
register=Library()
@register.filter(name='repspaces')
def repspaces(value):
	return value.replace(" ","_")
register.filter('repspaces',repspaces)
