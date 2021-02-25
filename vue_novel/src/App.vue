<template>
  <div id="app">
    <el-container>
      <Search></Search>
      <el-header>
        <Title></Title>
      </el-header>
      <el-container>
        <el-aside width="200px">Aside</el-aside>
        <el-container>
        <el-main>
          <router-view v-if="isAlive"/></router-view>
          <!-- <MainComponents></MainComponents> -->
        </el-main>
        <el-footer><Footer></Footer></el-footer>
      </el-container>
    </el-container>
</el-container>
    <!-- <router-view/> -->
  </div>
</template>

<script>
import Title from './components/Title'
import Home from './components/Home'
import Search from './components/search'
import Footer from './components/Footer'
import MainComponents from './views/MainComponents.vue'

export default {
  name: 'app',
  components: {
    Title,
    Home,
    MainComponents,
    Search,
    Footer,
  },
  // 组件重载
  provide(){
    return {
        reload:this.reload
    }
  },
  data() {
    return {
      isAlive: true
    }
  },
  created() {
  },
  methods: {
    reload(){
      this.isAlive = false;
      this.$nextTick(()=>{
          this.isAlive = true;
      })
    }
  },
}
</script>

<style scoped>
 .el-header {
    background-color: #fff;
    color: rgb(5, 4, 4);
    text-align: center;
    line-height: 60px;
  }
  .el-footer{
    background-color: #fff;
    color: rgb(5, 4, 4);
    text-align: center;
    line-height: 50px;
  }
  
  .el-aside {
    background-color: #ffffff;
    color: rgb(12, 11, 11);
    text-align: center;
    line-height: 200px;
  }
  
  .el-main {
    background-color: #ffffff;
    color: rgb(0, 0, 0);
    text-align: center;
    line-height: 160px;
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
</style>
