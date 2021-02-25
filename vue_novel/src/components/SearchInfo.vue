<template>
  <div id="search_info_div">
  <el-card class="search_card" :body-style="{ padding: '0px' }" v-if="book_info.length>0"  v-for="book in book_info" :key="book_info.pk">
    <div class="img_div">
      <router-link :to="{ name:'book_info',params: { book_id: book.pk}}"><img class="book_img" :src="getImg(book.fields.book_img)"></router-link>
    </div>
    <div class="info_div">
      <router-link class="book_name" :to="{ name:'book_info',params: { book_id: book.pk}}"><h4>{{book.fields.book_name}}</h4></router-link>
      <span>{{book.fields.book_author}}</span>
      <p>{{book.fields.book_info}}</p>
    </div>
  </el-card>
  <el-card v-else>
    <h4>你搜索的内容不存在</h4>
  </el-card>
  </div>
</template>

<script>
export default {
  data() {
    return {
      book_info: [],
    }
  },
  created() {
    this.searchInfo()
  },
  methods: {
    // 搜索内容返回结果
    searchInfo(){
      axios({
          method: 'get',
          url: '/api/search/',
          params:{
            bookinfo: this.$route.query.book_info
          }
        }).then(res => {
          this.book_info = res.data.book_name
          // this.book_info.push(res.data.book_author)
          console.log(this.book_info)
          console.log(this.book_info.length)
        })
    },

    // 获取图片
    getImg(val){
      return 'http://localhost:8000/static/book_images/'+val 
    },
  },
}
</script>

<style scoped>
  #search_info_div{
    min-height: 500px;
  }

  .el-card{
    line-height: normal;
    text-align: left;
  }

   .img_div {
    float: left;
    width: 13%;
    height: 100%;
    margin: 20px;
  }

  .info_div{
    float: left;
    width: 80%;
    /* margin-top: 20px; */
    margin-left: 20px;
    padding-top: 20px;
  }

    .book_name{
    text-decoration: none;  /*去掉a标签下面的横线*/
    text-transform: uppercase;
    color: black;
    font-size: 16px;
  }

  .book_name :hover{
    color: red;
  }

  .search_card{
    margin-bottom: 5px;
  }
</style>