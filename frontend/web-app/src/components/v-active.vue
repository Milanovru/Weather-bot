<template>
    <div class="auth-user">
        <p>Состояние аккаунта в MPWeatherbot</p>
        <ul>
            <li>Регистрация: {{user.registration_data}}</li>
            <li>Подписка: {{user.subscribe_status}}</li>
        </ul>

    </div>
</template>

<script>
export default {
    data() {
        return {
            user: this.$store.getters.GET_USER,
        }
    },
}
</script>

<style lang="less">


</style>