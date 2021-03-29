from django import forms

tof = [
    ("college/university", "College/University"),
    ("company/organization", "Company/Organization"),
    ("others", "Others"),
]

ef = [
    ("below 12", "Below 12"),
    ("below 16", "Below 16"),
    ("below 18", "Below 18"),
]

g = [
    ("female", "Female"),
    ("male", "Male"),
]


class HostForm(forms.Form):
    Your_Full_Name = forms.CharField(
        widget=forms.TextInput(
            attrs={"class": "form-control inp", "placeholder": "Your Full Name"}
        )
    )
    Email_address = forms.EmailField(
        widget=forms.EmailInput(
            attrs={"class": "form-control inp", "placeholder": "name@example.com"}
        )
    )
    Organization_hosting_the_contest = forms.CharField(
        widget=forms.TextInput(attrs={"class": "form-control inp", "placeholder": ""})
    )
    Type_of_Organization = forms.CharField(
        widget=forms.Select(
            choices=tof,
            attrs={"class": "form-control inp", "placeholder": "Type_of_Organization"},
        )
    )
    Designation = forms.CharField(
        max_length=5280,
        widget=forms.TextInput(attrs={"class": "form-control inp", "placeholder": ""}),
    )
    Phone_no = forms.IntegerField(
        widget=forms.NumberInput(attrs={"class": "form-control inp", "placeholder": ""})
    )
    Purpose_of_Contest = forms.CharField(
        widget=forms.Textarea(attrs={"class": "form-control inp", "placeholder": ""})
    )
    Brief_detail_about_your_event = forms.CharField(
        widget=forms.Textarea(attrs={"class": "form-control inp", "placeholder": ""})
    )
    Theme_of_Project = forms.CharField(
        widget=forms.TextInput(attrs={"class": "form-control inp", "placeholder": ""})
    )
    Guidelines_for_submission = forms.CharField(
        widget=forms.Textarea(attrs={"class": "form-control inp", "placeholder": ""})
    )
    Eligibility_Creteria = forms.CharField(
        widget=forms.Select(
            choices=ef, attrs={"class": "form-control inp", "placeholder": ""}
        )
    )


class ParticipantForm(forms.Form):
    School_Name = forms.CharField(
        widget=forms.TextInput(
            attrs={"class": "form-control inp", "placeholder": "Enter your school name"}
        )
    )
    School_Phone_no = forms.IntegerField(
        widget=forms.NumberInput(
            attrs={
                "class": "form-control inp",
                "placeholder": "Enter your school phone no.",
            }
        )
    )
    School_Email_address = forms.CharField(
        widget=forms.EmailInput(
            attrs={"class": "form-control inp", "placeholder": "name@example.com"}
        )
    )
    School_Address = forms.CharField(
        widget=forms.Textarea(attrs={"class": "form-control inp", "placeholder": ""})
    )
    State = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control inp",
                "placeholder": "Enter your school address",
            }
        )
    )
    Student_Name = forms.IntegerField(
        widget=forms.TextInput(
            attrs={"class": "form-control inp", "placeholder": "Enter your name"}
        )
    )
    Contact_no = forms.CharField(
        widget=forms.NumberInput(
            attrs={"class": "form-control inp", "placeholder": "Enter your phone no."}
        )
    )
    Email_address = forms.CharField(
        widget=forms.EmailInput(
            attrs={"class": "form-control inp", "placeholder": "name@example.com"}
        )
    )
    House_Address = forms.CharField(
        widget=forms.Textarea(attrs={"class": "form-control inp", "placeholder": ""})
    )
    Gender = forms.CharField(
        widget=forms.Select(
            choices=g, attrs={"class": "form-control inp", "placeholder": ""}
        )
    )
    # Student_Name_2 = forms.IntegerField(
    #     widget=forms.TextInput(
    #         attrs={"class": "form-control inp", "placeholder": "Enter your name"}
    #     )
    # )
    # Contact_no = forms.CharField(
    #     widget=forms.NumberInput(
    #         attrs={"class": "form-control inp", "placeholder": "Enter your phone no."}
    #     )
    # )
    # Email_address = forms.CharField(
    #     widget=forms.EmailInput(
    #         attrs={"class": "form-control inp", "placeholder": "name@example.com"}
    #     )
    # )
    # House_Address = forms.CharField(
    #     widget=forms.Textarea(attrs={"class": "form-control inp", "placeholder": ""})
    # )
    # Gender = forms.CharField(
    #     widget=forms.Select(
    #         choices=g, attrs={"class": "form-control inp", "placeholder": ""}
    #     )
    # )
    Title_of_your_project = forms.CharField(
        widget=forms.TextInput(attrs={"class": "form-control inp", "placeholder": ""})
    )
    Question_or_Problem = forms.CharField(
        widget=forms.Textarea(attrs={"class": "form-control inp", "placeholder": ""})
    )
    Hypothesis_or_possible_solution = forms.CharField(
        widget=forms.TextInput(attrs={"class": "form-control inp", "placeholder": ""})
    )
    Materials_needed = forms.CharField(
        widget=forms.Textarea(attrs={"class": "form-control inp", "placeholder": ""})
    )
    Results = forms.CharField(
        widget=forms.TextInput(attrs={"class": "form-control inp", "placeholder": ""})
    )
    Image_of_Project = forms.ImageField(
        widget=forms.ClearableFileInput(
            attrs={"class": "form-control inp", "placeholder": ""}
        )
    )
    Link_of_your_project = forms.URLField(
        widget=forms.URLInput(attrs={"class": "form-control inp"})
    )
