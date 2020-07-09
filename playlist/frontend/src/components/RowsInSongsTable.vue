<template>
  <tr @mouseleave= "deletehover = false;
                    edithover = false;
                    addhover = false;
                    saveEdithover = false;
                    undoEdithover = false"
      @dblclick= "setTitleArtistDuration">
    <th scope="row">{{songIndex}}</th>

    <!-- STATIC Rows, when it is not being edit -->
    <td v-if="!editRow">{{song.title}}</td>
    <td v-if="!editRow">{{song.artist}}</td>
    <td v-if="!editRow">{{setDuration(song.duration)}}</td>

    <!-- EDIT Rows, when it is being edit -->

    <td v-if="editRow"><form @submit.prevent="saveEdit"><input v-model="title" placeholder="enter title" type="text"></form></td>
    <td v-if="editRow"><form @submit.prevent="saveEdit"><input v-model="artist" placeholder="enter artist" type="text"></form></td>
    <td v-if="editRow"><form @submit.prevent="saveEdit"><input v-model="duration" placeholder="enter duration in sec" type="number"></form></td>

    <td>
      <ul v-if=!editRow class="nav">
        <!-- EDIT the song -->
        <li class="nav-item mx-1">
            <a class="pointer">
            <div @mouseover="edithover = true">
              <img v-if="!edithover" class="icon" alt="Edit" src="../assets/edit.svg">
            </div>
            <div @mouseleave="edithover = false">
              <img v-if="edithover" @click="setTitleArtistDuration" class="icon" alt="Edit" src="../assets/edit-hover.svg">
            </div>
          </a>
        </li>

        <!-- DELETE the song -->
        <li class="nav-item mx-1" >
          <div @mouseover="deletehover = true" >
            <a @click="deleteSong" href=""><img v-if="!deletehover" class="icon" alt="Edit" src="../assets/delete.svg"></a>
          </div>
          <div @mouseleave="deletehover = false">
            <a @click="deleteSong" href=""><img v-if="deletehover" class="icon" alt="Edit" src="../assets/delete-hover.svg"></a>
          </div>
        </li>

        <!-- ADD the song to a playlist-->
        <li class="nav-item mx-1" >
          <div @mouseover="addhover = true" data-toggle="modal" data-target="'#AddToPlaylistModal'+ songID" >
            <a  href=""><img class="icon" v-if="!addhover" @mouseover="addhover = true" alt="add to playlist" src="../assets/plus.svg"></a>
          </div>
          <div @mouseleave="addhover = false">
            <a data-toggle="modal" :data-target="'#Modal' + songID" @click="getPlaylists" href=""><img class="icon" v-if="addhover" @mouseover="addhover = true" alt="add to playlist" src="../assets/plus-hover.svg"></a>
          </div>

          <!-- Modal -->
          <div class="modal fade" :id="'Modal' + songID" tabindex="-1" role="dialog" aria-labelledby="exampleModalLabel" aria-hidden="true">
            <div class="modal-dialog">
              <div class="modal-content modal-style">
                <div class="modal-header">
                  <h5 class="modal-title" id="exampleModalLabel">{{song.title}} || {{song.artist}}</h5>
                  <button type="button" class="close" data-dismiss="modal" aria-label="Close">
                    <span aria-hidden="true">&times;</span>
                  </button>

                </div>
                <div class="modal-body">
                  <!-- Here is the content of the Model -->
                  <div class="row">
                    <div class="col-6">
                      <h5>Add Song to Playlist</h5>
                    </div>
                    <div class="col-6">
                      <h5>Remove Song from Playlist</h5>
                    </div>
                  </div>
                  <div class="row">

                    <!-- Add Song to Playlist -->

                    <div class="col-6">
                      <div class="btn-group-vertical">
                        <a  href=""
                            >
                          <button
                            v-for="playlist in PlaylistsNotInYet"
                            :key="playlist.id"
                            @click="AddToPlaylist(playlist.id)"
                            class="btn btn-outline-dark modal-style"
                            data-dismiss="modal"
                            >{{playlist.name}}
                          </button>
                        </a>
                      </div>
                    </div>

                    <!-- Remove Song from Playlist -->

                    <div class="col-6">
                      <div class="btn-group-vertical">
                        <a  href=""
                            >
                          <button
                            v-for="playlist in song.playlists"
                            :key="playlist.id"
                            @click="RemoveFromPlaylist(playlist.id)"
                            class="btn btn-outline-dark modal-style"
                            data-dismiss="modal"
                            >{{playlist.name}}
                          </button>
                        </a>
                      </div>
                    </div>
                  </div>

                  <!-- END Here ends the contend of the Modal -->
                </div>
              </div>
            </div>
          </div>
          <!-- Modal Ende-->

        </li>
      </ul>
      <!-- EDIT the SONG -->
      <ul v-if=editRow class="nav">

        <!-- Save the Change -->
        <li class="nav-item mx-1" >
          <div @mouseover="saveEdithover = true" @mouseleave="saveEdithover = false">
            <!-- no hover -->
              <img class="icon" v-if="!saveEdithover" alt="save" src="../assets/save.svg">
            <!-- hover -->
              <img class=" icon pointer" @click="saveEdit" v-if="saveEdithover" alt="save" src="../assets/save-hover.svg">
          </div>
        </li>
        
        <!-- Discard changes -->
        <li class="nav-item mx-1" >
          <div @mouseover="undoEdithover = true" @mouseleave="undoEdithover = false">
            <!-- no hover -->
              <img v-if="!undoEdithover" class="icon" alt="save" src="../assets/undo.svg">
            <!-- hover -->
              <img v-if="undoEdithover" class="icon pointer" @click="editRow=!editRow" alt="save" src="../assets/undo-hover.svg">
          </div>
        </li>
      </ul>

    </td>
  </tr>

</template>

<script>
import { apiService } from "@/common/api.service.js"
export default {
  name: 'RowInSongsTable',
  props: {
    id: Number,
    index: Number,
  },
  data() {
    return {
      playlists: [],
      song: [],
      songID: this.id,
      songIndex: this.index,
      edithover: false,
      deletehover: false,
      plushover: false,
      minushover: false,
      addhover: false,
      editRow: false,
      saveEdithover: false,
      undoEdithover: false,
      error: null,
      title: null,
      artist: null,
      duration: null,
    }
  },
  methods: {

    getSong() {
      let endpoint = `/api/users-songs/${this.songID}/`;
      apiService(endpoint)
      .then(data => {
        this.song=data
      })
    },
    getPlaylists() {
      let endpoint = "/api/users-playlists/";
      apiService(endpoint)
      .then(playlists => {

        this.playlists=playlists;
      })
    },
    async saveEdit() {
      console.log("saveEdit wurde gedrückt");
      if(!this.title){
        console.log('if(!this.title){');
        this.error = "You cannot send an empty title!";
      } else if (this.title.length > 240) {
      this.error = "Ensure this field has no more than 240 char ";
      }  else {
        let endpoint = `/api/songs/${this.songID}/`;
        let  method = "PUT";
        await apiService(endpoint, method, { title: this.title, artist: this.artist, duration: this.duration})
        .then(

        )
      }
      this.editRow = false;
      this.getSong();
    },
    setBackHoverValue() {
      this.edithover= false;
      this.deletehover= false;
      this.plushover= false;
      this.minushover= false;
      this.saveEdithover= false;

    },
    setDuration(duration) {
      if (duration == null) {
        return ''
      }
      var sec = duration % 60 ;
      var min = (duration-sec)/60;
      if (sec < 10){
        sec= '0' + sec
      }
      if (sec==0){
        sec= '00'
      }

      return min + ':' + sec
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
      },
      async AddToPlaylist(p_pk) {
          let endpoint = `/api/users-add-remove-song/${p_pk}/${this.songID}/`;
          try {
            await apiService(endpoint, "POST")
              .then(()=> {
                this.getSong()
              })
            // this.$delete(this.answers, this.answers.indexOf(answer))
            // this.userHasAnswered = false;
          }
          catch (err) {
            console.log(err)
          }
        },
        async RemoveFromPlaylist(p_pk) {
            let endpoint = `/api/users-add-remove-song/${p_pk}/${this.songID}/`;
            try {
              await apiService(endpoint, "DELETE")
                .then(()=> {
                  this.getSong()
                })
              // this.$delete(this.answers, this.answers.indexOf(answer))
              // this.userHasAnswered = false;
            }
            catch (err) {
              console.log(err)
            }
        },
      setTitleArtistDuration() {
        this.title = this.song.title;
        this.artist = this.song.artist;
        this.duration = this.song.duration;
        this.editRow = true;
      },
    },
  created() {
    this.getSong()
    this.setBackHoverValue()
  },
  // Hier fängt computed an
  computed: {
    PlaylistsNotInYet() {
      var addPlaylist = []

      var playlists_ids = this.song.playlists_ids;
      this.playlists.forEach(function (playlist) {
        if(!playlists_ids.includes(playlist.id)) {
          addPlaylist.push(playlist);
        }
      });
      return addPlaylist;
    },

  },
  // hier hört computed auf
}
</script>

<style scoped>
table, th, td {
  border: 1px solid #63ace5 !important;
  border-collapse: collapse;
}
.icon {
  height: 24px;
  weight: 24px;
  padding: 2px 2px 2px 2px  ;
}
.modal-style {
  background-color: #4a4e4d;
  color: #63ace5;
}

input:not(.userListBox){
  background:transparent !important;
  border: none !important;
  outline: none !important;
  padding: 0px 0px 0px 0px !important;
  color: #63ace5;
}
.pointer{
  /* https://stackoverflow.com/questions/3087975/make-the-cursor-a-hand-when-a-user-hovers-over-a-list-item */
  cursor: pointer;
 }
</style>
