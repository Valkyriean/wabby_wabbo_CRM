<template>
  <a-layout id="dashBoard">
    <a-layout-sider>
      <Menu />
    </a-layout-sider>

    <!-- <Login /> -->
    <a-layout-content>
      <List class="list-content"/>
    </a-layout-content>
  </a-layout>
</template>

<script>
import Menu from "./Menu.vue";
import List from "./Form.vue";

export default {
  name: "App",
  components: {
    Menu,
    List,
  },
};
</script>
<style scoped>
  #dashBoard {
    height: 100%;
  }
  #dashboard .logo {
    height: 10%;
    color: lightblue;
    margin: 16px;
  }
  .list-content {
    margin: 60px;
  }
</style>