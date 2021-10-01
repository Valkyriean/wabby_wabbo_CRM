<template>
  <div id="dashBoard">
    <Menu />

    <!-- <Login /> -->
    <List />
  </div>
</template>

<script>
import Menu from "./Menu.vue";
import List from "./List.vue";

export default {
  name: "App",
  components: {
    Menu,
    List,
  },
};
</script>