<template>
  <el-container>
  <el-main>
    <h1 style="text-align: center">{{chapter_name}}</h1>
    {{chapter_text}}
    <div  v-if="isRead" style="width:60%; text-align: center;  background-color: #B3C0D1">
      <pre style="margin: 30px ">{{message}}</pre>
    </div>
    
  </el-main>
  <el-footer>
    <el-button type="primary" @click="lastChapter()">上一章</el-button>
    <el-button type="primary" @click="Chapter()">目录</el-button>
    <el-button type="primary" @click="nextChapter()">下一章</el-button>
    </el-footer>
</el-container>
</template>

<script>
export default {
  name: 'chapter',
  data() {
    return {
      book_id: this.$route.params.book_id,
      chapter_id: this.$route.params.chapter_id,
      chapter_name: '',
      chapter_text: '',
      isRead: false,
      message: ''
    }
  },
  created() {
    this.getChapter()
  },
  methods: {
    // 获取图书信息
    getChapter(){
      axios({
        url: '/api/chapter_info/',
        method: 'get',
        params: {
          'book_id': this.book_id,
          'chapter_id': this.chapter_id
        },
        
      }).then(res => {
        console.log(res.data)
        this.chapter_name = res.data.chapter
        this.chapter_text = res.data.text
        this.message = res.data.message
        if(this.message == 'ok'){
          this.isRead = false
        }
        else{
          this.isRead = true
        }
        console.log(this.isRead)
      })
      },

    // 点击下一章 跳转
    nextChapter(){
      this.chapter_id = Number(this.chapter_id)+1
      this.$router.push({params: {book_id: this.book_id, chapter_id: this.chapter_id}})
      this.$router.go(0)
    },

    // 点击上一章跳转
    lastChapter(){
      this.chapter_id = Number(this.chapter_id)-1
      this.$router.push({params: {book_id: this.book_id, chapter_id: this.chapter_id}})
      this.$router.go(0)
    },

    // 点击跳转回目录
    Chapter(){
      this.$router.push({name: 'book_info', params:{book_id:this.$route.params.book_id}})
    }
  },
}
</script>

<style scoped>
 .el-header{
    background-color: #B3C0D1;
    color: #333;
    text-align: center;
    line-height: normal;
    font-size: 18px;
  }
  
  .el-aside {
    background-color: #D3DCE6;
    color: #333;
    text-align: center;
    line-height: 200px;
  }
  
  .el-main {
    background-color: #E9EEF3;
    color: #333;
    text-align: left;
    line-height: 60px;
    font-size: 20px;
    min-height: 1000px;
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

  h1{
    font-size: 19px;
  }
</style>