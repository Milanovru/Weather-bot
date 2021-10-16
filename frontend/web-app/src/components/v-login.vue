<template>
    <div class="form">
        <label>{{this.$store.getters.GET_STATUS}}</label>
        <input 
            v-model.lazy="account.username" 
            type='text' 
            placeholder="Введите логин" 
            class="form-item item1" 
            :class="{alert: isAlert}"
            @click="hidden_alert()"
            />
        <input v-model.lazy="account.password" 
            type='password' 
            placeholder="Введите пароль" 
            class="form-item item1" 
            :class="{alert: isAlert}"
            @click="hidden_alert()"
        />
        <button @click="login()" class="btn btn-submit">
            Submit
        </button>   
        <button @click="create_account()" class="btn btn-register">
            Registration
        </button>             
    </div>
</template>

<script>
export default {
    data () {
        return {
            account: {
                username: null,
                password: null,
            },
            label: null,
            isAlert: false,
        }
    },
    methods: {
        login () {
            if (this.account.username == null || this.account.password == null) {
                this.display_alert('Поля логина и пароля не могут быть пустыми!')
            } else if (this.account.username == /[0-9]{10}/) {
                this.$store.dispatch("LOGIN", this.account)
                this.clear_input()
                setTimeout(this.redirect_to_office, 2000)
            } else {
                this.display_alert('Неправильный формат логина или пароля!')
            }
        },
        create_account () {
            if (this.account.username == null || this.account.password == null) {
                this.display_alert('Поля логина и пароля не могут быть пустыми!')
            } else if (this.account.username == /[0-9]{10}/) {
                this.$store.dispatch("SET_ACCOUNT", this.account)
            } else {
                this.display_alert('Неправильный формат логина или пароля!')
            }
        },
        redirect_to_office () {
            this.$router.push('/office')
        },
        clear_input () {
            this.account.username = null
            this.account.password = null
        },
        display_alert (alert_message) {
            this.$store.commit('SET_STATUS', alert_message)
            this.isAlert = true
        },
        hidden_alert () {
            this.$store.commit('SET_STATUS_DEFAULT')
            this.isAlert = false
        }
    }    
}
</script>

<style lang="less">

.alert {
    outline: none !important;
    border: 3px solid rgb(211, 43, 43);
    border-radius: 3px;
}
  
</style>