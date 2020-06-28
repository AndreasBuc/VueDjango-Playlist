<template>
  <div class="home">
    <div class="centerthecontext">
      <h1>Playlist</h1>
      <h3 class="lead"> Here are all the songs you like</h3>
      <hr class="blueline">
    </div>
    <div class="song">
      <div v-for="song in songs" :key="song.pk">
        <SingleSong
            :id="song.id"
            :title="song.title"
            :artist="song.artist"
            :duration="song.duration"
            :lyrics="song.lyrics"
        ></SingleSong>
      </div>
    </div>
  </div>
</template>

<script>
import SingleSong from "@/components/SingleSong.vue"
import { apiService } from "@/common/api.service.js"
export default {
  name: 'Home',
  components: {
    SingleSong
  },
  data() {
    return {
      songs: [],
    }
  },
  methods: {
    getSongs() {
      let endpoint = "/api/songs/";
      console.log('Songs are beeing get')
      apiService(endpoint)
      .then(data => {
        console.log(data);
        this.songs=data
      })
    },
    makeLyricsShort(lyrics) {
      var LYRIC_LENGTH = 400;
      if (lyrics.length > LYRIC_LENGTH) {
        return lyrics.slice(0, LYRIC_LENGTH).replace(/\n/ig, ' -- ') + '...';
      } else {
        return lyrics.replace(/\n/ig, '-');
      }
    }
  },
  created() {
    console.log('Playlist is created, get Songs')
    this.getSongs()
    console.log('Songs have been fetched: '+ this.songs)
  }
}
</script>

<style>
.centerthecontext {
  text-align: center;
}
.blueline {
  border: solid 1px #63ace5;
}
.divstyle {
  border: solid 2px #63ace5;
  border-radius: 5px;
}
.icon {
  height: 20px;
  weight: 20px;
}
.icon:hover {
  color: #e7eff6;
}
</style>
