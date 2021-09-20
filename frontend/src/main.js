import Vue from 'vue'
import App from './App.vue'
import VueRouter from 'vue-router'
import Antd from 'ant-design-vue';
import axios from 'axios';
import VueAxios from 'vue-axios';
import 'ant-design-vue/dist/antd.css';

Vue.use(VueRouter)
Vue.use(Antd)
Vue.use(VueAxios, axios)
Vue.config.productionTip = false

new Vue({
  render: h => h(App),
}).$mount('#app')
