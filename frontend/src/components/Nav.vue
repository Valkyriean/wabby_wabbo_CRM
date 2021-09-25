<template>
  <div>
    <div class="top">
      <div class="t_logo">
        <img src="../assets/logo.png" alt="" style="width:110px; height:110px;"/>
      </div>
      <div class="t_contain">
        <div class="contain_center">
          <div class="title_tag">Login</div>
          <div class="title_tag">Register</div>
        </div>
      </div>
    </div>

  </div>

</template>

<script>

    // <a-menu v-model="current" mode="horizontal">
    //   <a-menu-item key="Login">
    //     <a target="_self" href="/app/login" rel="noopener noreferrer"
    //       >Login</a
    //     >
    //   </a-menu-item>
    //   <a-menu-item key="register">
    //     <a target="_self" href="/app/register" rel="noopener noreferrer"
    //       >Register</a
    //     >
    //   </a-menu-item>
    // </a-menu>


export default {
  data() {
    return {
      current: ['mail'],
    };
  },
};
</script>

<style scoped>
.top {
  width: 100%;
  height: 100px;
  border: 1px solid white;
  box-sizing: border-box;
  /* background-image: url(../assets/顶部背景.jpg); */
  background: white;
  position: fixed;
  top: 0%;
  box-shadow: 2px 2px 2px black;
  z-index: 100;
}
.t_logo {
  width: 10%;
  height: 130px;
  margin-top: -0.5%;
  font-size: 2.5rem;
  margin-left: 12%;
  color: #fff;
  position: relative;
  left: -8%;
}
.t_contain {
  width: 100%;
  /* height:10%; */
  height: 45px;
  /* border:0px solid red; */
  margin-top: -1%;
  margin-bottom: 1%;
  /* background:#161616; */
  opacity: 0.8;
  box-sizing: border-box;
  /* background:#111B25; */
  position: relative;
  top: -77%;
  left: 8%;
  background-color: rgba(0, 0, 0, 0);
  overflow-x: hidden;
}

.contain_center {
  width: 80%;
  height: 45px;
  /* line-height: 2.5rem; */
  margin: 0 auto;
  text-align: center;
}
.title_tag {
  width: 16.43%;
  height: 30px;
  border: 0px solid orange;
  float: left;
  cursor: pointer;
  margin-top: 0.7%;
  font-size: 1rem;
  color: black;
  text-align: center;
  line-height: 30px;
}
.title_tag:nth-child(2),
:nth-child(3),
:nth-child(4),
:nth-child(5),
:nth-child(6) {
  border-left: 2px solid #787878;
}
.title_tag:hover {
  color: gray;
}
</style>