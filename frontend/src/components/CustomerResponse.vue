<template>
    <div class="outer-wrapper">
        <a-form v-if="status" layout="vertical" :form="form">
            <li v-for="question in fieldList" :key="question.id">
                <a-form-item 
                    v-if="question.type == 'shortAnswer'" 
                    :label="question.question_name" 
                    :validate-status="question.validate"
                    :help="question.help"
                >
                    <a-input 
                        placeholder="" 
                        v-model="question.answer"
                        :id="question.id"
                        @change="shortAnswerChange(question.id)"
                    />
                </a-form-item>
                <a-form-item v-else :label="question.question_name">
                    <a-radio-group v-model="question.answer">
                        <li v-for="option in question.choice" :key="option.key">
                            <a-radio :style="radioStyle" :value="option.key">
                                {{ option.value }}
                            </a-radio>
                        </li>
                    </a-radio-group>
                </a-form-item>
            </li>
            <a-form-item>
                <a-button type="primary" @click="submitClick">
                    Submit
                </a-button>
            </a-form-item>
        </a-form>
        <div v-else>

        </div>
    </div>
</template>

<script>
    export default {
        data() {
            return {
                formId: "",
                fieldList: [],
                form: this.$form.createForm(this, {name: 'form'}),
                radioStyle: {
                    display: 'block',
                    height: '30px',
                    lineHeight: '30px',
                },
                status: true,
            }
        },
        mounted() {
            // console.log(this.$route.params);
            this.formId = this.$route.params.id;
            this.axios
                .post('https://wabby-wabbo-crm.herokuapp.com/form/getform', {
                    form_id: this.formId,
                })
                .then((response) => {
                    // console.log(response.data);
                    if(response.data.status == "Success") {
                        var id = 0;
                        response.data.field_list.forEach((item) => {
                            var questionItem = item;
                            questionItem["id"] = id ++;
                            questionItem["answer"] = "";
                            questionItem["validate"] = "success";
                            questionItem["help"] = "";
                            this.fieldList.push(questionItem);
                        });
                    } else {
                        this.status = false;
                    };
                });
        },
        methods: {
            shortAnswerChange(id) {
                // console.log(id);
                // console.log(this.fieldList[id]);
                if(this.fieldList[id].required && this.fieldList[id].answer == "") {
                    this.fieldList[id].validate = "error";
                    this.fieldList[id].help = "This question is required!";
                } else {
                    this.fieldList[id].validate = "success";
                    this.fieldList[id].help = "";
                };
            },
            submitClick() {
                var res = []
                this.fieldList.forEach((item) => {
                    res.push(item.answer);
                });
                this.axios
                    .post('https://wabby-wabbo-crm.herokuapp.com/form/saveresponse', {
                        form_id: this.formId,
                        response_list: res
                    })
                    .then((response) => {
                        if(response.data.status == "Success") {
                            console.log("Success");
                            // this.$router.push('/app/form/finished');
                        }
                    })
                    .catch((error) => {
                        console.log(error);
                    })
            },
        }
    }
</script>
<style scoped>
    .outer-wrapper {
        margin: 5%;
    }
</style>