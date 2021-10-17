<template>
  <div>
          <div class="form-content">
            <div class="form-title">
              <a-row>
                <div class="title-text">
                  Title
                </div>
              </a-row>
              <a-row>
                <a-input id="title" v-model="title" size="large" style="margin-left: -1%"/>
              </a-row>
              <a-row>
                <div class="description-text">
                  Description
                </div>
              </a-row>
              <a-row>
                <a-textarea placeholder="Please write your description" auto-size style="margin-left: -1%" v-model="description"/>
              </a-row>
              <br />
              <a-row>
                <a-row class="anonymous-position">
                  <a-col :span="4">
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
                  <div class="question-name">
                    Your Name
                  </div>
                </a-row>
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
                    <div class="question-name">
                      Question {{listItem.key + 1}}
                    </div>
                  </a-row>
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
  </div>
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
      let index = 0;
      for(let i = 0; i < this.listData.length; i ++) {
        if(this.listData[i].key == event.target.id) {
          index = i;
        };
      };
      this.listData.splice(index, 1);
    },
    requiredClick() {
      console.log(this.listData);
    },
    typeChange(value) {
      const data = value.split(";");
      var index = -1;
      for(let i = 0; i < this.listData.length; i ++) {
        if(this.listData[i].key == parseInt(data[0])) {
          index = i;
        };
      };
      if(data[1] == "1") {
        this.listData[index].type = "multipleChoice";
        this.listData[index].choiceKey = 0;
        this.listData[index].choice = [{value: "option0", key: 0}];
      } else {
        this.listData[index].type = "shortAnswer";
      }
    },
    addChoiceClick(event) {
      var index = -1;
      for(var i = 0; i < this.listData.length; i ++) {
        if(this.listData[i].key == event.target.id) {
          index = i;
        };
      };

      this.listData[index].choiceKey += 1;
      this.listData[index].choice.push({
        value: "option" + this.listData[index].choiceKey, 
        key: this.listData[index].choiceKey
      });
    },
    deleteChoiceClick(event) {
      const keys = event.target.id.split(";");
      var index = -1;
      var question_index = -1;
      for(let i = 0; i < this.listData.length; i ++) {
        if(this.listData[i].key == keys[0]) {
          question_index = i;
        }
      }
      for(let i = 0; i < this.listData[question_index].choice.length; i ++) {
        if(this.listData[question_index].choice[i].key == keys[1]) {
          index = i;
        };
      };
      this.listData[question_index].choice.splice(index, 1);
      // console.log(this.listData[question_index].choice);
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
        body.field_list.unshift({
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
    margin-left: 2%;
  }
  .control-buttons {
    margin-left: 45%;
    margin-top: 20px;
  }
  .title-text {
    font-size: 16px;
    margin-bottom: 1%;
  }
  .description-text {
    font-size: 16px;
    margin-top: 1%;
    margin-bottom: 1%;
  }
  .anonymous-position {
    margin-left: 41%;
  }
  .question-name {
    margin-bottom: 1%;
    margin-top: -4px;
  }
</style>