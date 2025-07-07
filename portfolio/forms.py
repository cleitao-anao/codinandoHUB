from django import forms
from .models import Project

class ProjectAdminForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = '__all__'
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Torna o campo slug somente leitura se o objeto já existir
        if self.instance and self.instance.pk:
            self.fields['slug'].widget.attrs['readonly'] = True
