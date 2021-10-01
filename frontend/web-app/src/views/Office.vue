<template>
    <div id="office">
        <div class="triangle opage"></div>
        <article class="officepage">
            
                <button class="btn btn-login" @click="logout()">
                    {{this.$store.getters.GET_BUTTON_LABEL}}
                </button>
            
            <div class="officepage-main">
                Здесь будет личный кабинет
                <router-view />
            </div>
        </article>
    </div>
</template>


<script>

export default {
    name: 'Office',
    data() {
        return {}
    },
    components: {
    },
    methods: {
        logout() {
            if (this.$store.getters.GET_BUTTON_LABEL == 'Log out') {
                let token = this.$store.state.user.token;
                this.$store.dispatch("LOGOUT", token)
            } else {
                this.$router.push("/accounts")
            }
        }
    },
}
</script>

<style lang="less">


</style>