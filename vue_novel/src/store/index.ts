import Vue from 'vue'
import Vuex from 'vuex'
Vue.use(Vuex)

export default new Vuex.Store({
  strict:true,  // 开启严格模式  确保state 中的数据只能 mutations 修改 不开启就可以随便修改
  state: {
    book_infos: [],
    book_name: '',
  },
  mutations: {
    changeBookInfo(state, books){
      state.book_infos = books
    },
    changeBookName(state, book_name){
      state.book_name = book_name
    }
  },
  actions: {
  },
  modules: {
  }
})
