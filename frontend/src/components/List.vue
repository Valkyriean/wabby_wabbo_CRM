<template>
  <a-list :grid="{ gutter: 16, column: 4 }" :data-source="data">
    <a-list-item slot="renderItem" slot-scope="item">
      <a-card :title="item.title">
        Card content
      </a-card>
    </a-list-item>
  </a-list>
</template>
<script>
const data = [
  {
    title: 'Title 1',
  },
  {
    title: 'Title 2',
  },
  {
    title: 'Title 3',
  },
  {
    title: 'Title 4',
  },
];
export default {
  data() {
    return {
      data,
    };
  },
  mounted() {
    console.log('Hiiii');
    localStorage.setItem("halo", "hiiiii");
    const abc = localStorage.getItem('halo');
    console.log(abc);
    if(localStorage.getItem("rememberMeToken")){
      console.log("exists");
      this.axios
          .post("/dashboard/", {
            jwt: localStorage.getItem("rememberMeToken"),
          })
          .then((response) => {
            putResponse(response.data);
          });
    }
  },
  putResponse(res) {
    console.log(response.data);
  },
};
</script>
<style></style>
