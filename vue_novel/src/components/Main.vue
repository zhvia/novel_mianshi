// 主页的小说简介
<template>
  <div>
  <el-row>
    <el-col :span="8" v-for="book in book_infos" :key="book.id">
      <el-card :body-style="{ padding: '0px' }">
        <div class="img_div">
          <img :src="getImg(book.fields.book_img)" class="image">
        </div>
        <div class="book_info_div" >          
          <router-link class="book_name" :to="{ name:'book_info',params: { book_id: book.pk}}"><h4>{{book.fields.book_name}}</h4></router-link>
          <p>{{book.fields.book_author}}</p>
          <p >{{book.fields.book_info | ellipsis}}</p>
        </div>
      </el-card>
    </el-col>
  </el-row>
  <div class="block">
    <el-pagination
      @size-change="handleSizeChange"
      @current-change="handleCurrentChange"
      :current-page="page"
      :page-sizes="[ 6, 9, 12]"
      :page-size="6"
      layout="total, sizes, prev, pager, next, jumper"
      :total="all_book">
    </el-pagination>
  </div>
  </div>
</template>

<script>
import localStorage from '../localStorages/localStorage';
export default {
  name: 'Main',
  data() {
    return {
      page: 1,
      per_page: 6,
      all_book_infos: [],
      book_infos: [],
      all_book: 0,
    }
  },
  
  created() {
    this.search()

  },
 
  methods: {
    // 找到当前 token
    getCookie(name){
      name = name + "="
      var start = document.cookie.indexOf(name),
          value = null;
      if(start>-1){
          var end = document.cookie.indexOf(";",start);
          if(end == -1){
              end = document.cookie.length;
          }
          value = document.cookie.substring(start+name.length,end);
      }
      return value;
    },

    // 查询小说  显示再首页
    async search(){
      // 接口
      const { data: res } = await this.$axios.get("/api/");
      this.$store.commit('changeBookInfo', res)
      // this.all_book_infos = res;
      this.all_book = this.$store.state.book_infos.length
      
      this.all_book_infos = res
      this.book_infos = this.all_book_infos.slice((this.page-1)*this.per_page, this.page*this.per_page)
      localStorage.save('book_info', res)
    },
    
   

     handleSizeChange(val) {
        this.per_page = val
        console.log(this.per_page)
        this.handleCurrentChange(this.page)
      },

    // 切换当前页显示当前小说
    handleCurrentChange(val) {
      this.page = val
      this.book_infos = this.all_book_infos.slice((this.page-1)*this.per_page, this.page*this.per_page)
     
    },

    // 得到图片的地址

    getImg(val){
      return 'http://localhost:8000/static/book_images/'+val 
    },


    },

  // 限制小说信息长度
  filters:{
    ellipsis (value) {
      if (!value) return '' //如果没有返回空
      if (value.length > 40) {
        return value.slice(0,40) + '...' //长度大于10的后面用......代替
      }
      return value
    }
    },

    } 


</script>

<style scoped>
.el-row{
  line-height: normal;
}

 .time {
    font-size: 13px;
    color: #999;
  }
  

  .image {
    width: 100%;
    display: inline;
  }

 

  .el-col{
    float: left;
    width: 33%;
  }

  .el-card{
    text-align: left;
    padding: 10px;
    min-height: 220px;
    margin: 20px;
  }

  .img_div{
    width: 30%;
    height: 100%;
    padding-top: 20px;
    float: left;
  }

  .book_info_div{
    width: 60%;
    float: left;

    margin-left: 30px;
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

 
</style>
