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
      email: null,
      phone: null,
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
      return state.user
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
    SET_USER_INFO: (state, data) => {
      state.user.id = data.id,
      state.user.username = data.username,
      state.user.email = data.email,
      state.user.phone = data.phone,
      state.user.token = data.token
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
        if (response.status == 200) {
          let token = response.data.auth_token
          axios.get("http://localhost:8000/auth/users/me", {
                headers: {"Authorization": "token " + token},
                data: {
                    username: account.username,
                    password: account.password
                }
          }).then(function (response) {
            let id = response.data.id;
            let username = response.data.username;
            let email = response.data.email;
            let phone = response.data.phone;
            context.commit('SET_USER_INFO', {
              'id': id,
              'username': username,
              'email': email,
              'phone': phone,
              'token': token
            })
          }).catch(function (error) {
            console.log(error)
          })
        }
      })
    },
  },
  modules: {
  }
})
