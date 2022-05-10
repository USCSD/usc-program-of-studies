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
                  src="./static/usclogo.png"
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
              <h1 class="title is-2">General Information</h1>
              <div class="columns">
                <template v-for="column in columns" :key="column.id">
                  <div>
                    <div class="column">
                      <div
                        class="box"
                        v-for="info in column"
                        :key="info.id"
                      >
                        <h1 class="subtitle is-5">
                          <router-link :to="{name:'infodetail',params:{id:info.id}}">{{info.info_name}}</router-link>
                        </h1>
                      </div>
                    </div>
                  </div>
                </template>
              </div>

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
  name: 'infolist',
  data: function () {
    return {
      info: [],
      cols: 2
    }
  },
  created: function () {
    var self = this

    axios
      .get('/api/info/?format=json')
      .then(function (response) {
        self.info = response.data
      })
      .catch(function (error) {
        // if an error occurs, print that error
        console.log(error)
      })
  },
  computed: {
    columns () {
      let columns = []
      let mid = Math.ceil(this.info.length / this.cols)
      for (let col = 0; col < this.cols; col++) {
        columns.push(this.info.slice(col * mid, col * mid + mid))
      }
      return columns
    }
  }
}

</script>
