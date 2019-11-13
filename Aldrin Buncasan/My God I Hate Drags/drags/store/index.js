import Vue from 'vue'
import Vuex from 'vuex'


import drugs from './drugs'

Vue.use(Vuex)

const createStore = () => {
  return new Vuex.Store({
    namespaced: true,
    modules: {
      drugs
    }
  })
}

export default createStore
