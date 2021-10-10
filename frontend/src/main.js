import Vue from 'vue/dist/vue.js';

import VueRouter from 'vue-router';
import Antd from 'ant-design-vue';
import axios from 'axios';
import VueAxios from 'vue-axios';
import 'ant-design-vue/dist/antd.css';

import App from './App.vue';
import Login from './components/Login.vue';
import Register from './components/Register.vue';
import Dashboard from './components/Dashboard.vue';
import Record from './components/Record.vue';
import Spread from './components/Spread.vue';
import Clients from './components/Clients.vue';
import CreateForm from './components/CreateForm.vue';
import CustomerResponse from './components/CustomerResponse.vue';
import Main from './components/Main.vue';

Vue.use(VueRouter);
Vue.use(Antd);
Vue.use(VueAxios, axios);
Vue.config.productionTip = false;

// const routes = [
//   {path: '/', component: App},
//   {path: '/app/login', component: Login}
// ]

// const router = new VueRouter({
//   routes
// })

var router = new VueRouter({
  mode: "history",
  routes: [
    {
      path: '/',
      component: Main,
    },
    {
      path: '/app/login',
      component: Login,
    },
    {
      path: '/app/register',
      component: Register,
    },
    {
      path: '/app/dashboard',
      component: Dashboard,
    },
    {
      path: '/app/record',
      component: Record,
    },
    {
      path: '/app/customer',
      component: Spread,
    },
    {
      path: '/app/clients',
      component: Clients,
    },
    {
      path: '/app/form_create',
      component: CreateForm
    },
    {
      path: '/app/form/:id',
      component: CustomerResponse,
    }
  ]
});

// const routes = {
//   '/': App,
//   '/app/login': Login,
//   '/app/register': Register,
//   '/app/dashboard': Dashboard,
//   '/app/record': Record,
//   '/app/customer': Spread,
//   '/app/clients': Clients,
//   '/app/form_create': CreateForm,
// };

new Vue({
  // el: '#app',
  // data: {
  //   currentRoute: window.location.pathname
  // },
  // computed: {
  //   ViewComponent () {
  //     return routes[this.currentRoute] || App
  //   }
  // },
  router,
  // render (h) { return h(this.ViewComponent) }
  // router,
  render: h => h(App),
}).$mount('#app');