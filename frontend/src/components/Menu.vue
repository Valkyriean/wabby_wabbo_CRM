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
      <a-sub-menu key="sub2" @titleClick="titleClick">
        <span slot="title"><a-icon type="crown" /><span>Profile</span></span>
        <a-menu-item key="1"> General </a-menu-item>
        <a-menu-item key="2"> Security </a-menu-item>
      </a-sub-menu>
      <a-sub-menu key="sub3" @titleClick="titleClick">
        <span slot="title"><a-icon type="cluster" /><span>Database</span></span>
        <a-menu-item key="4"> View Database </a-menu-item>
        <a-menu-item key="5"> Create Form </a-menu-item>
        <a-menu-item key="6"> View Forms </a-menu-item>
      </a-sub-menu>
      <a-menu-item key="8">
        <a-icon type="build" />
        <span @click="clientsClick">Clients</span>
      </a-menu-item>
      <a-menu-item key="7" @click="logOut()">
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
      window.location.href = "/";
    },
    dashboardClick() {
      this.current = ["0"];
      window.location.href = "/app/dashboard";
    },
    clientsClick() {
      this.current = ["8"];
      window.location.href = "/app/clients";
    }
  },
};
</script>
