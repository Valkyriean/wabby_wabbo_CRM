<template>
  <div>
 <!-- :default-selected-keys="['0']" -->
    <a-menu

     
      :open-keys.sync="openKeys"
      mode="inline"
      @click="handleClick"
    >
      <a-menu-item key="0" @click="dashboardClick">
        <a-icon type="home" />
        <span >Dashboard</span>
      </a-menu-item>
      <a-menu-item key="1" @click="createFormClick">
        <a-icon type="crown" />
        <span >Create Form</span>
      </a-menu-item>
      <a-menu-item key="2" @click="clientsClick">
        <a-icon type="build" />
        <span>Clients</span>
      </a-menu-item>
      <a-menu-item key="3" @click="logOut">
        <a-icon type="import" />
        <span>Log out</span>
      </a-menu-item>
    </a-menu>
  </div>
</template>
<script>
export default {
  data() {
    return {
      current: [],
      openKeys: [],
    };
  },
  watch: {
    openKeys(val) {
      console.log("openKeys", val);
    },
  },
  methods: {
    handleClick(e) {
      console.log("click", e);
    },
    titleClick(e) {
      console.log("titleClick", e);
    },
    logOut() {
      if ("rememberMeToken" in localStorage) localStorage.removeItem("rememberMeToken");
      this.$router.push("/");
    },
    dashboardClick() {
      this.current = ["0"];
      this.$router.push("/app/dashboard");
    },
    clientsClick() {
      this.current = ["8"];
      window.location.href = "/app/clients";
    },
    createFormClick() {
      window.location.href = "/app/form_create";
    },
  },
};
</script>
