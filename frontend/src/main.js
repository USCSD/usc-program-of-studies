import { createApp, h } from "vue";
import App from "./App.vue";
import Router from "./router";

const app = createApp({
  render: () => h(App),
});

app.use(Router);

app.mount("#app");
