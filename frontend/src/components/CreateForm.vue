<template>
  <a-layout id="form">
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
          <div class="form-content">
            <div class="form-title">
              <a-row>
                <a-input id="title" v-model="title" size="large" style="margin-left: -1%"/>
              </a-row>
              <a-row>
                <a-textarea placeholder="Please write your description" auto-size style="margin-left: -1%" v-model="description"/>
              </a-row>
              <br />
              <a-row>
                <a-row>
                  <a-col :span="2">
                    <div>Anonymous</div>
                  </a-col>
                  <a-col :span="2">
                    <a-switch v-model="anonymous" />
                  </a-col>
                </a-row>
              </a-row>
            </div>
          </div>
          <br v-show="anonymous == false"/>
          <a-card v-show="anonymous == false" style="width: 90%; margin-left: 5%;">
            <a-card-meta>
              <div slot="title">
                <a-row>
                  <a-col :span="12">
                    <a-input value="Name" size="large" disabled/>
                  </a-col>
                  <a-col :span="12">
                      <a-row>
                        <a-col :span="15">
                          <a-select :default-value="2" @change="typeChange" style="margin-top: 3px; margin-left: 2%;" disabled>
                            <a-select-option :value="1">
                              Multiple Choice
                            </a-select-option>
                            <a-select-option :value="2">
                              Short Answer
                            </a-select-option>
                          </a-select>
                          <a-button icon="delete" @click="deleteQuestionClick" style="margin-left: 2%;" disabled/>
                        </a-col>
                        <a-col :span="4" style="margin-top: 5px">
                          <div>Required</div>
                        </a-col>
                        <a-col :span="2" style="margin-top: 5px">
                          <a-switch default-checked @click="requiredClick" disabled/>
                        </a-col>
                      </a-row>
                    </a-col>
                </a-row>
              </div>
            </a-card-meta>
          </a-card>
          <li v-for="listItem in listData" :key="listItem.key">
            <a-card style="width: 90%; margin-left: 5%;">
              <a-card-meta>
                <div slot="title">
                  <a-row>
                    <a-col :span="12">
                      <a-input v-model="listItem.title" size="large"/>
                    </a-col>
                    <a-col :span="12">
                      <a-row>
                        <a-col :span="15">
                          <a-select :default-value="listItem.key + ';' + 1" @change="typeChange" style="margin-left: 2%; margin-top: 3px">
                            <a-select-option :value="listItem.key + ';' + 1">
                              Multiple Choice
                            </a-select-option>
                            <a-select-option :value="listItem.key + ';' + 2">
                              Short Answer
                            </a-select-option>
                          </a-select>
                          <a-button icon="delete" @click="deleteQuestionClick" :id="listItem.key" style="margin-left: 2%;"/>
                        </a-col>
                        <a-col :span="4" style="margin-top: 5px">
                          <div>Required</div>
                        </a-col>
                        <a-col :span="2" style="margin-top: 5px">
                          <a-switch v-model="listItem.required" @click="requiredClick"/>
                        </a-col>
                      </a-row>
                    </a-col>
                  </a-row>
                  <a-row>
                    <div v-if="listItem.type == 'multipleChoice'">
                      <li v-for="choice in listItem.choice" :key="choice.key">
                        <a-row>
                          <a-col :span="22">
                            <a-input v-model="choice.value" />
                          </a-col>
                          <a-col :span="1">
                            <a-button icon="delete" @click="deleteChoiceClick" :id="listItem.key + ';' + choice.key" />
                          </a-col>
                        </a-row>
                      </li>
                      <a-button icon="plus-circle" @click="addChoiceClick" :id="listItem.key"/>
                    </div>
                    <div v-else>
                    </div>
                  </a-row>
                </div>
              </a-card-meta>
            </a-card>
          </li>
          <div class="control-buttons">
            <a-button icon="plus-circle" @click="addClick" style="margin-right: 2%;"/>
            <a-button @click="submitClick">
              Submit
            </a-button>
          </div>
        </a-layout-content>
    </a-layout>
</template>

<script>
import Menu from "./Menu.vue";
import DashboardBar from "./DashboardBar.vue";
export default {
  components: {
    Menu,
    DashboardBar,
  },
  data() {
    return {
      title: "Untitled Form",
      listData: [],
      key: 0,
      anonymous: false,
      description: "",
    }
  },
  mounted() {
    // check if token expired
  },
  methods: {
    addClick() {
      this.listData.push({
        key: this.key ++, 
        type: "multipleChoice", 
        title: "Untitled question", 
        required: false,
        choice: [{value: "option0", key: 0}],
        choiceKey: 0,
      });
    },
    deleteQuestionClick(event) {
      let index = -1;
      for(let i = 0; i < this.listData.lenth; i ++) {
        if(this.listData[i].key == event.target.id) {
          index = key;
        }
      }
      this.listData.splice(index, 1);
    },
    requiredClick() {
      console.log(this.listData);
    },
    typeChange(value) {
      console.log(value);
      const data = value.split(";");
      if(data[1] == "1") {
        this.listData[parseInt(data[0])].type = "multipleChoice";
        this.listData[parseInt(data[0])].choiceKey = 0;
        this.listData[parseInt(data[0])].choice = [{value: "option0", key: 0}];
      } else {
        this.listData[parseInt(data[0])].type = "shortAnswer";
      }
    },
    addChoiceClick(event) {
      this.listData[event.target.id].choiceKey += 1;
      this.listData[event.target.id].choice.push({
        value: "option" + this.listData[event.target.id].choiceKey, 
        key: this.listData[event.target.id].choiceKey
      });
      console.log(event.target.id);
    },
    deleteChoiceClick(event) {
      const keys = event.target.id.split(";");
      let index = -1;
      for(let i = 0; i < this.listData[keys[0]].choice.length; i ++) {
        if(this.listData[keys[0]].choice[i].key == keys[1]) {
          index = i;
        };
      };
      this.listData[keys[0]].choice.splice(index, 1);
      console.log(this.listData[keys[0]].choice);
    },
    // anonymousClick(value) {
    //   if(value) {
    //     this.listData.unshift({
    //       key: this.key ++,
    //       type: "shortAnswer",
    //       title: "Name",
    //       required: true,
    //       choice: [],
    //       choiceKey: 0
    //     })
    //   }
    // },
    submitClick(event) {
      let body = {
        jwt: localStorage.getItem("rememberMeToken"),
        name: this.title,
        description: this.description,
        anonymous: this.anonymous,
        field_list: []
      };
      this.listData.forEach((question) => {
        let questionData = {
          question_name: question.title,
          type: question.type,
          required: question.required
        };
        if(question.type == "multipleChoice") {
          questionData["choice"] = question.choice;
        };
        body.field_list.push(questionData);
      });
      if(this.anonymous == false) {
        body.field_list.push({
          question_name: "Name",
          type: "shortAnswer",
          required: true
        });
      };
      this.axios
          .post("https://wabby-wabbo-crm.herokuapp.com/dashboard/createform", body)
          .then((response) => {
            console.log(response.data);
            if(response.data.status == "Success") {
              window.location.href = "/app/dashboard";
            };
          });
    }
  }
}
</script>
<style scoped>
  #form {
    height: 100%;
  }
  .list-content {
    margin-top: 10px;
  }
  .form-content {
    margin-left: 8%;
    margin-top: 10px;
  }
  .form-title {
    margin-right: 8%;
  }
  .control-buttons {
    margin-left: 45%;
    margin-top: 20px;
  }
</style>