<template>
  <a-layout id="dashBoard">

    <a-layout-sider style="background: #6495f2">
      <div class="logo">
        <img
          src="../assets/logo.png"
          alt=""
          style="width: 150px; height: 150px; margin: 15px; margin-left: 23px;"
        />
      </div>

      <Menu />

    </a-layout-sider>

    <!-- <Login /> -->
    <a-layout-content>

      <List class="list-content"/>
                    <DashboardBar />

    </a-layout-content>
  </a-layout>
</template>

<script>
import Menu from "./Menu.vue";
import DashboardBar from "./DashboardBar.vue";
import List from "./Form.vue";

export default {
  name: "App",
  components: {
    Menu,
    DashboardBar,
    List,
  },
};
</script>
<style scoped>
  #dashBoard {
    height: 100%;
  }
  .list-content {
    margin: 60px;
  }
</style>