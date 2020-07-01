<template>
  <div class="home">
    <div class="centerthecontext">
      <h1>All Songs</h1>
      <h3 class="lead"> Here are all the songs available</h3>
      <hr class="blueline">
    </div>

    <table class="table table-hover table-borderless">
      <thead v-if="!showaddSong && !StartedAdding" @mouseover="showaddSong = true">
        <tr>
          <th scope="col">#</th>
          <th scope="col">Title</th>
          <th scope="col">Artist</th>
          <th scope="col">Duration</th>
          <th scope="col">Function</th>
        </tr>
      </thead>
      <tbody>
        <!-- add new Song to Database -->
        <tr v-if="showaddSong || StartedAdding" @mouseleave="showaddSong = false">
            <th class="likeplaceholer" scope="row">{{songs_ids.length+1}}</th>
            <td><input v-model="title" placeholder="enter title" type="text"></td>
            <td><input v-model="artist" placeholder="enter artist" type="text"></td>
            <td><input v-model="duration" placeholder="enter duration in sec" type="number"></td>
            <td>

                <ul class="nav">
                  <!-- Add the song -->
                  <li class="nav-item mx-1">
                    <div @mouseover="addhover = true" >
                      <a @click="onSubmit" href=""><img v-if="!addhover" class="icon" alt="Edit" src="../assets/add.svg"></a>
                    </div>
                    <div @mouseleave="addhover = false">
                      <a @click="onSubmit" href=""><img v-if="addhover" class="icon" alt="Edit" src="../assets/add-hover.svg"></a>
                    </div>
                  </li>
                    <!-- delete, what you have added so far -->
                  <li class="nav-item mx-1" v-if="StartedAdding">
                    <div @mouseover="deletehover = true" >
                      <a @click="deleteAdding" href=""><img v-if="!deletehover" class="icon" alt="Edit" src="../assets/delete.svg"></a>
                    </div>
                    <div @mouseleave="deletehover = false" >
                      <a @click="deleteAdding" href=""><img v-if="deletehover" class="icon" alt="Edit" src="../assets/delete-hover.svg"></a>
                    </div>
                  </li>
                </ul>
            </td>
        </tr>

        <RowInSongsTable
              v-for="(song, index) in songs_ids"
              :key="song.id"
              :id="song.id"
              :index="(songs_ids.length+1) - (index+1)">

        </RowInSongsTable>

        <tr class="noborder">
            <th  scope="row">#</th>
            <td class="noborder"><input disabled ></td>
            <td class="noborder"><input disabled ></td>
            <td class="noborder"><input disabled ></td>
            <td class="noborder">Function</td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script>
import { apiService } from "@/common/api.service.js"
import RowInSongsTable from "@/components/RowsInSongsTable"
export default {
  name: 'Home',
  components: {
    RowInSongsTable,
  },
  data() {
    return {
      songs: [],
      songs_ids: [],
      title: '',
      artist: '',
      duration: '',
      showaddSong: false,
      addhover: false,
      deletehover: false,
    }
  },
  computed: {
    //check, if the user started adding new data
    StartedAdding() {
      if(this.title != '' || this.artist != '' || this.duration != '') {
        return true
      } else {
        return false
      }

    }
  },
  methods: {
    deleteAdding() {
      this.title = '';
      this.artist= '';
      this.duration= '';
    },
    getSongs() {
      // let endpoint = "/api/songs-ids/";
      let endpoint = "/api/songs/";

      apiService(endpoint)
      .then(data => {
        this.songs=data
      })
    },
    getSongsIDs() {
      // let endpoint = "/api/songs-ids/";
      let endpoint = "/api/songs-ids/";

      console.log('Songs IDs are beeing fetched')
      apiService(endpoint)
      .then(data => {
        console.log("data aus HOME: ");
        console.log(data);
        this.songs_ids=data
      })
    },
    async onSubmit(){
        if(!this.title){
          this.error = "You cannot send an empty title!";
        } else if (this.title.length > 240) {
        this.error = "Ensure this field has no more than 240 char ";
        }  else {
          let endpoint = "/api/songs/";
          let method = "POST";

          await apiService(endpoint, method, {  title: this.title,
                                                artist: this.artist,
                                                duration: this.duration})
          .then(
            this.$router.push({
              name: 'home'
            })
          )
        }
      }
  },
  created() {
    this.getSongsIDs()
  }
}
</script>

<style scoped>

input:not(.userListBox){
  background:transparent !important;
  border: none !important;
  outline: none !important;
  padding: 0px 0px 0px 0px !important;
  color: #63ace5;
}

table, th, td {
  border: 1px solid #63ace5 !important;

}
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
  height: 22px;
  weight: 22px;

}
.icon:hover {
  color: #e7eff6;
}
::placeholder {
  color: #63ace5;
  opacity: 0.5;
}
.likeplaceholer {
  color: #63ace5;
  opacity: 0.5;
}
.noborder {
  border: solid 2px #4a4e4d !important;
  color: #4a4e4d;
}
.noborder:hover {
  border: solid 2px #4a4e4d !important;
  background:transparent !important;
  color: #4a4e4d;
}
</style>
