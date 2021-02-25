<template>
  <el-breadcrumb separator-class="el-icon-arrow-right">
  <el-breadcrumb-item :to="{ path: '/' }">首页</el-breadcrumb-item>
  <el-breadcrumb-item :to="{path: ''}">{{book_name}}</el-breadcrumb-item>
  </el-breadcrumb>
</template>

<script>
import localStorage from '../localStorages/localStorage';

export default {
  name: 'Breadcrumb',
  created() {
   this.test()
  },
  data() {
    return {
       breakcrumbs: [],
       book_id: '',
       book_name: this.$store.state.book_name
    }
  },
  methods: {
    test(){
      this.book_id = this.$route.params.book_id
      var book_info = localStorage.fetch('book_info')
      this.book_name = book_info[this.book_id].fields.book_name
    },
  },  
}
</script>

<style>
 .el-breadcrumb{
    font-size: 20px !important ; 
    line-height: normal !important;
    margin-left: 40px;
  }
</style>