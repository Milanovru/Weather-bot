<template>
    <div id="accounts">
        <div class="triangle opage"></div>
        <article class="accountspage">
            <vLogin />
        </article>
    </div>
</template>

<script>
import vLogin from '@/components/v-login.vue';


export default {
    name: 'Accounts',
    components: {
        vLogin,
    },
    methods: {
    }

}
</script>