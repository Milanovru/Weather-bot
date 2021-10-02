<template>
    <div id="office">
        <div class="triangle opage"></div>
        <article class="officepage">
            <button class="btn btn-login" @click="logout()">
                {{user.is_active ? 'Log out' : 'Log in'}}
            </button>
            <h2>Личный кабинет</h2>
        </article>
        <section>
            <router-view />
            <!-- для теста -->
            <p>привет, {{user.username ? user.username : 'гость'}}</p>
        </section>
    </div>
</template>


<script>

export default {
    name: 'Office',
    data() {
        return {
            user: this.$store.getters.GET_USER,
        }
    },
    components: {
    },
    methods: {
        logout() {
            if (this.user.is_active) {
                this.$store.dispatch("LOGOUT", this.user.token)
            } else {
                this.$router.push("/accounts")
            }
        }
    },
}
</script>

<style lang="less">


</style>