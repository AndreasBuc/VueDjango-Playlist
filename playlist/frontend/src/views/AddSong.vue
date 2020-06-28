<template>
  <div class="addSong">

    <!-- heading -->
    <div class="centerthecontext">
      <h1>Add a song to your Playlist</h1>
      <h3 class="lead"> Fill out the Form to add a Song. Chubidu </h3>
      <hr class="blueline">
    </div>
    <!-- Fill out Form -->
    <div class="divstyle p-5">
      <form @submit.prevent="onSubmit">
        <div class="form-group">
          <label for="song-title">Title</label>
          <input type="text" v-model="title" class="form-control" id="song-title">
        </div>

        <div class="form-group">
          <label for="song-artist">Artist</label>
          <input type="text" v-model="artist" class="form-control" id="song-artist">
        </div>

        <div class="form-group">
          <label for="song-duration">Duration</label>
          <input type="number" v-model="duration" class="form-control" id="song-duration">
        </div>

        <div class="form-group">
          <label for="song-lyrics">Lyrics</label>
          <textarea type="textarea" v-model="lyrics" rows="8" class="form-control" id="song-lyrics"></textarea>
        </div>
        <button type="submit" class="btn btn-outline-light">{{buttonText}}</button>
      </form>
      <p  class="muted mt-2"
        v-if="error">{{error}}</p>
    </div>
  </div>
</template>

<script>
import { apiService } from "@/common/api.service.js"
export default {
  name: 'addSong',
  props: {
    id: {
      type: Number,
      required: false,
    }
  },
  data() {
    return{
      title: '',
      artist: '',
      duration: '',
      lyrics: '',
      error: '',
      buttonText: 'Add Song to Play',
    }
  },
  methods: {
    async onSubmit(){
        console.log("OnSubmit wurde gedrückt");
        if(!this.title){
          console.log('if(!this.title){');
          this.error = "You cannot send an empty title!";
        } else if (this.title.length > 240) {
        this.error = "Ensure this field has no more than 240 char ";
        }  else {
          let endpoint = "/api/songs/";
          let method = "POST";

          if(this.id !== undefined) {
            endpoint += `${this.id}/`;
            method = "PUT";
          }

          await apiService(endpoint, method, { title: this.title, artist: this.artist, duration: this.duration, lyrics: this.lyrics })
          .then(
            this.$router.push({
              name: 'home'
            })
          )
        }
      }
  },
  async beforeRouteEnter(to, from, next) {
      console.log('Ich bin im before Route Enter');
      if (to.params.id !== undefined) {
        console.log('Ich bin im before Route Enter und id ist nicht undefined');
        let endpoint = `/api/songs/${to.params.id}/`;
        let data = await apiService(endpoint);
        return next(vm => ( vm.title = data.title,
                            vm.artist= data.artist,
                            vm.duration = data.duration,
                            vm.lyrics = data.lyrics,
                            vm.buttonText = 'Update Song'))
      } else {
        console.log('Ich bin im before Route Enter und id ist undefined');
        return next();
      }


    },
}
</script>
.centerthecontext {
  text-align: center;
}
<style>
.divstyle {
  border: solid 2px #63ace5;
  border-radius: 5px;
}
</style>
