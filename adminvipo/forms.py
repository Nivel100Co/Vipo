from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, ButtonHolder, Submit,Button,Div, HTML
from crispy_forms.bootstrap import Field, InlineRadios, TabHolder, Tab,FormActions,StrictButton

class Register(forms.Form):

    #Campos definidos para el formulario de ingreso
    fullname = forms.CharField(label = '')
    email = forms.EmailField(label='')
    coproperty = forms.CharField(label = '')
    password = forms.CharField(label = '', widget = forms.PasswordInput)
    termsandconditions = forms.BooleanField(label = 'Acepto los terminos y condiciones y la Politica de privacidad')

    #Se define el init apra uilizar el helper de crispy
    def __init__(self, *args, **kwargs):
        super(Register, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = False
        self.helper.layout = Layout(
        	Div(
        		Field('fullname', placeholder='Nombre y primer apellido', css_class='form-group w-100 border-left-0 border-right-0 border-top-0'),
        		css_class="flex-shrink-1 mt-5"
        		),
        	Div(
        		Field('email', placeholder='E-mail', css_class='form-group w-100 border-left-0 border-right-0 border-top-0'),
        		css_class="flex-shrink-1 "
        		),

        	Div(
        		Field('coproperty', placeholder='Nombre de copropiedad', css_class='form-group w-100 border-left-0 border-right-0 border-top-0'),
        		css_class="flex-shrink-1 "
        		),

        	Div(
        		Field('password', placeholder='Contraseña', css_class='form-group w-100 border-left-0 border-right-0 border-top-0'),
        		css_class="flex-shrink-1 "
        		),

        	Div(
        		Field('termsandconditions', css_class='form-group w-100 border-left-0 border-right-0 border-top-0'),
        		css_class="flex-shrink-1 "
        		),

        	 Div(
                ButtonHolder(
                    Submit('submit', 'Crear Cuenta', css_class='btn-create-account w-100 pl-5 pr-5 pt-1 pb-1')
                ),
                css_class = 'd-flex justify-content-center '
                )

        	)
        self.fields['fullname'].required=True
        self.fields['email'].required=True
        self.fields['coproperty'].required=True
        self.fields['password'].required=True
        self.fields['termsandconditions'].required=True
        
class Login(forms.Form):

    #Campos definidos para el formulario de ingreso
    email = forms.EmailField(label='')
    password = forms.CharField(label = '', widget = forms.PasswordInput)

    #Se define el init apra uilizar el helper de crispy
    def __init__(self, *args, **kwargs):
        super(Login, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = False
        self.helper.layout = Layout(
        	Div(
        		Field('email', placeholder='E-mail', css_class='form-group w-100 border-left-0 border-right-0 border-top-0'),
        		css_class="flex-shrink-1 mt-5"
        		),
        	Div(
        		Field('password', placeholder='Contraseña', css_class='form-group w-100 border-left-0 border-right-0 border-top-0'),
        		css_class="flex-shrink-1 "
        		),
        	Div(
        	    HTML("<a href='../password-recovery'>¿Olvidaste tu Contraseña?</a>"),
        		css_class="d-flex justify-content-end pt-4 pb-4"
        		),
        	 Div(
                ButtonHolder(
                    Submit('submit', 'Entrar', css_class='btn-create-account w-100 pl-5 pr-5 pt-1 pb-1')
                ),
                css_class = 'd-flex justify-content-center '
                )

        	)
        self.fields['email'].required=True
        self.fields['password'].required=True












