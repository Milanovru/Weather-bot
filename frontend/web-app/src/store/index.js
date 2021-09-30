import { createStore } from 'vuex'
import axios from 'axios'


export default createStore({
  state: {
    account: {
      username: null,
      password: null,
    },
    status: '',
    user: {
      id: null,
      username: null,
      token: null,
    }
  },
  getters: {
    GET_ACCOUNT: state => {
      return state.account
    },
    GET_STATUS: state => {
      return state.status
    },
    GET_USER: state => {
      return state.user.token
    },
  },

  mutations: {
    SET_ACCOUNT: (state, account) => {
      state.account.username = account.username;
      state.account.password = account.password;
    },
    SET_STATUS: (state, status) => {
      state.status = 'пользователь ' + status + ' создан успешно!';
    },
    SET_USER_TOKEN: (state, data) => {
      state.user.token = data
    }
  },

  actions: {
    SET_ACCOUNT: async (context, account) => {
      await axios.post("http://localhost:8000/auth/users/", account).then(function (response) {
        if (response.status == 201) {
          context.commit('SET_ACCOUNT', account)
          context.commit('SET_STATUS', account.username)
        }
      }).catch(function (error) {
        console.log(error)
      })  
    },
    LOGIN: async (context, account) => {
      await axios.post("http://localhost:8000/auth/token/login/", account).then(function (response) {
        console.log(response)
        if (response.status == 200) {
          context.commit("SET_USER_TOKEN", response.data.auth_token)
        }
      })
    }
  },
  modules: {
  }
})
