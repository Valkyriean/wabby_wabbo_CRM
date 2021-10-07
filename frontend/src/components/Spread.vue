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
        <li v-for="listData in lists" :key="listData.id">
            <a-table :columns="listData.columns" :data-source="listData.data">
            </a-table>
        </li>
      </a-layout-content>
    </a-layout>
</template>

<script>
import Menu from "./Menu.vue";
import DashboardBar from "./DashboardBar.vue";

export default {
  components:{
    Menu,
    DashboardBar,
  },

  data() {
    return {
        lists: []
    };
  },
  mounted() {
    const body = {
      customer_id: localStorage.getItem("customer_id"),
      jwt: localStorage.getItem("rememberMeToken")
    };

    this.axios
        .post("https://wabby-wabbo-crm.herokuapp.com/form/checkcustomer", body)
        .then((response) => {
            if(response.data.status == "Success") {
                response.data.responses.forEach((item) => {
                    let itemData = {
                        id: item.response_id,
                        columns: [],
                        data: []
                    };
                    // set column names
                    var columnNames = [];
                    item.field_list.forEach((fieldName) => {
                        itemData.columns.push({
                            title: fieldName,
                            dataIndex: fieldName.toLowerCase(),
                            key: fieldName.toLowerCase(),
                        });
                        columnNames.push(fieldName.toLowerCase())
                    });
                    // set column data
                    var _data = {key: item.response_id};
                    for (let i = 0; i < columnNames.length; i ++) {
                        _data[columnNames[i]] = item.response[i];
                    }
                    itemData.data.push(_data);
                    this.lists.push(itemData);
                })
                console.log(this.lists);
            } else {
                localStorage.removeItem("rememberMeToken");
                window.location.href = "/app/login";
            }
        });
  }
}
</script>
<style scoped>
  #Record {
    height: 100%;
  }
  .list-content {
    margin-top: 10px;
  }
</style>