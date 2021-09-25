import Vue from 'vue/dist/vue.js';

import VueRouter from 'vue-router';
import Antd from 'ant-design-vue';
import axios from 'axios';
import VueAxios from 'vue-axios';
import 'ant-design-vue/dist/antd.css';

import App from './App.vue';
import Login from './components/Login.vue'
import Register from './components/Register.vue'

Vue.use(VueRouter)
Vue.use(Antd)
Vue.use(VueAxios, axios)
Vue.config.productionTip = false

// const routes = [
//   {path: '/', component: App},
//   {path: '/app/login', component: Login}
// ]

// const router = new VueRouter({
//   routes
// })
const routes = {
  '/': App,
  '/app/login': Login,
  '/app/register' : Register
}

new Vue({
  el: '#app',
  data: {
    currentRoute: window.location.pathname
  },
  computed: {
    ViewComponent () {
      return routes[this.currentRoute] || App
    }
  },
  render (h) { return h(this.ViewComponent) }
  // router,
  // render: h => h(Login),
})
