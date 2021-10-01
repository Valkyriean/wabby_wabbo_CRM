<template>
  <div id="dashBoard">
    <Menu />

    <!-- <Login /> -->
    <List />
  </div>
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