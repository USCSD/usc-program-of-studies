<template>
  <div>
    <div id="nav">
      <div class="hero is-medium is-bold is-dark">
        <div class="hero-body">
          <nav class="level">
            <p class="level-item has-text-centered">
              <router-link to="/">Home</router-link>
            </p>
            <p class="level-item has-text-centered">
              <a
                href=""
                class="link is-info"
              >
                <img
                  src="~__SHARED_STATIC__/usclogo.png"
                  alt=""
                  style="height:100px;"
                >
              </a>
            </p>
            <p class="level-item has-text-centered">
              <router-link to="/list">Class List</router-link>
            </p>
          </nav>
        </div>
      </div>
    </div>
    <div
      class="container"
      style="margin-top:-100px;"
    >
      <div class="column is-8 is-offset-2">
        <div class="card">
          <div class="card-content">
            <div class="box">
              <h1 class="title is-3">{{info_detail.info_name}}</h1>
              <div>
                <object
                  :data="info_detail.file_name"
                  type="application/pdf"
                  width="100%"
                  height="600px"
                >
                  <p>It appears you don't have a PDF plugin for this browser.</p>
                </object>
              </div>
              <a
                :href="info_detail.file_name"
                download
              >Click here to download the PDF file</a>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'infodetail',
  data: function () {
    return {
      info_detail: []
    }
  },
  created: function () {
    var self = this
    axios
      .get('/api/info/' + self.$route.params.id)
      .then(function (response) {
        self.info_detail = response.data
      })
      .catch(function (error) {
        // if an error occurs, print that error
        console.log(error)
      })
  }

}
</script>
