<template>
    <a-form layout="horizontal">
        <a-form-item
            label="Old Password"
            :label-col="{span: 4}"
            :wrapper-col="{span: 14}"
        >
            <a-input placeholder="Please enter your old password" v-model="oldPassword" />
        </a-form-item>
        <a-form-item
            label="New Password"
            :label-col="{span: 4}"
            :wrapper-col="{span: 14}"
        >
            <a-input 
                id="password"
                v-decorator="[
                'password',
                {
                    rules: [
                    { required: true, message: 'Please input your Password!\n' },
                    {
                        validator: checkPasswordStrength,
                        message: 'Password too short.',
                    },
                    {
                        validator: checkPasswordLegality,
                        message: 'Password can only be letters and numbers.',
                    },
                    { validator: checkConfirmWhenChanged },
                    ],
                },
                ]"
                type="password"
                @change="recordPassword"
                placeholder="Please enter your new password" v-model="newPassword"/>
        </a-form-item>
        <a-form-item
            label="Confirm Password"
            :label-col="{span: 4}"
            :wrapper-col="{span: 14}"
        >
            <a-input 
                id="confirmpassword"
                v-decorator="[
                'confirmpassword',
                {
                    rules: [
                    { required: true, message: 'Please confirm your Password!' },
                    { validator: checkConfirmPassword },
                    ],
                },
                ]"
                type="password"
                @change="recordConfirmPassword"
                placeholder="Please enter your new password again" v-model="ConfirmPassword"/>
        </a-form-item>
        <a-form-item :wrapper-col="{span: 14, offset: 4}">
            <a-button type="primary" @click="submitClick">
                Submit
            </a-button>
        </a-form-item>
    </a-form>
</template>

<script>
function hasErrors(fieldsError) {
    return Object.keys(fieldsError).some((field) => fieldsError[field]);
}
export default {
    data() {
        return {
            hasErrors,
            form: this.$form.createForm(this, { name: "change_password" }),
            oldPassword,
            pwd: "",
            cpwd: "",
        }
    },
    
    methods: {
        submitClick() {
            e.preventDefault();
            this.form.validateFields((err, values) => {
                if (!err) {
                console.log("Received values of form: ", values);
                }
                values.rememberMe = false;
                this.axios
                .post("https://wabby-wabbo-crm.herokuapp.com/auth/changepass", {
                    jwt: localStorage.getItem('rememberMeToken'),
                    password: values.oldPassword,
                    new_password: values.pwd,
                })
                .then((response) => {
                    checkRes(response.data);
                });
            });
        },
        // Only show error after a field is touched.
        emailError() {
        const { getFieldError, isFieldTouched } = this.form;
        return isFieldTouched("email") && getFieldError("email");
        },
        // Only show error after a field is touched.
        passwordError() {
        const { getFieldError, isFieldTouched } = this.form;
        return isFieldTouched("password") && getFieldError("password");
        },
        confirmpasswordError() {
        const { getFieldError, isFieldTouched } = this.form;
        return (
            isFieldTouched("confirmpassword") && getFieldError("confirmpassword")
        );
        },
        getRememberMe(checked) {
        console.log(`Remember me switch to ${checked}`);
        },
        recordPassword(e) {
        this.pwd = e.target.value;
        },
        recordConfirmPassword(e) {
        this.cpwd = e.target.value;
        },
        checkPasswordStrength() {
        const strongPassword = new RegExp("(?=.{6,})");
        return this.pwd != "" && strongPassword.test(this.pwd);
        },
        checkPasswordLegality() {
        const strongPassword = new RegExp("(?=.{6,})");
        const legalPassword = new RegExp("^[a-zA-Z0-9]+$");
        return !strongPassword.test(this.pwd) || legalPassword.test(this.pwd);
        },
        checkConfirmWhenChanged(rule, value, callback) {
        const form = this.form;
        if (value) {
            form.validateFields(["confirmpassword"], { force: true });
        }
        callback();
        },
        checkConfirmPassword(rule, value, callback) {
        const form = this.form;
        if (value && value !== form.getFieldValue("password")) {
            callback("Two passwords that you enter is inconsistent!");
        } else {
            callback();
        }
    },
    
  },
  
}
function checkRes(res) {
  //
}
</script>