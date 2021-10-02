<template>
    <div class="form">
        <p>{{this.$store.getters.GET_STATUS}}</p>
        <input v-model.lazy="account.username" placeholder="Введите логин" class="form-item item1"/>
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
    methods: {
        login () {
            let data = this.$store.getters.GET_ACCOUNT
            this.$store.dispatch("LOGIN", data)
            setTimeout(this.redirect_to_office, 2000)
        },
        create_account () {
            let data = this.$store.getters.GET_ACCOUNT
            this.$store.dispatch("SET_ACCOUNT", data)
        },
        redirect_to_office () {
            this.$router.push('/office')
        }
    },
    computed: {
        account: {
            get () {
                return this.$store.state.account;
            },
            set (value) {
                this.$store.commit('SET_ACCOUNT', value);
            }
        }
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