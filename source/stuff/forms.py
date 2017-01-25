from django import forms

from stuff.models import Item

class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = [
            'category',
            'location',
            'container',
            'description',
            'unit',
            'qty',
            'purchaseDate',
            'bestByDate',
            'checkOnFrequency',
            'moreInfoLink',
            'waterStored',
            'numServings',
            'calPerServing',
            'prescriptionMed',
            'notes',
        ]

