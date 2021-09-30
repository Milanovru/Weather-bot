<template>
    <div id="office">
        <div class="triangle opage"></div>
        <article class="officepage">
            <router-link to="/accounts">
                <button class="btn btn-login">
                    Log in
                </button>
            </router-link>
            <div class="officepage-main">
                Здесь будет личный кабинет
                <!-- <p>{{this.$store.getters.GET_USER}}</p> -->
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
            
        }
    },
    components: {
    },
    methods: {

    },
}
</script>

<style lang="less">


</style>