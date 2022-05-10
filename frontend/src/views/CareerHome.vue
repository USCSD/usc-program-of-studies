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
              <h1 class="title is-3">Career Clusters</h1>
              <p
                class="subtitle is-5"
                style="padding-top:15px"
              >The Career Cluster initiative is coordinated by the National Association of State Directors of Career Technical Education Consortium. Career Clusters provide 16 groupings of occupations and associated career pathways that help students explore similarly grouped career options. The Career Cluster is an organization tool that helps students navigate their way to greater success in college and career. <strong>Click on one of the boxes below to get more information about the Cluster and a list of classes that fit under it.</strong></p>
            </div>
            <div class="columns">
              <template v-for="n in 2" :key="n">
                <div>
                  <div class="column">
                    <div
                      class="box"
                      v-for="index in 8"
                      :key="index"
                    >
                      <h1
                        v-if="careers"
                        class="subtitle is-5"
                      >
                        <router-link :to="{name:'careerdetail',params:{id:careers[8*(n-1)+(index-1)].id}}">{{careers[8*(n-1)+(index-1)].career_name}}</router-link>
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
</template>

<script>
import axios from 'axios'

export default {
  name: 'CareerHome',
  data: function () {
    return {
      careers: null
    }
  },
  created: function () {
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
