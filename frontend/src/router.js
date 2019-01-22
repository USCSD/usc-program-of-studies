import Vue from 'vue';
import Router from 'vue-router';
import Home from './views/Home.vue';
import List from './views/List.vue';
import Detail from './views/Detail.vue';
import CareerHome from './views/CareerHome.vue';
import CareerDetail from './views/CareerDetail.vue';

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'home',
      component: Home
    },
    {
      path: '/list',
      name: 'list',
      component: List
    },
    {
      path: '/list/:id',
      name: 'detail',
      component: Detail,
      props: true
    },
    {
      path: '/careers',
      name: 'careerhome',
      component: CareerHome
    },
    {
      path: '/careers/:id',
      name: 'careerdetail',
      component: CareerDetail,
      props: true
    }
  ]
})

/*  routes: [{
    path: '/',
    name: 'home',
    component: Home
  },
  {
    path: '/list',
    name: 'list',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () =>
      import (  webpackChunkName: "view"  './views/List.vue')
  }
] */
