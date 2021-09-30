<template>
    <div id="office">
        <div class="triangle opage"></div>
        <article class="officepage">
            <router-link to="/accounts">
                <button class="btn btn-login" @click="check_authenticated()">
                    {{button_label}}
                </button>
            </router-link>
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
        return {
            is_authenticated: false,
            button_label: 'Log in',
            
        }
    },
    components: {
    },
    methods: {
        check_authenticated (){
            this.is_authenticated = true
            this.button_label = 'Log out'
        },
    },
}
</script>

<style lang="less">


</style>