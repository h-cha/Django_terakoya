# -*- coding: utf-8 -*-

from django import forms

class TerakoyaForm(forms.Form):
    q_num = forms.IntegerField(label='問題番号:',max_value=10)
    a1 = forms.IntegerField(label='(1)')
    a2 = forms.IntegerField(label='(2)')
    a3 = forms.IntegerField(label='(3)')
    a4 = forms.IntegerField(label='(4)')
    a5 = forms.IntegerField(label='(5)')
    
class IDForm(forms.Form):
    id = forms.IntegerField(label='問題番号',max_value=10)
    

class HelloForm(forms.Form):
    data=[
            ('one', 'radio 1'),
            ('two', 'radio 2'),
            ('three', 'radio 3')
        ]
    choice = forms.ChoiceField(label='radio', \
            choices=data, widget=forms.RadioSelect())

