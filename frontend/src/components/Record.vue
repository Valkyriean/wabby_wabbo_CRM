<template>
  <a-layout id="Record">
    <a-layout-sider style="background: #6495f2">
      <div class="logo">
        <img
          src="../assets/logo.png"
          alt=""
          style="width: 150px; height: 150px; margin: 15px; margin-left: 23px;"
        />
      </div>
      <Menu />
    </a-layout-sider>
    <a-layout-content class="list-content">
      <DashboardBar />
      <div class="place-holder" />
      <a-table :columns="columns" :data-source="data">
        <span slot="action" slot-scope="text, record">
          <a :id="record.id" @click="viewClick">View All</a>
        </span>
      </a-table>
    </a-layout-content>
  </a-layout>
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
    const body = {
      form_id: localStorage.getItem("record_id"),
      jwt: localStorage.getItem("rememberMeToken")
    }
    this.axios
        .post('http://172.20.10.3:5000/form/showresponse', body)
        .then((response) => {
          // console.log(response.data);
          if(response.data.status == "Success") {
            // set column names
            var columnNames = [];
            response.data.field_list.forEach((item) => {
              this.columns.push({
                title: item,
                dataIndex: item.toLowerCase(),
                key: item.toLowerCase(),
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
            window.location.href = "/app/login";
          }
        });
  },
  methods: {
    viewClick(event) {
      const id = event.target.id;
      localStorage.setItem("customer_id", id);
      window.location.href = "/app/customer";
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
