<template>
    <div id="office">
        <div class="triangle opage"></div>
        <article class="office-page">
                <!-- {% if user.is_authenticated %}
            hello, {{user.username}}! -->
            <button class="btn btn-logout">
                <a href="">Log out</a>
            </button>
        <!-- {% else %}
            hello, guest! -->
            <button class="btn btn-login">
                <a href="">Log in</a>
            </button> 
        <!-- {% endif %} -->
        </article>
        <section>
        </section>
    </div>
</template>


<script>
export default {
  name: 'Office',
}
</script>