import { createStore } from 'vuex'
import axios from 'axios'


export default createStore({
  state: {
    status: '',
    user: {
      id: null,
      telegram_id: null,
      email: null,
      phone: null,
      token: null,
      telegram_name: null,
      registration_data: null,
      subscribe_status: '',
      is_active: false,
    },
  },
  getters: {
    GET_STATUS: state => {
      return state.status
    },
    GET_USER: state => {
      return state.user
    },
 
  },

  mutations: {
    SET_STATUS: (state, status) => {
      state.status = status
    },
    SET_STATUS_DEFAULT: (state) => {
      state.status = ''
    },
    SET_USER: (state, data) => {
      state.user.id = data.id
      state.user.telegram_id = data.telegram_id
      state.user.email = data.email
      state.user.phone = data.phone
      state.user.token = data.token
      state.user.telegram_name = data.telegram_name
      state.user.registration_data = data.registration_data
      state.user.subscribe_status = data.subscribe_status
      state.user.is_active = data.is_active
    },
    SET_USER_DEFAULT: (state) => {
      state.user.id = null
      state.user.telegram_id = null
      state.user.email = null
      state.user.phone = null
      state.user.token = null
      state.user.telegram_name = null
      state.user.registration_data = null
      state.user.subscribe_status = ''
      state.user.is_active = false
    },

  },
  actions: {
    SET_ACCOUNT: async (context, account) => {
      await axios.post("http://localhost:8000/auth/users/", account).then(function (response) {
        if (response.status == 201) {
          context.commit('SET_STATUS', 'Аккаунт успешно создан!')
        } 
      }).catch(function (error) {
        console.log(error)
        context.commit('SET_STATUS', 'Аккаунт уже сущесвтует или пароль слишком расспространён!')
      })  
    },
    LOGIN: async (context, account) => {
      await axios.post("http://localhost:8000/auth/token/login", account).then(function (response) {
        if (response.status == 200) {
          context.commit('SET_STATUS', 'Перенаправление в личный кабинет...')
          let token = response.data.auth_token
          axios.get("http://localhost:8000/auth/users/me", {
                headers: {"Authorization": `token ${token}`},
                data: {
                    username: account.username,
                    password: account.password
                }
          }).then(function (response) {
            let id = response.data.id;
            let telegram_id = response.data.username;
            let email = response.data.email;
            let phone = response.data.phone;
            axios.get(`http://localhost:8000/api/subscribers/${telegram_id}/get_detail_info/`,{
                headers: {"Authorization": `token ${token}`},
                data: {
                    username: account.username,
                    password: account.password
                }
            }).then(function (response) {
            let telegram_name = response.data.name;
            let registration_data = response.data.data.slice(0,10);
            let subscribe_status = response.data.status;
            context.commit('SET_USER', {
              'id': id,
              'telegram_id': telegram_id,
              'email': email,
              'phone': phone,
              'token': token,
              'telegram_name': telegram_name,
              'registration_data': registration_data,
              'subscribe_status': subscribe_status,
              'is_active': true
            })
          })
          })
        } 
      }).catch(function (error) {
        console.log(error)
        context.commit('SET_STATUS', 'Неправильный логин или пароль')
      })
    },
    LOGOUT: async (context, token) => {
      // c axios.post почему-то не работает
      await axios({
        method: 'POST',
        url: "http://localhost:8000/auth/token/logout",
        headers: {"Authorization": "token " + token}
      }).then(function (response) {
        if (response.status == 204) {
          context.commit('SET_USER_DEFAULT')
          context.commit('SET_STATUS_DEFAULT')
          }}).catch(function (error) {
        console.log(error)
      })
    }
  },
})
