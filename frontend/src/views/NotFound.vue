<template>
  <div>
    <section class="hero is-dark is-fullheight has-bg-img">
      <!-- Hero header: will stick at the top -->
      <div class="hero-head">
        <header class="navbar">
          <div class="navbar-brand">
            <a class="navbar-item" href="https://www.uscsd.k12.pa.us/">
              <img src="../../static/usclogo.png" width="50" height="118" />
            </a>

            <div class="navbar-burger">
              <span></span>
              <span></span>
              <span></span>
            </div>
          </div>
          <div class="navbar-menu">
            <!-- navbar start, navbar end -->
            <div class="navbar-end">
              <a class="navbar-item">
                <a href="/admin">Admin Page</a>
              </a>
              <a class="navbar-item">
                <router-link to="/list">Class List</router-link>
              </a>
            </div>
          </div>
        </header>
      </div>

      <!-- Hero content: will be in the middle -->
      <div class="hero-body" style="margin-bottom: 50px">
        <div class="container has-text-centered">
          <img
            style="margin-bottom: 25px"
            src="../../static/usclogo.png"
            width="250"
            height="400"
          />
          <h1 class="title">Not Found</h1>
        </div>
      </div>
      <!-- Hero footer: will stick at the bottom -->
    </section>
  </div>
</template>

<style>
.has-bg-img {
  background: url("../../static/homebackground.jpg") center center;
  background-size: cover;
}
</style>
