<template>
  <div class="myPlaylists">
    <div class="centerthecontext">
      <h1>See your Playlists</h1>
      <h3 class="lead"> Here are all the songs in your Playlists</h3>
      <hr class="blueline">
    </div>
    <div class="row">
      <div class="col-3 text-c">
        <!-- Hier ist die Leiste -->
        <div  v-for="playlist in playlists"
              :key="playlist.id"
        >
          <div id="list-example" class="list-group">
            <a class="list-group-item text-c list-group-item-action" :href="'#'+playlist.id">{{playlist.name}}</a>
          </div>
        </div>
      </div>

    <div class="col-9">
      <!-- Hier ist der Inhalt -->
      <div data-spy="scroll" data-target="#list-example" data-offset="0" class="scrollspy-example">
        <div  v-for="playlist in playlists"
              :key="playlist.id"
        >
        <h4 :id="playlist.id">{{playlist.name}}</h4>
        <h4 v-if="playlist.is_empty" class="lead mb-3" >Noch kein Song in dieser Playliste</h4>
        <div
          v-for="(song,index) in playlist.songs"
          :key = "index">
          <SingleSong
          :id= song.id
          :showPlaylist="false"
          />

        </div>
      </div>
      </div>
    </div>

    </div>
  </div>
</template>

<script>
import SingleSong from "@/components/SingleSong"
import { apiService } from "@/common/api.service.js"
export default {
  name: 'MyPlaylist',
  components: {
    SingleSong
  },
  data() {
    return {
      playlists: [],
    }
  },
  methods: {
    getPlaylists() {
      let endpoint = "/api/playlists/";
      console.log('GET Playlist /api/playlists/')
      apiService(endpoint)
      .then(data => {
        console.log(data);
        this.playlists = data;
      })
    },

  },
  created() {
    this.getPlaylists()
  }
}
</script>

<style scoped>
.text-c {
  background-color: #4a4e4d;
  border-color: #4a4e4d;
  color: #63ace5;
}
.text-c:hover {

  border-color: #63ace5;
  color: #63ace5;
}
.blueline {
  border: solid 1px #63ace5;
}
.centerthecontext {
  text-align: center;

}
</style>
