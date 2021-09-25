<template>
  <div>
    <a-menu v-model="current" mode="horizontal">
      <a-menu-item key="Customers" disabled> <a-icon type="mail" />View Customers </a-menu-item>
      <a-menu-item key="Forms" disabled> <a-icon type="appstore" />View Forms </a-menu-item>
    </a-menu>
  </div>
</template>

<script>
export default {
  data() {
    return {
      current: ['mail'],
    };
  },
};
</script>
