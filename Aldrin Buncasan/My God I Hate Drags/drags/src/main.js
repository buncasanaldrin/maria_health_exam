import Vue from 'vue'
import BootstrapVue from 'bootstrap-vue'
import store from '../store'

import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'

import App from './App.vue'

Vue.use(BootstrapVue)
Vue.config.productionTip = false


new Vue({
  render: h => h(App),
  store,
}).$mount('#app')
