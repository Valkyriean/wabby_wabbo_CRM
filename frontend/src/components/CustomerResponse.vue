<template>
    
</template>

<script>
    export default {
        data() {
            return {
                url,
            }
        },
        mounted() {
            this.url = window.location.href;
            console.log(this.url);
        }
    }
</script>