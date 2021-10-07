<template>
  <body>
    <Nav />

    <main class="register-form">
      <h2>Sign up for</h2>
      <h2>Wabby Wabbo CRM</h2>
      <a-alert
        id="emailNotAvailable"
        type="error"
        message="The email is not available."
      />
      <a-form layout="formLayout" :form="form" @submit="handleSubmit">
        <a-form-item
          class="input"
          :validate-status="emailError() ? 'error' : ''"
          :help="emailError() || ''"
        >
          <a-input
            v-decorator="[
              'email',
              {
                rules: [
                  { type: 'email', message: 'The input is not valid E-mail!' },
                  { required: true, message: 'Please input your Email!' },
                ],
              },
            ]"
            placeholder="Email"
          >
            <a-icon
              slot="prefix"
              type="user"
              style="color: rgba(0, 0, 0, 0.25)"
            />
          </a-input>
        </a-form-item>

        <a-form-item
          :validate-status="passwordError() ? 'error' : ''"
          :help="passwordError() || ''"
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
            placeholder="Password"
            @change="recordPassword"
          >
            <a-icon
              slot="prefix"
              type="lock"
              style="color: rgba(0, 0, 0, 0.25)"
            />
          </a-input>
        </a-form-item>

        <a-form-item
          :validate-status="confirmpasswordError() ? 'error' : ''"
          :help="confirmpasswordError() || ''"
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
            placeholder="Confirm password"
            @change="recordConfirmPassword"
          >
            <a-icon
              slot="prefix"
              type="lock"
              style="color: rgba(0, 0, 0, 0.25)"
            />
          </a-input>
        </a-form-item>

        <a-row type="flex" justify="center" align="middle" :span="12">
          <a-form-item>
            <a-button
              id="btnSubmit"
              type="primary"
              html-type="submit"
              :disabled="hasErrors(form.getFieldsError())"
            >
              Register
            </a-button>
          </a-form-item>
        </a-row>
      </a-form>
    </main>
  </body>
</template>

<script>
import Nav from "./Nav.vue";
function hasErrors(fieldsError) {
  return Object.keys(fieldsError).some((field) => fieldsError[field]);
}
export default {
  name: "Register",
  components: {
    Nav,
  },
  data() {
    return {
      hasErrors,
      form: this.$form.createForm(this, { name: "horizontal_register" }),
      pwd: "",
      cpwd: "",
    };
  },
  mounted() {
    var emailNotAvailable = document.getElementById("emailNotAvailable");
    emailNotAvailable.style.display = "none";
    this.$nextTick(() => {
      // To disabled submit button at the beginning.
      this.form.validateFields();
    });
    if ("rememberMeToken" in localStorage)
      localStorage.removeItem("rememberMeToken");
  },
  computed: {
    formItemLayout() {
      const { formLayout } = this;
      return formLayout === "horizontal"
        ? {
            labelCol: { span: 4 },
            wrapperCol: { span: 14 },
          }
        : {};
    },
    buttonItemLayout() {
      const { formLayout } = this;
      return formLayout === "horizontal"
        ? {
            wrapperCol: { span: 14, offset: 4 },
          }
        : {};
    },
  },
  methods: {
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
    handleSubmit(e) {
      e.preventDefault();
      this.form.validateFields((err, values) => {
        if (!err) {
          console.log("Received values of form: ", values);
        }
        console.log("hello");
        values.rememberMe = false;
        this.axios
          .post("https://wabby-wabbo-crm.herokuapp.com/auth/register", {
            email: values.email,
            password: values.password,
            rememberMe: values.rememberMe,
          })
          .then((response) => {
            checkRes(response.data);
          });
      });
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
};

function checkRes(res) {
  var emailNotAvailable = document.getElementById("emailNotAvailable");
  emailNotAvailable.style.display = "none";
  console.log(res["status"]);
  if (res["status"] == "Success") {
    localStorage.setItem("rememberMeToken", res.jwt);
    window.location.href = "/app/dashboard";
  } else {
    if (res["status"] == "Email already registered.") {
      emailNotAvailable.style.display = "block";
    } else {
      console.log("something went wrong");
    }
  }
}
</script>

<style scoped>
body {
  display: flex;
  align-items: center;
  padding-top: 40px;
  padding-bottom: 40px;
  background-color: #f5f5f5;
}

.register-form {
  width: 100%;
  max-width: 330px;
  padding: 15px;
  margin: auto;
}

h2 {
  text-align: center;
}
</style>