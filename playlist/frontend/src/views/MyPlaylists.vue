<template>
  <div class="myplaylist">
    <div class="centerthecontext">
      <h1>My Playlists</h1>
      <h3 class="lead"> Here are all your playlists and songs</h3>
      <hr class="blueline">
    </div>
    <!-- Add a new Playlist to your Account -->
    <div class="row ">
      <div class="col-3 d-flex justify-content-center middleline">
        <input v-model="name" placeholder = " Add a new playlist" type="text">
      </div>
      <div class="col-1">
        <!-- Add Button -->
        <div @mouseover="addhover = true" class="mx-1" >
          <a @click="onSubmit" href=""><img v-if="!addhover" class="icon" alt="Edit" src="../assets/add.svg"></a>
        </div>

        <div @mouseleave="addhover = false" class="mx-1">
          <a @click="onSubmit" href=""><img v-if="addhover" class="icon" alt="Edit" src="../assets/add-hover.svg"></a>
        </div>
        {{error}}
      </div>

      <!-- END - Add a new Playlist to your Account -->
    </div>
    <br>
    <!-- Table with all the data -->
    <div  class="row"
          v-for="playlist in playlists"
          :key=playlist.id
          >
        <div class="col-3 middleline">
          <PlaylistInPlaylists
          :PlaylistName = playlist.name
          :PlaylistID = playlist.id
          >
          </PlaylistInPlaylists>


        </div>
        <div class="col-9 ">
          <SongsInPlaylist
            v-for="song in playlist.songs"
            :key="song.id"
            class="d-flex justify-content-center"
            :SongId="song.id"
          >
        </SongsInPlaylist>
        <hr>
        </div>
    </div>

  </div>
</template>

<script>
import { apiService } from "@/common/api.service.js";
import SongsInPlaylist from "@/components/SongsInPlaylist.vue"
import PlaylistInPlaylists from "@/components/PlaylistInPlaylists.vue"

export default {
  name: 'MyPlaylist',
  components: {
    SongsInPlaylist,
    PlaylistInPlaylists,
  },
  data() {
    return {
      playlists: [],
      addhover: false,
      error: null,
      name: null,
    }
  },
  methods: {
    getMyPlaylistsIDs() {
      let endpoint = "/api/users-playlists/";
      apiService(endpoint)
      .then(playlists => {
        this.playlists=playlists;
      })
    },
    async onSubmit(){
        if(!this.name){
          this.error = "You cannot send an empty Name!";
        } else if (this.name.length > 240) {
        this.error = "Ensure this field has no more than 240 char ";
        }  else {
          let endpoint = "/api/users-playlists/";
          let method = "POST";

          await apiService(endpoint, method, {name: this.name})
          .then(
            this.getMyPlaylistsIDs()
            // this.$router.push({
            //   name: 'my-playlist'
            // })
          )
        }
      }

  },
  created() {
    this.getMyPlaylistsIDs()
  }
}
</script>

<style scoped>
.centerthecontext {
  text-align: center;
}
.middleline {
  border-style: none solid none none;
  border-color: #63ace5
}
input:not(.userListBox){
  background:transparent !important;
  border: none !important;
  outline: none !important;
  padding: 0px 0px 0px 0px !important;
  color: #63ace5;
}
.icon {
  height: 24px;
  weight: 24px;
  padding: 2px 2px 2px 2px  ;
}

</style>
