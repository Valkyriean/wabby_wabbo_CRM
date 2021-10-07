<template>
  <a-list :grid="{ gutter: 16, column: 4 }" :data-source="data">
    <a-list-item slot="renderItem" slot-scope="item">
      <a-card :id="item.id">
        <a-card-meta :id="item.id">
          <div slot="title" :id="item.id" @click="cardClick">
            {{ item.title }}
          </div>
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
      console.log("exists");
      this.axios
        .post("http://172.20.10.3:5000/dashboard/", {
          jwt: localStorage.getItem("rememberMeToken"),
        })
        .then((response) => {
          console.log(response.data);
          this.data = [];
          if (response.data.status == "Success") {
            response.data.forms.forEach((item) => {
              this.data.push({
                title: item.name,
                content: item.description,
                id: item.form_id,
              });
            });
          } else {
            localStorage.removeItem("rememberMeToken");
            window.location.href = "/app/login";
          }
          // putResponse(response.data);
          console.log(this.data);
        });
    }
  },
  methods: {
    cardClick(event) {
      console.log(event.target.id);
      localStorage.setItem("record_id", event.target.id);
      window.location.href = "/app/record";
    },
  },
};
</script>


<style></style>
