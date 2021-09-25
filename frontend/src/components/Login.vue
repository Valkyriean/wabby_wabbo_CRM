<template>
  <body>
    <main class="login-form">
      <h2>Sign in to</h2>
      <h2>Wabby Wabbo CRM</h2>
      <a-form layout="inline" :form="form" @submit="handleSubmit">
        <a-row type="flex" justify="center" align="middle" :span="12">
          <a-form-item
            class="input"
            :validate-status="userNameError() ? 'error' : ''"
            :help="userNameError() || ''"
          >
            <a-input
              v-decorator="[
                'userName',
                {
                  rules: [
                    { required: true, message: 'Please input your username!' },
                  ],
                },
              ]"
              placeholder="Username"
            >
              <a-icon
                slot="prefix"
                type="user"
                style="color: rgba(0, 0, 0, 0.25)"
              />
            </a-input>
            <a-alert
              id="incorrectEmail"
              type="error"
              message="Incorrect email."
            />
          </a-form-item>
        </a-row>
        <a-row type="flex" justify="center" align="middle" :span="12">
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
                  ],
                },
              ]"
              type="password"
              placeholder="Password"
            >
              <a-icon
                slot="prefix"
                type="lock"
                style="color: rgba(0, 0, 0, 0.25)"
              />
            </a-input>
            <a-alert
              id="incorrectPassword"
              type="error"
              message="Incorrect password."
            />
          </a-form-item>
        </a-row>
        <a-row type="flex" justify="center" align="middle" :span="12">
          <a-form-item label="Remember me">
            <a-switch
              v-decorator="['rememberMe', { valuePropName: 'checked' }]"
              default-checked
              @change="getRememberMe"
            />
          </a-form-item>
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
function hasErrors(fieldsError) {
  return Object.keys(fieldsError).some((field) => fieldsError[field]);
}
export default {
  name: "Login",
  data() {
    return {
      hasErrors,
      form: this.$form.createForm(this, { name: "horizontal_login" }),
    };
  },
  mounted() {
    this.$nextTick(() => {
      // To disabled submit button at the beginning.
      this.form.validateFields();
    });
    var incorrectEmail = document.getElementById("incorrectEmail");
    var incorrectPassword = document.getElementById("incorrectPassword");
    incorrectEmail.style.display = "none";
    incorrectPassword.style.display = "none";
    if ("rememberMeToken" in localStorage) {
      window.location.href = "/app/dashboard";
    }
  },
  methods: {
    // Only show error after a field is touched.
    userNameError() {
      const { getFieldError, isFieldTouched } = this.form;
      return isFieldTouched("userName") && getFieldError("userName");
    },
    // Only show error after a field is touched.
    passwordError() {
      const { getFieldError, isFieldTouched } = this.form;
      return isFieldTouched("password") && getFieldError("password");
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
          .post("http://192.168.0.4:5000/auth/login", {
            email: values.userName,
            password: values.password,
            rememberMe: values.rememberMe,
          })
          .then((response) => {
            checkRes(response.data);
          });
      });
    },
  },
};
function checkRes(res) {
  var incorrectEmail = document.getElementById("incorrectEmail");
  var incorrectPassword = document.getElementById("incorrectPassword");
  incorrectEmail.style.display = "none";
  incorrectPassword.style.display = "none";
  if (res["status"] == "Success") {
    localStorage.setItem("rememberMeToken", res.jwt);
    window.location.href = "/app/dashboard";
  } else {
    if (res["status"] == "Incorrect email.") {
      incorrectEmail.style.display = "block";
    } else {
      incorrectPassword.style.display = "block";
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