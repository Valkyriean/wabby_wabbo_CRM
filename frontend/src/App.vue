<template>
  <div id="app">
    <Nav />
    <div class="place-holder"/>
    <Carousel />
    <img alt="Vue logo" src="./assets/logo.png" style="width:300px; height:300px;">
    
    <!-- <Login /> -->
  </div>
</template>

<script>
// import HelloWorld from './components/HelloWorld.vue'
// import Login from './components/Login.vue'
import Nav from './components/Nav.vue'
import Carousel from './components/Carousel.vue'

export default {
  name: 'App',
  components: {
    Nav,
    Carousel,
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}
.place-holder {
  height: 100px;
}
</style>
