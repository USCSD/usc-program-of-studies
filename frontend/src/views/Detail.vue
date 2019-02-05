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
    <div class="list">
      <div
        class="container"
        style="margin-top:-100px;"
      >
        <div class="column is-8 is-offset-2">
          <div class="card">
            <div class="card-content">
              <div class="box has-text-centered ">
                <h1 class="title is-3">{{class_detail.class_name}}</h1>
                <p
                  class="is-1"
                  style="padding-bottom:15px"
                >{{class_detail.description}}</p>
                <table class="table is-bordered is-fullwidth">
                  <thead>
                    <tr>
                      <th>Length</th>
                      <th>Credits</th>
                      <th>Grade Levels</th>
                      <th>Weighted</th>
                      <th>Qualifications</th>
                      <th>Mods Per Week</th>
                    </tr>
                  </thead>
                  <tbody>
                    <tr>
                      <td>{{class_detail.length}}</td>
                      <td>{{class_detail.credits}}</td>
                      <td>{{class_detail.grade}}</td>
                      <td>{{class_detail.weighted}}</td>
                      <td>{{class_detail.qualifications}}</td>
                      <td>{{class_detail.mods}}</td>
                    </tr>
                  </tbody>
                </table>
              </div>
              <div class="box has-text-centered">
                <h1 class="title is-4">For More Information:</h1>
                <iframe
                  v-if="getId!='error'"
                  width="640"
                  height="360"
                  :src=" getId "
                  frameborder="0"
                  allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture"
                  allowfullscreen
                ></iframe>
                <p v-else>Video Not Available</p>
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
  name: 'detail',
  data: function () {
    return {
      class_detail: []
    }
  },

  computed: {
    getId: function () {
      var regExp = /^.*(youtu.be\/|v\/|u\/\w\/|embed\/|watch\?v=|\&v=)([^#\&\?]*).*/
      var match = this.class_detail.link.match(regExp)

      if (match && match[2].length == 11) {
        return 'https://www.youtube.com/embed/' + match[2]
      } else {
        return 'error'
      }
    }
  },
  created: function () {
    console.log('detail::created') // useful for understanding the lifecycle
    var self = this
    axios
      .get('/api/classes/' + self.$route.params.id)
      .then(function (response) {
        self.class_detail = response.data
        if (
          self.class_detail.qualifications == '' ||
          self.class_detail.qualifications == null
        ) {
          self.class_detail.qualifications = 'None'
        }
        if (self.class_detail.weighted == true) {
          self.class_detail.weighted = 'Yes'
        }
        if (self.class_detail.weighted == false) {
          self.class_detail.weighted = 'No'
        }
      })
      .catch(function (error) {
        // if an error occurs, print that error
        console.log(error)
      })
  }
}
</script>
