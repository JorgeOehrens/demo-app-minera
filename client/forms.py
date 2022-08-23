from django import forms

from .models import Entrada

class PostForm(forms.ModelForm):

	class Meta:
		model = Entrada
		fields = ["unidad"]

		widgets = {

			'unidad':forms.TextInput(

				attrs = {'id':'post-formulario', 'requerid':True, 'placeholder':'Escribe tu post'}
				)
			

		}