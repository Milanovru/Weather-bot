<template>
  <header>
    <nav class="nav">
      <router-link to="/">
        <span class="nav-item">
          <img src="@/assets/home.png"  alt="home">
        </span>
      </router-link>
      <router-link to="/work">
        <span class="nav-item">
          <img src="@/assets/work.png" alt="work">
        </span>
      </router-link>
      <router-link to="/office">
        <span class="nav-item">
          <img src="@/assets/office.png" alt="office">
        </span>
      </router-link>
      <a href="https://instagram.com/milanov_web_programming?utm_medium=copy_link" target="_blank" class="nav-item">
        <img src="@/assets/contact.png" alt="contact">
      </a>
    </nav>
  </header>
  <router-view/>
</template>

<style lang="less" src="./main.less">
</style>
