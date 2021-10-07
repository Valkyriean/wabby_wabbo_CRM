<template>
  <a-carousel autoplay>
      <video src="../assets/v1.mp4" autoplay loop muted class="carousel-image" />
      <video src="../assets/v2.mp4" autoplay loop muted class="carousel-image" />
      <video src="../assets/v3.mp4" autoplay loop muted class="carousel-image" />
      <video src="../assets/v4.mp4" autoplay loop muted class="carousel-image" />
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
  background: #6495f2;
  overflow: hidden;
}

.ant-carousel >>> .slick-slide img {
  display: block;
  margin: auto;
}

.carousel-image {
  width: 100%;
  height: 600px;
}
</style>
