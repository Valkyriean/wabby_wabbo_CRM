<template>
    <div>
        <li v-for="listData in lists" :key="listData.id">
            <a-table :columns="listData.columns" :data-source="listData.data">
            </a-table>
        </li>
    </div>
</template>

<script>
export default {
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
        .post("http://172.20.10.3:5000/form/checkcustomer", body)
        .then((response) => {
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
        });
  }
}
</script>