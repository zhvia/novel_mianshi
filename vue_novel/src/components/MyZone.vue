<template>
  <div id="myzone_div">
    <h3>个人中心</h3>
    <el-form ref="form" :model="form" label-width="50px" size="large">
      <el-form-item label="昵称:">
      <el-input v-model="form.username"></el-input>
    </el-form-item>
      <el-form-item label="性别:">
        <el-select v-model="form.gender" placeholder="请选择您的性别">
          <el-option label="男" value="1"></el-option>
          <el-option label="女" value="2"></el-option>
          <el-option label="保密" value="3"></el-option>
        </el-select>
      </el-form-item>
      <el-form-item label="地址:">
        <el-select v-model="form.address" placeholder="请选择您的住址">
          <el-option label="安徽" value="1"></el-option>
          <el-option label="湖南" value="2"></el-option>
          <el-option label="上海" value="3"></el-option>
          <el-option label="北京" value="4"></el-option>
        </el-select>
      </el-form-item>
      <el-form-item size="large">
        <el-button type="primary" @click="onSubmit">立即创建</el-button>
        <el-button>取消</el-button>
      </el-form-item>
    </el-form>
  </div>
</template>

<script>
export default {
  name: 'Myzone',
  data() {
    return {
      login_btn: '编辑',
      dialogFormVisible: false,
      isChange: true,
      isread: true,
      form: {
        username: '',
        gender:'',
        phone: '',
        address: '',
        delivery: false,
        cookie: this.getCookie('token')
      },
       
    };
  },
  created() {
    if(this.getCookie('token')){
    this.getInfo()
    }
  },
  methods: {
    getInfo(){
      axios({
        method: 'get',
        url: '/api/my_zone/',
        params: {
          cookie: this.getCookie('token')
        },
      }).then(res => {
        // console.log(res.data)
        this.form.username = res.data['name']
        this.form.gender = res.data['gender']
        this.form.phone = res.data['phone']
        this.form.address = res.data['address']
      })
    },

    // 更改用户信息
    changeInfo(){
      axios({
        method: 'post',
        url: '/api/my_zone/',
        data: {
          'info': this.form
        }
      }).then(res => {
        this.isread = true
        alert('修改信息成功')
      })
    },

    // 点击编辑按钮切换按钮属性
    edit(){
      this.isChange = false
      this.isread = false
    },


        // 获取cookie
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
  },
}
</script>

<style scoped>
  #myzone_div{
    width: 100%;
    height: auto;
    text-align: center;
  }
 .el-form{
   width: 60%;
   height: auto;
 }
 .el-input__inner{
   width: 30%;
   text-align: left;
 }
</style>