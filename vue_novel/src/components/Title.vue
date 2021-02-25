<template>
  <el-menu
  :default-active="activeIndex2"
  class="el-menu-demo"
  mode="horizontal"
  @select="handleSelect"
  background-color="#fff"
  text-color="black"
  active-text-color="#ffd04b">
  <el-menu-item style="margin-left: 30vw" index="/">首页</el-menu-item>
  <el-submenu index="2">
    <template slot="title">分类</template>
    <el-menu-item index="#">玄幻修真</el-menu-item>
    <el-menu-item index="#">二次元</el-menu-item>
    <el-menu-item index="#">仙侠武侠</el-menu-item>
    <el-menu-item index="#">历史军事</el-menu-item>
    <el-menu-item index="#">科幻游戏</el-menu-item>
    <el-menu-item index="#">悬疑灵幻</el-menu-item>
  </el-submenu>
  <el-menu-item index="#">书库</el-menu-item>
  <el-menu-item index="#">排行</el-menu-item>
  <el-menu-item index="#">完本</el-menu-item>
  <el-menu-item index="#">免费</el-menu-item>
  <el-menu-item index="#">作家专区</el-menu-item>
  <Myzone></Myzone>
  <Login></Login>
  <el-button ref="mybook_btn" type="text"  @click="myBook()" >我的书架</el-button>
  <el-button ref="myzone_btn" type="text"  @click="myZone()" >个人中心</el-button>
</el-menu>
</template>

<script>
import Login from '../components/Login'
import MyZone from '../components/MyZone'
import Mybooks from '../components/Mybooks';
export default {
  name: 'Home',
  components: {
    Login,
    MyZone,
    Mybooks
  },
  data() {
        return {
          activeIndex: '1',
          activeIndex2: '1',
          
        };
      },
      methods: {
        handleSelect(key, keyPath) {
          this.$router.push(key)
          // console.log(key, keyPath);
          console.log(this.$route.path);
        },

        
        // 跳转到我的书架
        myBook(){
          this.$router.push('/mybooks')
        },
        // 跳转到个人中心
        myZone(){
          this.$router.push('/myzone')
        }
      }
}
</script>

<style scoped>
.el-menu-item{
    font-size: 16px;
    text-align: center
}


</style>