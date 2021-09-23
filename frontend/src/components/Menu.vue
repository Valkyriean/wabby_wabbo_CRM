<template>
  <div>
    <a-menu
      style="width: 256px"
      :default-selected-keys="['1']"
      :open-keys.sync="openKeys"
      mode="inline"
      @click="handleClick"
    >
      <a-sub-menu key="sub1">
        <span slot="title"><a-icon type="home" /><span>Homepage</span></span>
      </a-sub-menu>
      <a-sub-menu key="sub2" @titleClick="titleClick">
        <span slot="title"><a-icon type="crown" /><span>Profile</span></span>
          <a-menu-item key="1">
            General
          </a-menu-item>
          <a-menu-item key="2">
            Security
          </a-menu-item>
          <a-menu-item key="3">
            Log out
          </a-menu-item>
      </a-sub-menu>
      <a-sub-menu key="sub3" @titleClick="titleClick">
        <span slot="title"><a-icon type="cluster" /><span>Database</span></span>
        <a-menu-item key="4">
          View Database
        </a-menu-item>
        <a-menu-item key="5">
          Create Form
        </a-menu-item>
        <a-menu-item key="6">
          View Forms
        </a-menu-item>
      </a-sub-menu>
    </a-menu>
  </div>
</template>
<script>
export default {
  data() {
    return {
      current: ['mail'],
      openKeys: ['sub1'],
    };
  },
  watch: {
    openKeys(val) {
      console.log('openKeys', val);
    },
  },
  methods: {
    handleClick(e) {
      console.log('click', e);
    },
    titleClick(e) {
      console.log('titleClick', e);
    },
  },
};
</script>
