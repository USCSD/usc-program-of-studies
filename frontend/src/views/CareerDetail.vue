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
              <a href="" class="link is-info">
                <img
                  src="../../static/usclogo.png"
                  alt=""
                  style="height: 100px"
                />
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
      <div class="container" style="margin-top: -100px">
        <div class="column is-8 is-offset-2">
          <div class="card">
            <div class="card-content">
              <div class="box has-text-centered">
                <h1 class="title is-3">
                  Career: {{ career_detail.career_name }}
                </h1>
                <p class="is-1" style="padding-bottom: 15px">
                  {{ career_detail.description }}
                </p>
                <h1 class="title is-4">Suggested Elective Classes</h1>
                <table class="table is-bordered is-fullwidth">
                  <thead>
                    <tr>
                      <th>Class Name</th>
                      <th>Grade Levels</th>
                    </tr>
                  </thead>
                  <tbody>
                    <div
                      v-for="a_class in career_detail.suggested_classes"
                      :key="a_class.id"
                      class="class"
                    >
                      {{ getClassName(a_class) }}
                    </div>
                    <tr
                      v-for="classdata in class_detail"
                      :key="classdata.id"
                      class="class"
                    >
                      <td>
                        <router-link
                          :to="{ name: 'detail', params: { id: classdata.id } }"
                          >{{ classdata.class_name }}</router-link
                        >
                      </td>
                      <td>{{ classdata.grade }}</td>
                    </tr>
                  </tbody>
                </table>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "careerdetail",
  data: function () {
    return {
      career_detail: [],
      class_detail: [],
      hasAdded: 0,
    };
  },

  methods: {
    getClassName: function (id) {
      var self = this;
      if (self.hasAdded !== self.career_detail.suggested_classes.length) {
        axios
          .get("/api/classes/" + id)
          .then(function (response) {
            self.class_detail.push(response.data);
          })
          .catch(function (error) {
            console.log(error);
          });
        this.hasAdded = this.hasAdded + 1;
      }
    },
  },

  created: function () {
    var self = this;
    axios
      .get("/api/careers/" + self.$route.params.id)
      .then(function (response) {
        self.career_detail = response.data;
      })
      .catch(function (error) {
        // if an error occurs, print that error
        console.log(error);
      });
  },
};
</script>
