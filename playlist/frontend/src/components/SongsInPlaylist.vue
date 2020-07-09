<template>
<div class="row">
  <div class="col-md-5 col-6 d-flex justify-content-center">{{song.title}}</div>
  <div class="col-md-5 col-6 d-flex justify-content-center">{{song.artist}}</div>
  <div class="col-md-1 col-6 d-flex justify-content-center">{{song.duration}}</div>
  <div class="col-md-1 col-6 d-flex justify-content-center">{{song.id}}</div>

</div>
</template>

<script>
import { apiService } from "@/common/api.service.js"
export default {
  name: 'SongsInPlaylist',
  props: {
    SongId: Number
  },
  data() {
    return {
      id: this.SongId,
      song: null,
    }
  },
  methods: {
    getSongInPlaylist() {
      let endpoint = `/api/songs/${this.id}/`;
      apiService(endpoint)
      .then(song => {
        this.song=song;
      })
    },

  },
  created() {
    this.getSongInPlaylist()
  }
}
</script>

<style>

</style>
