<template>
<div class="single-song">
    <div class="divstyle my-3 p-2">
      <div class="row">
        <div class="col-md-4">
          <div class="row">
            <div class="col-6">TITLE:</div>
            <div class="col-6">{{song.title}}</div>
          </div>
          <div class="row">
            <div class="col-6">Artist</div>
            <div class="col-6">{{song.artist}}</div>
          </div>
          <div class="row mb-3">
            <div class="col-6">Duration</div>
            <div class="col-6">{{song.duration}}</div>
          </div>
        </div>
        <div class="col-md-8">

          <div class="row">
            <div class="col-8"><p>Lyrics:</p></div>
            <div class="col-4">




                  <div class="row">
                    <router-link
                      :to="{ name: 'song-editor', params: {id: song.id} }"
                      ><a
                      href="">
                      <div @mouseover="edithover = true">
                        <img v-if="!edithover" class="icon" alt="Edit" src="../assets/edit.svg">
                      </div>
                      <div @mouseleave="edithover = false">
                        <img v-if="edithover" class="icon" alt="Edit" src="../assets/edit-hover.svg">
                      </div>
                    </a>
                    </router-link>

                    <div @mouseover="deletehover = true" class="ml-2">
                      <a @click="deleteSong" href=""><img v-if="!deletehover" class="icon" alt="Edit" src="../assets/delete.svg"></a>
                    </div>
                    <div @mouseleave="deletehover = false">
                      <a @click="deleteSong" href=""><img v-if="deletehover" class="icon" alt="Edit" src="../assets/delete-hover.svg"></a>
                    </div>
                  </div>


            </div>
          </div>
          <p>{{makeLyricsShort(song.lyrics)}}
            <img class="icon" v-if="songIsToLong && !showFullLyrics && !plushover"   @mouseover="plushover = true"      alt="see more" src="../assets/plus.svg">
            <img class="icon" v-if="songIsToLong && !showFullLyrics && plushover"    @mouseleave="plushover = false"    @click="showFullLyrics = true" alt="see more" src="../assets/plus-hover.svg">
            <img class="icon" v-if="showFullLyrics && !minushover" @mouseover="minushover = true"    alt="see less" src="../assets/minus.svg">
            <img class="icon" v-if="showFullLyrics && minushover"  @mouseover="minushover = false"   @click="showFullLyrics = false" alt="see less" src="../assets/minus-hover.svg">
          </p>

          <div v-if="song.is_in_playlist && showSongsPlaylist" class="my-3 p-2" >
            <p>Playlists:</p>
            <div  v-for="(playlist, index) in song.playlists"
                  :key="index"
            >

            <div class="row">
              <div class="col-6">
                <p>
                  {{playlist.name}}
                </p>
              </div>
              <div class="col-6">
                  <a @click="removePlaylist(playlist.id)" href=""><img  class="icon" alt="Delete" src="../assets/delete.svg"></a>
              </div>
            </div>

                    </div>
          </div>

        </div>


      </div>
    </div>

</div>
</template>

<script>
import { apiService } from "@/common/api.service.js"
export default {
  name: 'SingleSong',
  props: {
    id: Number,
    showPlaylist: {
      type: Boolean,
      required: false,
    }
  },
  data() {
    return {
      song: [],
      songID: this.id,
      edithover: false,
      deletehover: false,
      plushover: false,
      minushover: false,
      songIsToLong: false,
      showFullLyrics: false,
      showSongsPlaylist: this.showPlaylist,
    }
  },

  methods: {
    getSong() {
      let endpoint = `/api/users-songs/${this.songID}/`;
      console.log('Song is fetched by ID')
      apiService(endpoint)
      .then(data => {
        console.log(data);
        this.song=data
      })
    },
    async removePlaylist(p_pk) {
      let endpoint = `/api/users-add-remove-song/${p_pk}/${this.songID}/`;
      console.log('Song is fetched by ID')
      await apiService(endpoint, "DELETE")


    },
    setBackHoverValue() {
      this.edithover= false;
      this.deletehover= false;
      this.plushover= false;
      this.minushover= false;
    },
    makeLyricsShort(lyrics) {
      var LYRIC_LENGTH = 100;
      if (this.showFullLyrics) {
        return lyrics.replace(/\n/ig, ' -- ');
      } else if (lyrics.length > LYRIC_LENGTH) {
        this.songIsToLong = true;
        return lyrics.slice(0, LYRIC_LENGTH).replace(/\n/ig, ' -- ') + '...';
      } else {
       return lyrics.replace(/\n/ig, ' -- ');
     }


    },
    async deleteSong() {
        let endpoint = `/api/users-songs/${this.songID}/`;
        try {
          await apiService(endpoint, "DELETE")
            .then(()=> {
              this.$router.push({
                name: 'home'
              })
            })
          // this.$delete(this.answers, this.answers.indexOf(answer))
          // this.userHasAnswered = false;
        }
        catch (err) {
          console.log(err)
        }
      }
  },
  created() {
    this.setBackHoverValue()
    this.getSong()
  },
}
</script>

<style scoped>
.divstyle {
  border: solid 2px #63ace5;
  border-radius: 5px;
}

.icon {
  height: 24px;
  weight: 24px;
  padding: 2px 2px 2px 2px  ;

}


</style>
