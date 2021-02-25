<template>
<div id="search_div">
  <el-form :inline="true" class="demo-form-inline">
  <el-form-item label="查询书籍">
    <el-input v-model="book_info" placeholder="请输入书名或作者"></el-input>
  </el-form-item>
  <el-form-item>
    <el-button type="primary" @click="onSubmit">查询</el-button>
  </el-form-item>
</el-form>
</div>
</template>

<script>
  export default {
    inject:['reload'],
    data() {
      return {
        book_info: '',
      }
    },
    methods: {
      onSubmit() {
        this.$router.replace({name: 'searchinfo', query:{'book_info': this.book_info}}).catch(console.error())
        // 重新加载并且清空搜索框
        this.reload()
        this.book_info = ''
      }
    }
  }
   
</script>

<style scoped>
#search_div{
  margin-top: 20px;
  text-align: center;
}

.el-form-item__label{
  font-size: 16px;
}
</style>