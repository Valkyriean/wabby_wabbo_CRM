<template>
  <body>
    <Nav />
    <main class="register-form">
      <h2>Sign up for</h2>
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
              message="Email unavilable."
            />
          </a-form-item>
        </a-row>

        <a-row type="flex" justify="center" align="middle" :span="12">
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
                    { required: true, message: 'Please input your Password!' },
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
          <a-alert
            id="passwordInstruction"
            type="error"
            message="Password should countain at least a letter, a number, and over 8 chars in length"
          />
        </a-row>
        <a-row type="flex" justify="center" align="middle" :span="12">
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
                    {
                      required: true,
                      message: 'Please confirm your Password!',
                    },
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
          <a-alert
            id="passwordConInstruction"
            type="error"
            message="Two password are different."
          />
        </a-row>
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
    this.$nextTick(() => {
      // To disabled submit button at the beginning.
      this.form.validateFields();
    });
    var incEmail = document.getElementById("incorrectEmail");
    var pswIns = document.getElementById("passwordInstruction");
    var pswConIns = document.getElementById("passwordConInstruction");
    incEmail.style.display = "none";
    pswIns.style.display = "none";
    pswConIns.style.display = "none";
    if ("rememberMeToken" in localStorage) localStorage.removeItem("rememberMeToken");
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
          .post("/auth/register", {
            email: values.userName,
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
      this.checkPassword();
    },
    recordConfirmPassword(e) {
      this.cpwd = e.target.value;
      this.checkPassword();
    },
    checkPassword() {
      const { isFieldTouched } = this.form;
      const strongPassword = new RegExp("(?=.*[a-zA-Z])(?=.*[0-9])(?=.{8,})");
      var pswIns = document.getElementById("passwordInstruction");
      var pswConIns = document.getElementById("passwordConInstruction");
      var flag = false;
      if (strongPassword.test(this.pwd)) {
        // password strong enough
        pswIns.style.display = "none";
        flag = true;
      } else {
        pswIns.style.display = "block";
        flag = false;
      }
      if (this.cpwd == this.pwd) {
        // password same
        pswConIns.style.display = "none";
        flag = true;
      } else {
        if (isFieldTouched("confirmpassword")) pswConIns.style.display = "block";
        flag = false;
      }
      return flag;
    },
  },
};

function checkRes(res) {
  var incorrectEmail = document.getElementById("incorrectEmail");
  var incorrectPassword = document.getElementById("passwordInstruction");
  var incorrectConfirmPassword = document.getElementById("passwordConInstruction");
  incorrectEmail.style.display = "none";
  incorrectPassword.style.display = "none";
  incorrectConfirmPassword.style.display = "none";
  console.log(res["status"]);
  if (res["status"] == "Success") {
    localStorage.setItem("rememberMeToken", res.jwt);
    window.location.href = "/app/dashboard";
  } else {
    if (res["status"] == "Email already registered.") {
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