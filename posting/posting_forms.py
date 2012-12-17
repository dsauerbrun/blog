from posting.models import Location
from django.forms import Form,ModelForm,Textarea,TextInput,Select,ModelMultipleChoiceField,CheckboxSelectMultiple

class MultipleLocationChoiceField(ModelMultipleChoiceField):
	def label_from_instance(self, instance):
		return instance.title

class location_form(Form):
#	locations = Location.objects.all().order_by('-date')	
#	location_map =()
#	for location in locations:
#		new_tuple=((location.id,location.title),)
#		location_map = location_map + new_tuple
	location_list = MultipleLocationChoiceField(queryset=Location.objects.order_by('-date'), widget=Select(attrs={'size':'14'}))
