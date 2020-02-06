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
            <div
              v-if="class_detail && class_detail.class_name"
              class="card-content"
            >
              <div class="box has-text-centered ">
                <h1 class="title is-3">{{class_detail.class_name}}</h1>
                <p
                  class="is-1"
                  style="padding-bottom:15px"
                >{{class_detail.description}}</p>
                <table class="table is-bordered is-fullwidth is-hidden-touch">
                  <thead>
                    <tr>
                      <th>Class ID</th>
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
                      <td>{{class_detail.code}}</td>
                      <td>{{class_detail.length}}</td>
                      <td>{{class_detail.credits}}</td>
                      <td>{{class_detail.grade}}</td>
                      <td>{{class_detail.weighted}}</td>
                      <td>{{class_detail.qualification}}</td>
                      <td>{{class_detail.mods}}</td>
                    </tr>
                  </tbody>
                </table>
                <table class="table is-bordered is-fullwidth is-hidden-touch">
                  <thead>
                    <tr>
                      <th>
                        Prerequisites
                      </th>
                    </tr>
                  </thead>
                  <tbody>
                    <tr>
                      <td>
                        {{class_detail.prerequisite}}
                      </td>
                    </tr>
                  </tbody>
                </table>
                <table class="table is-bordered is-fullwidth is-hidden-desktop">
                  <thead>
                    <tr>
                      <th>Length</th>
                      <th>Credits</th>
                      <th>Grade Levels</th>
                    </tr>
                  </thead>
                  <tbody>
                    <tr>
                      <td>{{class_detail.length}}</td>
                      <td>{{class_detail.credits}}</td>
                      <td>{{class_detail.grade}}</td>
                    </tr>
                  </tbody>
                  <thead>
                    <tr>
                      <th>Weighted</th>
                      <th>Qualifications</th>
                      <th>Mods Per Week</th>
                    </tr>
                  </thead>
                  <tbody>
                    <tr>
                      <td>{{class_detail.weighted}}</td>
                      <td>{{class_detail.qualification}}</td>
                      <td>{{class_detail.mods}}</td>
                    </tr>
                  </tbody>
                  <thead>
                    <tr>
                      <th>Prerequisites</th>
                    </tr>
                  </thead>
                  <tbody>
                    <tr>
                      <td>{{class_detail.prerequisite}}</td>
                    </tr>
                  </tbody>
                </table>
              </div>
              <div class="box has-text-centered">
                <h1 class="title is-4">For More Information:</h1>
                <iframe
                  v-if="getId!='error'"
                  width="100%"
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
      class_detail: null
    }
  },

  computed: {
    getId: function () {
      var link = this.class_detail.link
      if (link.includes('you')) {
        var regExp = /^.*(youtu.be\/|v\/|u\/\w\/|embed\/|watch\?v=|\&v=)([^#\&\?]*).*/
        var match = this.class_detail.link.match(regExp)
        if (match && match[2].length === 11) {
          return 'https://www.youtube.com/embed/' + match[2]
        } else {
          return 'error'
        }
      } else {
        return link
      }
    }
  },
  created: function () {
    var self = this
    axios
      .get('/api/classes/' + self.$route.params.id)
      .then(function (response) {
        self.class_detail = response.data
        if (
          self.class_detail.qualification === '' ||
          self.class_detail.qualification == null
        ) {
          self.class_detail.qualification = 'None'
        }
        if (self.class_detail.weighted === true) {
          self.class_detail.weighted = 'Yes'
        }
        if (self.class_detail.weighted === false) {
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
