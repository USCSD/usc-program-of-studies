<template>
  <div>
    <section class="hero is-dark is-fullheight has-bg-img">
      <!-- Hero header: will stick at the top -->
      <div class="hero-head">
        <header class="navbar">
          <div class="navbar-brand">
            <a
              class="navbar-item"
              href="https://www.uscsd.k12.pa.us/"
            >
              <img
                src="~__SHARED_STATIC__/usclogo.png"
                width="50"
                height="118"
              >
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
      <div
        class="hero-body"
        style="margin-bottom:50px"
      >
        <div class="container has-text-centered">
          <img
            style="margin-bottom:25px"
            src="~__SHARED_STATIC__/usclogo.png"
            width="250"
            height="400"
          >
          <h1 class="title">
            Welcome to the Upper Saint Clair Program of Studies!
          </h1>
          <h2 class="subtitle">
            An interactive website for more information about the USC classes.
          </h2>
          <router-link
            class="button is-fullwidth is-large"
            to="/list"
            style="margin-bottom:20px"
          >
            <div class="container has-text-centered">
              Click this button for a complete class list
              <span class="icon is-pulled-right">
                <i
                  class="fa fa-arrow-right"
                  aria-hidden="true"
                ></i>
              </span></div>

          </router-link>
          <router-link
            class="button is-fullwidth is-large"
            to="/careers"
            style="margin-bottom:20px"
          >
            <div class="container has-text-centered">
              Click this button for career clusters
              <span class="icon is-pulled-right">
                <i
                  class="fa fa-arrow-right"
                  aria-hidden="true"
                ></i>
              </span></div>

          </router-link>
          <router-link
            class="button is-fullwidth is-large"
            to="/info"
          >
            <div class="container has-text-centered">
              Click this button for general information
              <span class="icon is-pulled-right">
                <i
                  class="fa fa-arrow-right"
                  aria-hidden="true"
                ></i>
              </span></div>

          </router-link>
        </div>
      </div>
      <!-- Hero footer: will stick at the bottom -->
    </section>
  </div>
</template>

<style>
.has-bg-img {
  background: url("~__SHARED_STATIC__/homebackground.jpg") center center;
  background-size: cover;
}
</style>
