<!--<template>
    <div>
        <div id="nav">
            <div class="hero is-medium is-bold is-dark">
                <div class="hero-body">
                    <nav class="level">
                        <p class="level-item has-text-centered">
                            <router-link to="/">Home</router-link>
                        </p>
                        <p class="level-item has-text-centered">
                            <a href="" class="link is-info">
                                <img src="https://webinfo.uscsd.k12.pa.us/wp-content/uploads/2016/08/USCLogoBlackOutline-e1471545661634.png"
                                    alt="" style="height:100px;">
                            </a>
                        </p>
                        <p class="level-item has-text-centered">
                            <router-link to="/list">Class List</router-link>
                        </p>
                    </nav>
                </div>
            </div>
        </div>
        <div class="list">
            <div class="container" style="margin-top:-100px;">
                <div class="column is-8 is-offset-2">
                    <div class="card">
    <div class="card-content">
        <div class="box">
        <div class="media">
            <div class="media-content has-text-centered">
                <p class="title is-size-2">Welcome to the Upper Saint Clair School District Program of Studies</p>
            </div>
        </div>
        <div class="content article-body has-text-centered">
            <p class="subtitle is-size-4">A 100 page PDF condensed into a single webpage for easy viewing access</p>
        </div>
        </div>
    </div>
    </div>
    </div>
    </div>
    </div>
    </div>
</template>-->

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
              <a
                class="navbar-item"
                href="/about"
              >About</a>
              <a class="navbar-item">
                <router-link to="/list">Class List</router-link>
              </a>
            </div>
          </div>
        </header>
      </div>

      <!-- Hero content: will be in the middle -->
      <div class="hero-body">
        <div class="container has-text-centered">
          <h1 class="title">
            Welcome to the Upper Saint Clair Program of Studies!
          </h1>
          <h2 class="subtitle">
            An interactive website for more information about the USC classes
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

<!--<script>
// @ is an alias to /src
import HelloWorld from "@/components/HelloWorld.vue";

export default {
  name: "home",
  components: {
    HelloWorld
  }
};
</script>-->
