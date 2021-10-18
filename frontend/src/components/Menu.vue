<template>
  <div>
 <!-- :default-selected-keys="['0']" -->
    <a-menu
      :open-keys.sync="openKeys"
      mode="inline"
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
      <a-sub-menu key="sub3" @titleClick="titleClick">
        <span slot="title"><a-icon type="cluster" /><span>Profile</span></span>
        <a-menu-item key="4" @click="changePassword"> Change Password </a-menu-item>
        <a-menu-item key="5" @click="logOut"> Log out </a-menu-item>
      </a-sub-menu>
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
      this.$router.push("/app/form");
    },
    clientsClick() {
      this.current = ["2"];
      this.$router.push("/app/clients");
    },
    createFormClick() {
      this.current = ["1"];
      this.$router.push("/app/form_create");
    },
    changePassword(){
      this.current = ["4"];
      this.$router.push("/app/change_password");
    },
  },
};
</script>
