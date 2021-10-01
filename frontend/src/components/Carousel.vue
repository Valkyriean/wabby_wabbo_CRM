<template>
  <a-carousel>
      <img src="../assets/1.jpg" class="carousel-image"/>
      <img src="../assets/2.jpg" class="carousel-image"/>
      <img src="../assets/3.jpg" class="carousel-image"/>
      <img src="../assets/4.jpg" class="carousel-image"/>
  </a-carousel>
</template>
<script>
export default {};
</script>
<style scoped>
/* For demo */
.ant-carousel >>> .slick-slide {
  text-align: center;
  height: 600px;
  background: #364d79;
  overflow: hidden;
}

.ant-carousel >>> .slick-slide img {
  display: block;
  margin: auto;
}

.carousel-image {
  width: 100%;
}
</style>
