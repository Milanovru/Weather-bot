<template>
    <div id="office">
        <div class="triangle opage"></div>
        <article class="officepage">
            <button class="btn btn-login" @click="logout()">
                {{user.is_active ? 'Log out' : 'Log in'}}
            </button>
            <h2>Личный кабинет</h2>
            <p>Добро пожаловать, {{user.telegram_name ? user.telegram_name : 'гость'}}!</p>
            <hr>
        </article>
        <section>
            <router-view />
            <vActive v-if="user.is_active"/>
            <vUndo v-else />
        </section>
    </div>
</template>


<script>
import vActive from '@/components/v-active.vue';
import vUndo from '@/components/v-undoactive.vue';

export default {
    name: 'Office',
    data() {
        return {
            user: this.$store.getters.GET_USER,
        }
    },
    components: {
        vActive,
        vUndo
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
    p {
        width: 75%;
    }
</style>