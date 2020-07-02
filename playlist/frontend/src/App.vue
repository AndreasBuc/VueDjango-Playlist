<template>
  <div id="app">
    <Navigation/>
    <div class="container mt-5">

      <router-view />
    </div>
  </div>
</template>

<script>
import { apiService } from "@/common/api.service.js";
import Navigation from "@/components/Navigation";
export default {
    name: 'App',
    components: {
    Navigation
  },
methods: {
async setUserInfo() {
  const data = await apiService("/api/user/");
  const requestUser = data["username"];
  window.localStorage.setItem("username", requestUser);
  window.localStorage.setItem("username_id", data["id"]);
}
},
created() {
  this.setUserInfo()
},
}
</script>

<style>

</style>
