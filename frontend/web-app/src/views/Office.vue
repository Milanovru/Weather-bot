<template>
    <div id="office">
        <div class="triangle opage"></div>
        <article class="office-page">
            <form action="">
                <input v-model="account.username" placeholder="Введите логин" />
                <input v-model="account.password" placeholder="Введите пароль" />
                <button @click="create_account()">
                    Submit
                </button>                
            </form>

            <!-- <button class="btn btn-logout">
                Log out
            </button> -->

            <button class="btn btn-login" @click="create_account">
                Log in
            </button> 
        </article>
        <section>
        </section>
    </div>
</template>


<script>

export default {
    name: 'Office',
    data() {},
    methods: {
        create_account () {
            let data = this.$store.getters.GET_ACCOUNT
            console.log(data)
            this.$store.dispatch("SET_ACCOUNT", data)
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