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
            <div
              class="box"
              v-for="a_career in careers"
              :key="a_career.id"
            >
              <router-link :to="{name:'careerdetail',params:{id:a_career.id}}">{{a_career.career_name}}</router-link>
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
  name: 'CareerHome',
  data: function () {
    return {
      careers: []
    }
  },
  created: function () {
    console.log('list::created') // useful for understanding the lifecycle

    var self = this

    axios
      .get('/api/careers/?format=json')
      .then(function (response) {
        self.careers = response.data
      })
      .catch(function (error) {
        // if an error occurs, print that error
        console.log(error)
      })
  }
}
</script>
