import Vue from "vue";
import VueRouter from "vue-router";
import Home from "../views/Home.vue";
import AddSong from "@/views/AddSong.vue";
Vue.use(VueRouter);

const routes = [
  {
    path: "/",
    name: "home",
    component: Home
  },
  {
    path: "/addSong",
    name: "add-song",
    component: AddSong
  },
  {
    path: "/editSong/:id?",
    name: "song-editor",
    component: AddSong,
    props: true
  }
];

const router = new VueRouter({
  mode: "history",
  // base: process.env.BASE_URL,
  routes
});

export default router;
