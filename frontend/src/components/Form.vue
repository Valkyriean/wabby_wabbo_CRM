<template>
  <a-list :grid="{ gutter: 16, column: 3 }" :data-source="data">
    <a-list-item slot="renderItem" slot-scope="item">
      <a-card :id="item.id">
        <a-card-meta :id="item.id">
          <a-row slot="title" >
            <a-col :span="8">
              <div :id="item.id" @click="cardClick" class="itemTitle">
                {{ item.title }}
              </div>
            </a-col>
            <a-col :span="10">
              <a-button :id="item.id" @click="URLClick" style="margin-top: -2%; margin-left: 15%" type="link">
                Copy URL
              </a-button>
            </a-col>
            <a-col :span="3">
              <a-button :id="item.id" @click="deleteClick" type="danger" style="margin-top: -5%;">
                Delete
              </a-button>
            </a-col>
          </a-row>
          <div slot="description" :id="item.id" @click="cardClick">
            {{ item.content }}
          </div>
        </a-card-meta>
      </a-card>
    </a-list-item>
  </a-list>
</template>
<script>
const data = [];
export default {
  data() {
    return {
      data,
    };
  },
  mounted() {
    // console.log('Hiiii');
    // localStorage.setItem("halo", "hiiiii");
    // const abc = localStorage.getItem('halo');
    // console.log(abc);
    if (localStorage.getItem("rememberMeToken")) {
      // console.log("exists");
      this.axios
        .post("https://wabby-wabbo-crm.herokuapp.com/dashboard/", {
          jwt: localStorage.getItem("rememberMeToken"),
        })
        .then((response) => {
          console.log(response.data);
          this.data = [];
          if (response.data.status == "Success") {
            response.data.forms.forEach((item) => {
              var title = item.name.length > 12 ? item.name.substr(0, 12) + '...' : item.name;
              var content = item.description.length > 30 ? item.description.substr(0, 30) + '...' : item.description;
              content = content.length == 0 ? "no description" : content;
              this.data.push({
                title: title,
                content: content,
                id: item.form_id,
              });
            });
          } else {
            localStorage.removeItem("rememberMeToken");
            this.$router.push("/app/login");
          }
          // putResponse(response.data);
          console.log(this.data);
        });
    }
  },
  methods: {
    cardClick(event) {
      localStorage.setItem("record_id", event.target.id);
      this.$router.push("/app/record");
    },
    URLClick(event) {
      this.$copyText("https://wabby-wabbo-crm.herokuapp.com/app/form/" + event.target.id)
          .then((e) => { alert('Copy Success') }, (e) => { alert('Copy Failed') });
    },
    deleteClick(event) {
      this.axios
          .post("https://wabby-wabbo-crm.herokuapp.com/dashboard/deleteform", 
          {
            jwt: localStorage.getItem("rememberMeToken"),
            form_id: event.target.id,
          })
          .then((response) => {
            if(response.data.status == "Success") {
              // location.reload();
              for(let i = 0; i < this.data.length; i ++) {
                if(this.data[i].id == event.target.id) {
                  var index = i;
                }
              }
              this.data.splice(index, 1);
            } else {
              alert("Failed to delete " + response.data.status);
            };
          })
    }
  },
};
</script>

<style scoped>
</style>