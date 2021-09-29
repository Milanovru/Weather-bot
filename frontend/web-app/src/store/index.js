import { createStore } from 'vuex'
import axios from 'axios'


export default createStore({
  state: {
    account: {
      username: null,
      password: null,
    },
  },
  getters: {
    GET_ACCOUNT: state => {
      return state.account
    }
  },
  mutations: {
    SET_ACCOUNT: (state, account) => {
      state.account.username = account.username;
      state.account.password = account.password;
    },
  },
  actions: {
    SET_ACCOUNT: (context, account) => {
      let responce = axios.post("http://localhost:8000/auth/users/", account)
      console.log(responce.status)
      context.commit('SET_ACCOUNT', account)   
    },
  },
  modules: {
  }
})
