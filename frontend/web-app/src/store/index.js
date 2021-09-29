import { createStore } from 'vuex'
import axios from 'axios'


export default createStore({
  state: {
    account: {
      username: null,
      password: null,
    },
    status: null
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
    SET_STATUS: (state, status) => {
      state.status = status;
    }
  },
  actions: {
    SET_ACCOUNT: async (context, account) => {
      await axios.post("http://localhost:8000/auth/users/", account).then(function (response) {
        if (response.status == 201) {
          context.commit('SET_ACCOUNT', account)
          context.commit('SET_STATUS', response.statusText)
        }
      }).catch(function (error) {
        console.log(error)
      })  
    },
  },
  modules: {
  }
})
