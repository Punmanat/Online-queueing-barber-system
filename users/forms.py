from django import forms
from django.core.validators import validate_email

from users.models import BarberShop, Customer


class RegisterCustomerForm(forms.Form):
    email = forms.CharField(label="email", required=True, validators=[validate_email])
    email.widget.attrs['placeholder'] = 'email'
    email.widget.attrs['class'] = 'form-input'

    username = forms.CharField(label="username", required=True)
    username.widget.attrs['placeholder'] = 'username'
    username.widget.attrs['class'] = 'form-input'

    pass1 = forms.CharField(label="password", required=True, widget=forms.PasswordInput)
    pass1.widget.attrs['placeholder'] = 'password'
    pass1.widget.attrs['class'] = 'form-input'

    pass2 = forms.CharField(label="re-password", required=True, widget=forms.PasswordInput)
    pass2.widget.attrs['placeholder'] = 'password'
    pass2.widget.attrs['class'] = 'form-input'

    name = forms.CharField(required=True)
    name.widget.attrs['placeholder'] = 'name'
    name.widget.attrs['class'] = 'form-input'

    tel = forms.CharField(required=True, max_length=10)
    tel.widget.attrs['placeholder'] = 'phone number'
    tel.widget.attrs['class'] = 'form-input'

    style = forms.CharField(required=True, max_length=100)
    style.widget.attrs['placeholder'] = 'style'
    style.widget.attrs['class'] = 'form-input'

    MALE = "M"
    FEMALE = "F"
    OTHER = "X"
    GENDERS = (
        (MALE, 'ชาย'),
        (FEMALE, 'หญิง'),
        (OTHER, 'อื่น'),
    )
    gender = forms.ChoiceField(label="gender", widget=forms.RadioSelect(), required=True, choices=GENDERS)
    gender.widget.attrs['class'] = "fontt"

    def clean_style(self):
        data = self.cleaned_data['style']

        if (not data):
            raise forms.ValidationError("โปรดใส่ทรงผมที่ท่านชื่นชอบ")

        return data

    def clean_tel(self):
        data = self.cleaned_data['tel']

        if not data.isdigit():
            raise forms.ValidationError("เบอร์โทรศัพท์ต้องเป็นตัวเลขเท่านั้น")
        if len(data) < 10:
            raise forms.ValidationError("เลขโทรศัพท์ต้องเท่ากับ 10 ตัว")

        return data

    def clean_pass1(self):
        data = self.cleaned_data['pass1']
        if (len(data) < 8):
            raise forms.ValidationError("รหัสผ่านต้องมีตัวอักษรมากกว่า 8 ตัวอักษร")

        return data

    def clean_pass2(self):
        data = self.cleaned_data['pass2']

        if (len(data) < 8):
            raise forms.ValidationError("รหัสผ่านใหม่ต้องมีตัวอักษรมากกว่า 8 ตัวอักษร")

        return data

    def clean(self):
        clean = super().clean()
        pass1 = clean.get('pass1')
        pass2 = clean.get('pass2')
        if (pass1 != pass2):
            raise forms.ValidationError("รหัสผ่านใหม่ กับ ยืนยันรหัสผ่านต้องเหมือนกัน")


class RegisterBarberForm(forms.Form):
    email = forms.CharField(label="email", required=False, validators=[validate_email])
    email.widget.attrs['placeholder'] = 'email'
    email.widget.attrs['class'] = 'form-input'

    username = forms.CharField(label="username", required=True, )
    username.widget.attrs['placeholder'] = 'username'
    username.widget.attrs['class'] = 'form-input'

    pass1 = forms.CharField(label="password", required=True, widget=forms.PasswordInput)
    pass1.widget.attrs['placeholder'] = 'password'
    pass1.widget.attrs['class'] = 'form-input'

    pass2 = forms.CharField(label="re-password", required=True, widget=forms.PasswordInput)
    pass2.widget.attrs['placeholder'] = 're-password'
    pass2.widget.attrs['class'] = 'form-input'

    tel = forms.CharField(label="tel", max_length=10)
    tel.widget.attrs['placeholder'] = 'mobile phone'
    tel.widget.attrs['class'] = 'form-input'

    style = forms.CharField(label="hit style in your shop",required=True, max_length=100)
    style.widget.attrs['placeholder'] = 'รองทรงสูง, สกีนเฮด'
    style.widget.attrs['class'] = 'form-input'

    address = forms.CharField(label="address", widget=forms.Textarea, required=False)
    address.widget.attrs['placeholder'] = 'address'
    address.widget.attrs['class'] = 'form-input'

    description = forms.CharField(label="description", widget=forms.Textarea, required=False)
    description.widget.attrs['placeholder'] = 'description'
    description.widget.attrs['class'] = 'form-input'

    shopname = forms.CharField(label="shop Name", required=False, max_length=250)
    shopname.widget.attrs['placeholder'] = 'shopname'
    shopname.widget.attrs['class'] = 'form-input'

    def clean_style(self):
        data = self.cleaned_data['style']

        if (not data):
            raise forms.ValidationError("โปรดใส่ทรงผมยอดนิยมของทางร้าน")

        return data

    def clean_address(self):
        data = self.cleaned_data['address']
        if (not data):
            raise forms.ValidationError('โปรดใส่ที่อยู่')
        return data

    def clean_desciption(self):
        data = self.cleaned_data['description']
        if (not data):
            raise forms.ValidationError('โปรดใส่รายละเอียดของร้าน')
        return data

    def clean_shopname(self):
        data = self.cleaned_data['shopname']

        if (not data):
            raise forms.ValidationError("โปรดใส่ชื่อร้าน")

        return data

    def clean_tel(self):
        data = self.cleaned_data['tel']

        if len(data) < 10:
            raise forms.ValidationError("เลขโทรศัพท์ต้องเท่ากับ 10 ตัว")
        if not data.isdigit():
            raise forms.ValidationError("เบอร์โทรศัพท์ต้องเป็นตัวเลขเท่านั้น")

        return data

    def clean_pass1(self):
        data = self.cleaned_data['pass1']
        if len(data) < 8:
            raise forms.ValidationError("รหัสผ่านต้องมีตัวอักษรมากกว่า 8 ตัวอักษร")

        return data

    def clean_pass2(self):
        data = self.cleaned_data['pass2']

        if len(data) < 8:
            raise forms.ValidationError("รหัสผ่านใหม่ต้องมีตัวอักษรมากกว่า 8 ตัวอักษร")

        return data

    def clean(self):
        clean = super().clean()
        pass1 = clean.get('pass1')
        pass2 = clean.get('pass2')
        if pass1 != pass2:
            raise forms.ValidationError("รหัสผ่านใหม่ กับ ยืนยันรหัสผ่านต้องเหมือนกัน")


class ChangePasswordForm(forms.Form):
    old_password = forms.CharField(label="รหัสผ่านเก่า")
    new_password1 = forms.CharField(label="รหัสผ่านใหม่")
    new_password2 = forms.CharField(label="ยืนยันรหัสผ่าน")

    def clean_newpassword1(self):
        value = self.cleaned_data['new_password1']

        if (len(value) < 8):
            raise forms.ValidationError("รหัสผ่านใหม่ต้องมีตัวอักษรมากกว่า 8 ตัวอักษร")
        return value

    def clean_newpassword2(self):
        value = self.cleaned_data['new_password2']

        if (len(value) < 8):
            raise forms.ValidationError("รหัสผ่านใหม่ต้องมีตัวอักษรมากกว่า 8 ตัวอักษร")
        return value

    def clean(self):
        clean = super().clean()
        pass1 = clean.get('new_password1')
        pass2 = clean.get('new_password2')

        if (pass1 != pass2):
            raise forms.ValidationError("รหัสผ่านใหม่ กับ ยืนยันรหัสผ่านต้องเหมือนกัน")
        elif (pass1 == pass2):
            if (len(pass1) < 8 and len(pass2) < 8):
                self.add_error('new_password1', "รหัสผ่านใหม่ต้องมีตัวอักษรมากกว่า 8 ตัวอักษร")
                self.add_error('new_password2', "รหัสผ่านใหม่ต้องมีตัวอักษรมากกว่า 8 ตัวอักษร")

class BarberShopForm(forms.ModelForm):
    class Meta:
        model = BarberShop
        exclude = ['user']

class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        exclude = ['user']