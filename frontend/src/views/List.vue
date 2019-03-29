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
              <div class="box">
                <div class="buttons is-centered">
                  <div class="control">
                    <div class="dropdown is-hoverable">
                      <div class="dropdown-trigger">
                        <button
                          class="button"
                          style="margin-right: 10px"
                          aria-haspopup="true"
                          aria-controls="dropdown-menu4"
                        >
                          <span>Grade Level</span>
                          <span class="icon is-small">
                            <i
                              class="fa fa-caret-down"
                              aria-hidden="true"
                            ></i>
                          </span>
                        </button>
                      </div>
                      <div
                        class="dropdown-menu"
                        id="dropdown-menu4"
                        role="menu"
                      >
                        <div class="dropdown-content">
                          <div style="padding-left:5px">
                            <input
                              type="checkbox"
                              id="9th"
                              value="grade=9"
                              v-model="checkedBoxes"
                              @change="filter"
                            >
                            <label for="9th"> 9th</label>
                          </div>
                        </div>
                        <div class="dropdown-content">
                          <div style="padding-left:5px">
                            <input
                              type="checkbox"
                              id="10th"
                              value="grade=10"
                              v-model="checkedBoxes"
                              @change="filter"
                            >
                            <label for="10th"> 10th</label>
                          </div>
                        </div>
                        <div class="dropdown-content">
                          <div style="padding-left:5px">
                            <input
                              type="checkbox"
                              id="11th"
                              value="grade=11"
                              v-model="checkedBoxes"
                              @change="filter"
                            >
                            <label for="11th"> 11th</label>
                          </div>
                        </div>
                        <div class="dropdown-content">
                          <div style="padding-left:5px">
                            <input
                              type="checkbox"
                              id="12th"
                              value="grade=12"
                              v-model="checkedBoxes"
                              @change="filter"
                            >
                            <label for="12th"> 12th</label>
                          </div>
                        </div>
                      </div>
                    </div>
                  </div>
                  <div class=control>
                    <div class="dropdown is-hoverable">
                      <div class="dropdown-trigger">
                        <button
                          class="button"
                          aria-haspopup="true"
                          aria-controls="dropdown-menu4"
                          style="margin-right: 10px"
                        >
                          <span>Subject</span>
                          <span class="icon is-small">
                            <i
                              class="fa fa-caret-down"
                              aria-hidden="true"
                            ></i>
                          </span>
                        </button>
                      </div>
                      <div
                        class="dropdown-menu"
                        id="dropdown-menu4"
                        role="menu"
                      >
                        <div class="dropdown-content">
                          <div style="padding-left:5px">
                            <input
                              type="checkbox"
                              id="English"
                              value="subject=English"
                              v-model="checkedBoxes"
                              @change="filter"
                            >
                            <label for="English"> English</label>
                          </div>
                        </div>
                        <div class="dropdown-content">
                          <div style="padding-left:5px">
                            <input
                              type="checkbox"
                              id="Science"
                              value="subject=Science"
                              v-model="checkedBoxes"
                              @change="filter"
                            >
                            <label for="Science"> Science</label>
                          </div>
                        </div>
                        <div class="dropdown-content">
                          <div style="padding-left:5px">
                            <input
                              type="checkbox"
                              id="Social Studies"
                              value="subject=Social Studies"
                              v-model="checkedBoxes"
                              @change="filter"
                            >
                            <label for="Social Studies"> Social Studies</label>
                          </div>
                        </div>
                        <div class="dropdown-content">
                          <div style="padding-left:5px">
                            <input
                              type="checkbox"
                              id="Mathematics"
                              value="subject=Mathematics"
                              v-model="checkedBoxes"
                              @change="filter"
                            >
                            <label for="Mathematics"> Mathematics</label>
                          </div>
                        </div>
                        <div class="dropdown-content">
                          <div style="padding-left:5px">
                            <input
                              type="checkbox"
                              id="Electives"
                              value="subject=Electives"
                              v-model="checkedBoxes"
                              @change="filter"
                            >
                            <label for="Electives">Electives</label>
                          </div>
                        </div>
                        <div class="dropdown-content">
                          <div style="padding-left:5px">
                            <input
                              type="checkbox"
                              id="World Language Electives"
                              value="subject=World Language Electives"
                              v-model="checkedBoxes"
                              @change="filter"
                            >
                            <label for="World Language Electives"> World Language Electives</label>
                          </div>
                        </div>
                        <div class="dropdown-content">
                          <div style="padding-left:5px">
                            <input
                              type="checkbox"
                              id="Technical and Practical Studies"
                              value="subject=Technical and Practical Studies"
                              v-model="checkedBoxes"
                              @change="filter"
                            >
                            <label for="Technical and Practical Studies"> Technical and Practical Studies</label>
                          </div>
                        </div>
                        <div class="dropdown-content">
                          <div style="padding-left:5px">
                            <input
                              type="checkbox"
                              id="Visual Arts Electives"
                              value="subject=Visual Arts Electives"
                              v-model="checkedBoxes"
                              @change="filter"
                            >
                            <label for="Visual Arts Electives"> Visual Arts Electives</label>
                          </div>
                        </div>
                        <div class="dropdown-content">
                          <div style="padding-left:5px">
                            <input
                              type="checkbox"
                              id="Music Electives"
                              value="subject=Music Electives"
                              v-model="checkedBoxes"
                              @change="filter"
                            >
                            <label for="Music Electives"> Music Electives</label>
                          </div>
                        </div>
                        <div class="dropdown-content">
                          <div style="padding-left:5px">
                            <input
                              type="checkbox"
                              id="Wellness Education"
                              value="subject=Wellness Education"
                              v-model="checkedBoxes"
                              @change="filter"
                            >
                            <label for="Wellness Education"> Wellness Education</label>
                          </div>
                        </div>
                        <div class="dropdown-content">
                          <div style="padding-left:5px">
                            <input
                              type="checkbox"
                              id="Interdisciplinary Opportunities Electives"
                              value="subject=Interdisciplinary Opportunities Electives"
                              v-model="checkedBoxes"
                              @change="filter"
                            >
                            <label for="Interdisciplinary Opportunities Electives"> Interdisciplinary Opportunities Electives</label>
                          </div>
                        </div>
                      </div>
                    </div>
                  </div>
                  <div class=control>
                    <div class="dropdown is-hoverable">
                      <div class="dropdown-trigger">
                        <button
                          class="button"
                          aria-haspopup="true"
                          aria-controls="dropdown-menu4"
                          style="margin-right: 10px"
                        >
                          <span>Qualifications</span>
                          <span class="icon is-small">
                            <i
                              class="fa fa-caret-down"
                              aria-hidden="true"
                            ></i>
                          </span>
                        </button>
                      </div>
                      <div
                        class="dropdown-menu"
                        id="dropdown-menu4"
                        role="menu"
                      >
                        <div class="dropdown-content">
                          <div style="padding-left:5px">
                            <input
                              type="checkbox"
                              id="AP"
                              value="qualification=AP"
                              v-model="checkedBoxes"
                              @change="filter"
                            >
                            <label for="AP"> Advanced Placement(AP)</label>
                          </div>
                        </div>
                        <div class="dropdown-content">
                          <div style="padding-left:5px">
                            <input
                              type="checkbox"
                              id="Honors"
                              value="qualification=Honors"
                              v-model="checkedBoxes"
                              @change="filter"
                            >
                            <label for="Honors"> Honors</label>
                          </div>
                        </div>
                        <div class="dropdown-content">
                          <div style="padding-left:5px">
                            <input
                              type="checkbox"
                              id="IB Diploma"
                              value="qualification=IB Diploma"
                              v-model="checkedBoxes"
                              @change="filter"
                            >
                            <label for="IB Diploma"> IB Diploma</label>
                          </div>
                        </div>
                      </div>
                    </div>
                  </div>
                  <div class=control>
                    <div class="dropdown is-hoverable">
                      <div class="dropdown-trigger">
                        <button
                          class="button"
                          aria-haspopup="true"
                          aria-controls="dropdown-menu4"
                          style="margin-right: 10px"
                        >
                          <span>Term Length</span>
                          <span class="icon is-small">
                            <i
                              class="fa fa-caret-down"
                              aria-hidden="true"
                            ></i>
                          </span>
                        </button>
                      </div>
                      <div
                        class="dropdown-menu"
                        id="dropdown-menu4"
                        role="menu"
                      >
                        <div class="dropdown-content">
                          <div style="padding-left:5px">
                            <input
                              type="checkbox"
                              id="year"
                              value="length=year"
                              v-model="checkedBoxes"
                              @change="filter"
                            >
                            <label for="year"> Year</label>
                          </div>
                        </div>
                        <div class="dropdown-content">
                          <div style="padding-left:5px">
                            <input
                              type="checkbox"
                              id="semester"
                              value="length=semester"
                              v-model="checkedBoxes"
                              @change="filter"
                            >
                            <label for="semester"> Semester</label>
                          </div>
                        </div>
                      </div>
                    </div>
                  </div>
                  <div class=control>
                    <div class="dropdown is-hoverable">
                      <div class="dropdown-trigger">
                        <button
                          class="button"
                          aria-haspopup="true"
                          aria-controls="dropdown-menu4"
                          style="margin-right: 10px"
                        >
                          <span>Credits Per Semester</span>
                          <span class="icon is-small">
                            <i
                              class="fa fa-caret-down"
                              aria-hidden="true"
                            ></i>
                          </span>
                        </button>
                      </div>
                      <div
                        class="dropdown-menu"
                        id="dropdown-menu4"
                        role="menu"
                      >
                        <div class="dropdown-content">
                          <div style="padding-left:5px">
                            <input
                              type="checkbox"
                              id="half credit"
                              value="credits=0.5"
                              v-model="checkedBoxes"
                              @change="filter"
                            >
                            <label for="half credit"> 0.5</label>
                          </div>
                        </div>
                        <div class="dropdown-content">
                          <div style="padding-left:5px">
                            <input
                              type="checkbox"
                              id="1 credit"
                              value="credits=1"
                              v-model="checkedBoxes"
                              @change="filter"
                            >
                            <label for="1 credits"> 1</label>
                          </div>
                        </div>
                      </div>
                    </div>
                  </div>

                </div>
                <div class="level">
                  <input
                    class='input'
                    type="text"
                    placeholder='Enter Keywords'
                    id='searchbar'
                    v-model='search_term'
                    v-on:keyup="filter"
                  >
                </div>
              </div>
              <table class="table is-fullwidth is-bordered">
                <thead>
                  <th>Class Name</th>
                  <th>Grade Levels</th>
                  <th>Subject</th>
                  <th>Credits</th>
                </thead>

                <tbody id='table_body'>
                  <tr v-if="classes.length==0||classes==null">
                    <td>No Classes Matched Your Search :(</td>
                    <td>Try Different Search Terms!</td>
                    <td></td>
                    <td></td>
                  </tr>
                  <tr
                    v-else
                    v-for="a_class in classes"
                    :key="a_class.id"
                  >
                    <td>
                      <router-link :to="{name:'detail', params: {id:a_class.id}}">{{a_class.class_name}}</router-link>
                    </td>
                    <td>
                      {{a_class.grade}}
                    </td>
                    <td>
                      {{a_class.subject}}
                    </td>
                    <td>
                      {{a_class.credits}}
                    </td>
                  </tr>
                </tbody>
              </table>
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
  name: 'list',
  data: function () {
    return {
      classes: [],
      checkedBoxes: [],
      search_term: '',
      filters: '?'
    }
  },
  created: function () {
    var self = this

    axios
      .get('/api/classes/?format=json')
      .then(function (response) {
        self.classes = response.data
      })
      .catch(function (error) {
        // if an error occurs, print that error
        console.log(error)
      })
  },
  methods: {
    filter: function () {
      var self = this
      var box
      self.filters = '?'
      for (box = 0; box < self.checkedBoxes.length; box++) {
        self.filters = self.filters + String(self.checkedBoxes[box]) + '&'
      }
      if (this.search_term !== '' || this.search_term !== null) {
        self.filters = self.filters + 'search=' + this.search_term
      }
      axios
        .get('/api/classes/' + self.filters)
        .then(function (response) {
          self.classes = response.data
        })
        .catch(function (error) {
          // if an error occurs, print that error
          console.log(error)
        })
    }
  }
}
</script>
