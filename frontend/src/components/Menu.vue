<template>
  <div>
    <a-menu

      :default-selected-keys="['1']"
      :open-keys.sync="openKeys"
      mode="inline"
      @click="handleClick"
    >
      <a-menu-item key="0">
        <a-icon type="home" />
        <span @click="dashboardClick">Dashboard</span>
      </a-menu-item>
      <a-menu-item key="1">
        <a-icon type="crown" />
        <span @click="createFormClick">Create Form</span>
      </a-menu-item>
      <a-menu-item key="2">
        <a-icon type="build" />
        <span @click="clientsClick">Clients</span>
      </a-menu-item>
      <a-menu-item key="3" @click="logOut()">
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
