<template>
  <div id="book_info_div">
    <el-container>
      <el-main>
      <el-card :body-style="{ padding: '0px' }">
        <div class="img_div">
          <img class="book_img" :src="getImg(book_info.book_img)">
        </div>
        <div class="info_div">
          <h4>{{book_info.book_name}}</h4>
          <span>{{book_info.book_author}}</span>
          <p>{{book_info.book_info}}</p>
          <div class="button_div">
            <el-button type="primary" @click="startRead()"  round>开始阅读</el-button>
            <el-button  type="primary"  v-if="isOnBook" disabled round>已在书架</el-button>
            <el-button type="primary" v-else @click="addmybook()"  round>加入书架</el-button>
          </div>
        </div>
        </el-card>
        <hr>
        <router-view></router-view>
        <el-card>
        <ul class="chapter_ul" >
          <li v-for="chapter_info in chapters" :key="chapter_info.id">
            <router-link :to="{name:'chapter',params: {book_id: book_id, chapter_id: chapter_info.pk}}">{{chapter_info.fields.chapters}}</router-link>
            <img v-if="chapter_info.fields.chapter_types=='2'" style="width:5%" src="http://localhost:8000/static/image/vip.jpg">
          </li>
        </ul>
        </el-card>
      </el-main>
    </el-container>
  </div>
</template>

<script>
export default {
  name: 'book_info',
  created(){
    this.get_book_info()
    this.isOnBooks()
  },
  data() {
    return {
      book_id: this.$route.params.book_id,
      book_img: '',
      book_info: [],
      chapters: [],
      isOnBook: false,
    }
  },
  methods: {
    // 找到点击的书的信息章节
    get_book_info(){
      axios({
      url: '/api/chapter/',
      method: 'get',
      params: {
        book_id: this.book_id,
      }
      }).then((res) => {
        this.book_info = res.data.book[0].fields
        this.chapters = res.data.book_chapter
      })
    },

    // 判断小说是否已经加入书架 
    isOnBooks(){
      axios({
        url: '/api/is_on_book/',
        method: 'get',
        params: {
          book_id: this.book_id,
          cookie: this.getCookie('token')
        },
      }).then(res=>{
        if(res.data === 'true'){
          this.isOnBook = true
          console.log('yes')
        }
        else{
          this.isOnBook = false
          console.log(res.data)
        }
      })
    },

    // 得到图书地址
    getImg(val){
      return 'http://localhost:8000/static/book_images/'+val 
    },

    // 点击加入书架按钮 将该本小说加入到书架
    addmybook(){
      axios({
        url: '/api/add_book/',
        method:'get',
        params:{
          book_id: this.book_id,
          cookie: this.getCookie('token')
        },
        
      }).then(res => {
        alert(res.data)
        this.isOnBooks()
      })
    },

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

    // 
    startRead(){
      this.$router.push('2/')
    },

  },
}
</script>

<style scoped>
#book_info_div{
  line-height: normal;
  
}

  .el-header, .el-footer {
    background-color: #fff;
    color: #333;
    text-align: center;
    line-height: normal;
  }
  
  .el-aside {
    background-color: #fff;
    color: #333;
    text-align: center;
    line-height: normal;
  }
  
  .el-main {
    background-color: #fff;
    color: #333;
    text-align: left;
    line-height: 40px;
  }
  
  body > .el-container {
    margin-bottom: 40px;
  }
  
  .el-container:nth-child(5) .el-aside,
  .el-container:nth-child(6) .el-aside {
    line-height: 260px;
  }
  
  .el-container:nth-child(7) .el-aside {
    line-height: 320px;
  }

  .book_img{
    width: 100%;
    height: 100%;
  }



  .el-card{
    text-align: left;
    padding: 10px;
    min-height: 220px;
    margin: 20px;
  }

  .clearfix:before,
  .clearfix:after {
      display: table;
      content: "";
  }
  
  .clearfix:after {
      clear: both
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

  .chapter_ul li{
    width: 32%;
    height:28px;
    line-height:normal;
    white-space:nowrap;
    margin-bottom: 20px;
    display:block;
    float:left;
    text-align: center;
    /* padding-top: 30px;
    margin-top: 30px; */
}

.chapter_ul li a{
    text-decoration: none;  /*去掉a标签下面的横线*/
    text-transform: uppercase;
    color: black;
    font-size: 20px;
}

.chapter_ul li a:hover{
    color: #C4302B;
}

.button_div{
  text-align: left;
  height: 80px;
  margin-top: 50px;
}


</style>