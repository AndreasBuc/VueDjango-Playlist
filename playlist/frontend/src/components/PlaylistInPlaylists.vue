<template>
<div class="PlaylistInPlaylists">
  <div class="row">
    <div class="col-6">
      <p>{{PlaylistName}}</p>
    </div>

    <div class="col-6 d-flex justify-content-end">
      <!-- DELETE the Playlist -->
      <div @mouseover="deletehover = true" >
        <a @click="deletePlaylist" href=""><img v-if="!deletehover" class="icon" alt="Edit" src="../assets/delete.svg"></a>
      </div>
      <div @mouseleave="deletehover = false">
        <a @click="deletePlaylist" href=""><img v-if="deletehover" class="icon" alt="Edit" src="../assets/delete-hover.svg"></a>
      </div>
    </div>



  </div>
</div>



</template>

<script>
import { apiService } from "@/common/api.service.js"
export default {
  name: 'PlaylistInPlaylists',
  props: {
    PlaylistName: String,
    PlaylistID: Number,
  },
  data() {
    return {
      name: this.PlaylistName,
      id: this.PlaylistID,
      deletehover: false,
    }
  },
  methods: {
    setBackHoverValue() {
      this.deletehover= false;
    },
    async deletePlaylist() {
        let endpoint = `/api/users-playlists/${this.id}/`;
        try {
          await apiService(endpoint, "DELETE")
            .then(()=> {
              this.$router.push({
                name: 'my-playlist'
              })
            })
          // this.$delete(this.answers, this.answers.indexOf(answer))
          // this.userHasAnswered = false;
        }
        catch (err) {
          console.log(err)
        }
      },
  },
  created() {
    this.setBackHoverValue()
  },
}
</script>

<style scoped>
.icon {
  height: 24px;
  weight: 24px;
  padding: 2px 2px 2px 2px  ;
}
</style>
