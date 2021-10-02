<template>
    <div class="form">
        <p>{{this.$store.getters.GET_STATUS}}</p>
        <input v-model.lazy="account.username" type='text' placeholder="Введите логин" class="form-item item1"/>
        <input v-model.lazy="account.password" type='password' placeholder="Введите пароль" class="form-item item1"/>
        <button @click="login()">
            Submit
        </button>   
        <button @click="create_account()">
            Registtation
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
        }
    },
    methods: {
        login () {
            this.$store.dispatch("LOGIN", this.account)
            this.clear_input()
            setTimeout(this.redirect_to_office, 2000)
        },
        create_account () {
            this.$store.dispatch("SET_ACCOUNT", this.account)
        },
        redirect_to_office () {
            this.$router.push('/office')
        },
        set_text_label () {
            if (this.$store.getters.GET_STATUS) {

            }
        },
        clear_input () {
            this.account.username = null
            this.account.password = null
        },
    }    
}
</script>

<style lang="less">

.form {
    position: absolute;
    top: 6rem;
    left: 3rem;
    display: grid;
    gap: 1rem;

    .item1, .item2 {
        width: 16rem;
        height: 1.7rem;
    }

} 
  
</style>