<template>
        <a-table :columns="columns" :data-source="data">
            <span slot="action" slot-scope="text, record">
            <a :id="record.key" @click="viewClick">View All</a>
            </span>
        </a-table>
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
            columns: [
                {
                    title: "Name",
                    dataIndex: "name",
                    key: "name",
                },
                {
                    title: 'Action',
                    key: 'action',
                    scopedSlots: { customRender: 'action' },
                }
            ],
            data: [],
        }
    },
    mounted() {
        const body = {
            customer_id: localStorage.getItem("customer_id"),
            jwt: localStorage.getItem("rememberMeToken")
        };
        this.axios
            .post("https://wabby-wabbo-crm.herokuapp.com/form/getcustomer", body)
            .then((response) => {
                console.log(response.data.responses);
                if(response.data.status == "Success") {
                    response.data.responses.forEach((item) => {
                        var itemData = {
                                key: item.customer_id,
                                name: item.name,
                            };
                        this.data.push(itemData);
                    });
                } else {
                    localStorage.removeItem("rememberMeToken");
                    window.location.href = "/app/login";
                }
            })
    },
    methods: {
        viewClick(event) {
            const id = event.target.id;
            localStorage.setItem("customer_id", id);
            // console.log(event.target.id)
            window.location.href = "/app/customer";
        }
    }
};
</script>

<style scoped>
  #clients {
    height: 100%;
  }
  .list-content {
    margin-top: 10px;
  }
</style>