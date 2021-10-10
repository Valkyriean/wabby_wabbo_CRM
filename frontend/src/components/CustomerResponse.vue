<template>
    
</template>

<script>
    export default {
        data() {
            return {
                formId,
            }
        },
        mounted() {
            console.log(this.$route.params);
            this.formId = this.$route.params.formId;
        }
    }
</script>