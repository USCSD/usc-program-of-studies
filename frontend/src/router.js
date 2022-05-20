import { createWebHistory, createRouter } from "vue-router";
import Home from "./views/Home.vue";
import List from "./views/List.vue";
import Detail from "./views/Detail.vue";
import CareerHome from "./views/CareerHome.vue";
import CareerDetail from "./views/CareerDetail.vue";
import InfoDetail from "./views/InfoDetail.vue";
import InfoList from "./views/InfoList.vue";
import NotFound from "./views/NotFound.vue";

export default createRouter({
  history: createWebHistory("/"),
  routes: [
    {
      path: "/",
      name: "home",
      component: Home,
    },
    {
      path: "/list",
      name: "list",
      component: List,
    },
    {
      path: "/list/:id",
      name: "detail",
      component: Detail,
      props: true,
    },
    {
      path: "/careers",
      name: "careerhome",
      component: CareerHome,
    },
    {
      path: "/careers/:id",
      name: "careerdetail",
      component: CareerDetail,
      props: true,
    },
    {
      path: "/info",
      name: "infolist",
      component: InfoList,
    },
    {
      path: "/info/:id",
      name: "infodetail",
      component: InfoDetail,
      props: true,
    },
    {
      path: "/:pathMatch(.*)",
      component: NotFound,
    },
  ],
});
