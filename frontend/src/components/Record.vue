<template>
      <a-table :columns="columns" :data-source="data">
        <span slot="action" slot-scope="text, record">
          <a :id="record.id" @click="viewClick">View All</a>
        </span>
      </a-table>
</template>
<script>

import Menu from "./Menu.vue";
import DashboardBar from "./DashboardBar.vue";
const columns = [];
const data = [];
export default {
  components:{
    Menu,
    DashboardBar,
  },

  data() {
    return {
      data,
      columns,
    };
  },
  mounted() {
      this.columns = []
      this.data = []
    const body = {
      form_id: localStorage.getItem("record_id"),
      jwt: localStorage.getItem("rememberMeToken")
    }
    this.axios
        .post('https://wabby-wabbo-crm.herokuapp.com/form/showresponse', body)
        .then((response) => {
          // console.log(response.data);
          if(response.data.status == "Success") {
            // set column names
            var columnNames = [];
            var counter = 0;
            response.data.field_list.forEach((item) => {
              this.columns.push({
                title: item,
                dataIndex: item.toLowerCase(),
                key: counter ++,
              });
              columnNames.push(item.toLowerCase());
            });
            // push action column
            this.columns.push({
              title: 'Action',
              key: 'action',
              scopedSlots: { customRender: 'action' },
            },)

            // set column data
            this.data = [];
            response.data.responses.forEach((item) => {
              var itemData = {key: item.response_id};
              for (let i = 0; i < columnNames.length; i ++) {
                itemData[columnNames[i]] = item.response[i];
              }
              itemData["id"] = item.customer_id;
              // console.log(itemData);
              this.data.push(itemData);
            });
          } else {
            localStorage.removeItem("rememberMeToken");
            this.$router.push("/app/login");
          }
        });
  },
  methods: {
    viewClick(event) {
      const id = event.target.id;
      localStorage.setItem("customer_id", id);
      this.$router.push("/app/customer");
    }
  }
};
</script>
<style scoped>
  #Record {
    height: 100%;
  }
  .list-content {
    margin-top: 10px;
  }
</style>
