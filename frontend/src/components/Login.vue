<template>
  <body>
    <Nav />
    <main class="login-form">
      <h2>Sign in to</h2>
      <h2>Wabby Wabbo CRM</h2>
      <a-alert
        id="emailWrong"
        type="error"
        message="The email does not exist."
      />
      <a-alert
        id="passwordWrong"
        type="error"
        message="The password is wrong."
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
                  { required: true, message: 'Please input your email!' },
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
            v-decorator="[
              'password',
              {
                rules: [
                  { required: true, message: 'Please input your Password!' },
                  {
                    validator: checkPasswordLegality,
                    message: 'Password invalid.',
                  },
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

        <a-row type="flex" justify="center" align="middle" :span="12">
          <h3 style="padding-right:20px;">Remember me:</h3>
          <a-switch
            v-decorator="['rememberMe', { valuePropName: 'checked' }]"
            default-checked
            @change="getRememberMe"
          />
        </a-row>

        <a-row type="flex" justify="center" align="middle" :span="12">
          <a-form-item>
            <a-button
              type="primary"
              html-type="submit"
              :disabled="hasErrors(form.getFieldsError())"
            >
              Log in
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
  name: "Login",
  components: {
    Nav,
  },
  data() {
    return {
      hasErrors,
      form: this.$form.createForm(this, { name: "horizontal_login" }),
      pwd: "",
      rememberMe:true,
    };
  },
  mounted() {
    var emailWrong = document.getElementById("emailWrong");
    emailWrong.style.display = "none";
    var passwordWrong = document.getElementById("passwordWrong");
    passwordWrong.style.display = "none";
    this.$nextTick(() => {
      // To disabled submit button at the beginning.
      this.form.validateFields();
    });
    if ("rememberMeToken" in localStorage) {
      window.location.href = "/app/dashboard";
    }
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
    getRememberMe(checked) {
      this.rememberMe = checked;
      console.log(`Remember me switch to ${checked}`);
    },
    recordPassword(e) {
      this.pwd = e.target.value;
    },
    handleSubmit(e) {
      e.preventDefault();
      this.form.validateFields((err, values) => {
        if (!err) {
          console.log("Received values of form: ", values);
        }
        console.log("hello");
        this.axios
          .post("https://wabby-wabbo-crm.herokuapp.com/auth/login", {
            email: values.email,
            password: values.password,
            rememberMe: this.rememberMe,
          })
          .then((response) => {
            checkRes(response.data);
          });
      });
    },
    checkPasswordLegality() {
      const legalPassword = new RegExp("^[a-zA-Z0-9]+$");
      return legalPassword.test(this.pwd);
    },
  },
};
function checkRes(res) {
  var emailWrong = document.getElementById("emailWrong");
  emailWrong.style.display = "none";
  var passwordWrong = document.getElementById("passwordWrong");
  passwordWrong.style.display = "none";
  if (res["status"] == "Success") {
    localStorage.setItem("rememberMeToken", res.jwt);
    window.location.href = "/app/dashboard";
  } else {
    if (res["status"] == "Incorrect email.") {
      emailWrong.style.display = "block";
    } else {
      passwordWrong.style.display = "block";
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

.login-form {
  width: 100%;
  max-width: 330px;
  padding: 15px;
  margin: auto;
}

h2 {
  text-align: center;
}
</style>