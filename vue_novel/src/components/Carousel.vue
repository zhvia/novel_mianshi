// 首页轮播图

<template>
  <el-carousel :interval="4000" type="card" height="280px">
    <el-carousel-item v-for="item in this.imgs" :key="item">
      <img :src="item" class="imgs">
    </el-carousel-item>
  </el-carousel>
 
</template>

<script>
export default {
  name: 'Carousel',
  data() {
    return {
     imgs: [
    'https://readx-her-1252317822.image.myqcloud.com/boss/5120_pc%20%281%29.jpg',
    'https://bossaudioandcomic-1252317822.image.myqcloud.com/activity/document/0818c32b25f4585b3cdc5eec69f9394b.jpg',
    'https://bossaudioandcomic-1252317822.image.myqcloud.com/activity/document/12e213d2b3f1f4f79537f321956fb847.jpg',
    'https://bossaudioandcomic-1252317822.file.myqcloud.com/activity/document/841ecd66d86b15f8cb3b4976ce621cff.JPG'
  ]  
    }
  },
 
}
</script>

<style scoped>
  .el-carousel__item h3 {
    color: #475669;
    font-size: 16px;
    opacity: 0.75;
    line-height: 160px;
    margin: 0;
  }


  .el-carousel__item:nth-child(2n) {
    background-color: #99a9bf;
  }
  
  .el-carousel__item:nth-child(2n+1) {
    background-color: #d3dce6;
  }

  .imgs{
    width: 100%;
    height: 100%;
  }

  
</style>