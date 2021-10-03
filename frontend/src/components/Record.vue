<template>
  <a-table :columns="columns" :data-source="data">
    <span slot="action" slot-scope="text, record">
      <a :id="record.id" @click="viewClick">View All</a>
    </span>
  </a-table>
</template>
<script>
const columns = [];

const data = [];
export default {

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
<style></style>
