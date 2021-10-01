<template>
  <a-table :columns="columns" :data-source="data">
    <a slot="name" slot-scope="text">{{ text }}</a>
    <span slot="customTitle"><a-icon type="smile-o" /> Name</span>
    <span slot="tags" slot-scope="tags">
      <a-tag
        v-for="tag in tags"
        :key="tag"
        :color="tag === 'loser' ? 'volcano' : tag.length > 5 ? 'geekblue' : 'green'"
      >
        {{ tag.toUpperCase() }}
      </a-tag>
    </span>
    <span slot="action" slot-scope="text, record">
      <a>Invite 一 {{ record.name }}</a>
      <a-divider type="vertical" />
      <a>Delete</a>
      <a-divider type="vertical" />
      <a class="ant-dropdown-link"> More actions <a-icon type="down" /> </a>
    </span>
  </a-table>
</template>
<script>
const columns = [
  {
    dataIndex: 'name',
    key: 'name',
    slots: { title: 'customTitle' },
    scopedSlots: { customRender: 'name' },
  },
  {
    title: 'Age',
    dataIndex: 'age',
    key: 'age',
  },
  {
    title: 'Address',
    dataIndex: 'address',
    key: 'address',
  },
  {
    title: 'Tags',
    key: 'tags',
    dataIndex: 'tags',
    scopedSlots: { customRender: 'tags' },
  },
  {
    title: 'Action',
    key: 'action',
    scopedSlots: { customRender: 'action' },
  },
];

const data = [
  {
    key: '1',
    name: 'John Brown',
    age: 32,
    address: 'New York No. 1 Lake Park',
    tags: ['nice', 'developer'],
  },
  {
    key: '2',
    name: 'Jim Green',
    age: 42,
    address: 'London No. 1 Lake Park',
    tags: ['loser'],
  },
  {
    key: '3',
    name: 'Joe Black',
    age: 32,
    address: 'Sidney No. 1 Lake Park',
    tags: ['cool', 'teacher'],
  },
];
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
          this.columns = [];
          var columnNames = [];
          response.data.field_list.forEach((item) => {
            this.columns.push({
              title: item[0],
              dataIndex: item[0].toLowerCase(),
              key: item[0].toLowerCase(),
            });
            columnNames.push(item[0].toLowerCase());
          });
          this.data = [];
          response.data.responses.forEach((item) => {
            var itemData = {key: item.response_id};
            for (let i = 0; i < columnNames.length; i ++) {
              itemData[columnNames[i]] = item.response[i];
            }
            console.log(itemData);
            this.data.push(itemData);
          });

          response.data.responses.forEach((item) => {
            console.log(item.customer_id);
          });
        });
  },
  methods: {

  }
};
</script>
<style></style>
