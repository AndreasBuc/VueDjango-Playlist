import Vue from "vue";
import VueRouter from "vue-router";
import MySongs from "../views/Home.vue";
import AddSong from "@/views/AddSong.vue";
import MyPlaylist from "@/views/MyPlaylists.vue";
Vue.use(VueRouter);

const routes = [
  {
    path: "/",
    name: "home",
    component: MySongs
  },
  {
    path: "/myPlaylist",
    name: "my-playlist",
    component: MyPlaylist
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
