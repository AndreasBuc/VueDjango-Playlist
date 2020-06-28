<template>

  <nav class="navbar navbar-expand-lg navbar-dark bg-dark">
    <div class="container">
    <a class="navbar-brand" href="">
      <router-link
        :to="{ name: 'home' }"
        class="navbar-brand"
        >Playlist
      </router-link></a>
    <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
      <span class="navbar-toggler-icon"></span>
    </button>

    <div class="collapse navbar-collapse" id="navbarSupportedContent">
      <ul class="navbar-nav ml-auto">
        <li class="nav-item active">
          <a class="nav-link" href=""><router-link
            :to="{ name: 'add-song' }"
            class="navbar-brand"
            >Add Song
          </router-link><span class="sr-only">(current)</span></a>
        </li>
      </ul>
    </div>
    </div>
</nav>
</template>

<script>
  export default {
    name: 'navbar'
  }
</script>

<style scoped>

</style>
