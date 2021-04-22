from django import forms

from inventory.models import InventoryItem


# Creating a model form (using a model to collect data)
class ItemCreateForm(forms.ModelForm):
    #  Here we are adjusting the inputs, adding attributes to give clarity to the user
    item = forms.CharField(widget=forms.Textarea(
        attrs={
            "placeholder": "Enter the name of the item to add...",
            "rows": 1
        }
    ))
    desc = forms.CharField(widget=forms.Textarea(
        attrs={
            "placeholder": "Enter a description of the item..."
                           "These can be keywords!",
            "rows": 4,
        }
    ))
    loc = forms.CharField(widget=forms.Textarea(
        attrs={
            "placeholder": "Where is this normally kept? It helps you find it next time!",
            "rows": 4,
        }
    ))

    #  Here we create a function to check if a specific thing is included in the input and
    #  raise an error if it is not. I'm just testing it with the image field for now.
    def clean_image(self, *args, **kwargs):
        image = self.cleaned_data.get("image")
        #  Adding the exception first so we can have multiple errors listed. If none, it ill return the image
        if not "dotpng" in image:
            raise forms.ValidationError("This must have 'dotpng' in the name for testing")
        else:
            return image

    class Meta:
        model = InventoryItem
        fields = [
            'item',
            'desc',
            'loc',
            'image'
        ]

# Creating a raw form, not using a model.
# class RawItemCreateForm(forms.Form):
#     item = forms.CharField()
#     desc = forms.CharField(required=False, widget=forms.Textarea)
#     loc = forms.CharField()
#     image = forms.CharField(required=False)
