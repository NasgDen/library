from django import forms

from .models import News


class StyleFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["title"].widget.attrs.update({"class": "form-control"})
        self.fields["content"].widget.attrs.update(size="40")
        # for fild_name, field in self.fields.items():
            # field.widget.attrs['class'] = "form-control"
            # print(field.widget.attrs['class'])
            # if fild_name == 'title':
            #     field.widget.attrs['placeholder'] = "Введите название товара"
            # elif fild_name == 'content':
            #     field.widget.attrs['placeholder'] = "Введите описание товара"


class NewsForm(forms.ModelForm):
    """ Класс реализует интерфейс для создания новости """

    class Meta:
        model = News
        fields = ['title', 'content']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'Введите название новости'}),
            'content': forms.Textarea(attrs={'class': 'styled-textarea'}),
        }
