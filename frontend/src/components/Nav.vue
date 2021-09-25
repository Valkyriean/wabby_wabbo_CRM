<template>
  <div>
    <a-menu v-model="current" mode="horizontal">
      <a-menu-item key="Login">
        <a target="_self" href="/app/login" rel="noopener noreferrer"
          >Login</a
        >
      </a-menu-item>
      <a-menu-item key="register">
        <a target="_self" href="/app/register" rel="noopener noreferrer"
          >Register</a
        >
      </a-menu-item>
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
