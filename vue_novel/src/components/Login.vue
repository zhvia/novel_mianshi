<template>
<div id="login_div">
    <el-button ref="logout_btn" type="text" v-if="isLogin"  @click="logout()" >注销</el-button>
    <el-button ref="login_btn" type="text" v-else @click="dialogFormVisible = true" >登陆</el-button>
    <!-- 登陆弹窗 -->
    <el-dialog  title="登陆" :visible.sync="dialogFormVisible" @opened='open()' width='35%'>
      <el-form :model="this.form" ref="form">
        <span ref="msg" style="color: red; font-size=18px"></span>
        <el-form-item label="用户名"  :label-width="formLabelWidth" prop="username">
          <el-input maxlength="10" @blur="login_check_username()" v-model="form.username" autocomplete="off"></el-input>
        </el-form-item>
        <el-form-item label="密码"  :label-width="formLabelWidth" prop="password">
          <el-input @blur="login_check_psw()" v-model="form.password" maxlength="14" type=password autocomplete="off"></el-input>
        </el-form-item>
        <el-form-item label="验证码" :label-width="formLabelWidth" prop="code">
          <el-input v-model="form.code" maxlength="4" type=text autocomplete="off"></el-input>
          <img :src="form.img_url" @click="changeCode" class="code_img">
        </el-form-item>    
      </el-form>
      <!-- 注册弹窗 -->
      <el-dialog  title="注册" :visible.sync="dialogFormVisibleRegiter" @opened='open'  width='35%'>
      <el-form :model="this.form" ref="form">
        <span ref="msg" style="color: red; font-size=18px"></span>
        <el-form-item label="用户名" :label-width="formLabelWidth" prop="username">
          <el-input maxlength="10"  @blur="check_username()" v-model="register_form.username" autocomplete="off"></el-input>
        </el-form-item>
        <el-form-item label="密码" :label-width="formLabelWidth" prop="password">
          <el-input v-model="register_form.password" @blur="check_psw()" maxlength="14" type=password autocomplete="off"></el-input>
        </el-form-item>
        <el-form-item label="确认密码"  :label-width="formLabelWidth" prop="password">
          <el-input v-model="register_form.repassword" @blur="check_psw()" maxlength="14" type=password autocomplete="off"></el-input>
        </el-form-item>
        <el-form-item label="验证码" :label-width="formLabelWidth" prop="code">
          <el-input v-model="register_form.code" maxlength="4" type=text autocomplete="off"></el-input>
          <img :src="form.img_url" @click="changeCode" class="code_img">
        </el-form-item>    
      </el-form>
      <div slot="footer" class="dialog-footer">
        <el-button @click="dialogFormVisibleRegiter = false">离开</el-button>
        <el-button type="primary" @click="register()"  round>注册</el-button>
      </div>
      </el-dialog>
    <!-- <Checkcode></Checkcode> -->
      <div slot="footer" class="dialog-footer">
        <el-button @click="dialogFormVisible = false">离开</el-button>
        <el-button type="primary" @click="login()"  round>登录</el-button>
        <el-button type="primary" @click="dialogFormVisibleRegiter=true"  round>注册</el-button>

      </div>
    </el-dialog>
    
    </div>
</template>

<script>
import { Dialog } from 'element-ui';
import { mapState } from 'vuex'
// import Checkcode from '../components/Checkcode'
export default {
  components: {
  },
  name: 'login',
  
  data() {
    return {
      dialogFormVisibleRegiter: false,
      dialogFormVisible: false,
      isLogin: false,
      isLegal: false,
      form: {
        username: '',
        password: '',
        code: '',
        delivery: false,
        img_url: '/api/img/',
      },
      register_form: {
        username: '',
        password: '',
        repassword: '',
        code: '',
        delivery: false,
        img_url: '/api/img/',
      },
      formLabelWidth: '120px'
    };
  },
  mounted() {
    this.checkLogin() 
  },
  methods: {
    // 打开dialog前清除数据  并且更新验证码
    open(){
      this.$refs.form.resetFields();
      this.fileComponet=false;
      this.form.img_url = this.form.img_url + '?'
    },

    // 检验注册时输入内容的合法性
    check_psw(){
      if (this.register_form.password.length>=4){
        if(this.register_form.password != this.register_form.repassword && this.register_form.repassword != ''){
          this.$refs.msg.innerHTML='两次密码不一致'
          this.isLegal = false  
        }
        else{
          this.$refs.msg.innerHTML='' 
          var pattern = new RegExp("[`~!@#$^&*=|{}':;',\\[\\]<>《》/?~！@#￥……&*|{}【】‘；：”“'。，、？' ']");
          if (pattern.test(this.register_form.password)){
            this.$refs.msg.innerHTML='密码不可以使用非法字符'
            this.isLegal = false  
          }
          else{
            this.isLegal = true
          }
        }
      }
      else{
        this.$refs.msg.innerHTML='密码必须在4-14位'
        this.isLegal = false  
      }
    },

    // 检验注册用户名合法性
    check_username(){
      var pattern = new RegExp("[`~!@#$^&*=|{}':;',\\[\\]<>《》/?~！@#￥……&*|{}【】‘；：”“'。，、？' ']");
      var username = this.register_form.username
      if(username.length>=4)
        if (pattern.test(this.register_form.username)){
          this.$refs.msg.innerHTML='用户名不可以使用非法字符'
          this.isLegal = false  
        }
        else{
          this.isLegal = true
        }
      else{
        this.$refs.msg.innerHTML='用户名必须在4-14位'
      }
    },

    // 检验登陆用户名合法性
    login_check_username(){
      var pattern = new RegExp("[`~!@#$^&*=|{}':;',\\[\\]<>《》/?~！@#￥……&*|{}【】‘；：”“'。，、？' ']");
      var username = this.form.username
      if(username.length>=4)
        if (pattern.test(username)){
          this.$refs.msg.innerHTML='用户名不可以使用非法字符'
          this.isLegal = false  
        }
        else{
          this.isLegal = true
        }
      else{
        this.$refs.msg.innerHTML='用户名必须在4-14位'
      }
    },

    // 检验登陆时输入内容的合法性
    login_check_psw(){
      if (this.form.password.length>=4){
        this.$refs.msg.innerHTML='' 
        var pattern = new RegExp("[`~!@#$^&*=|{}':;',\\[\\]<>《》/?~！@#￥……&*|{}【】‘；：”“'。，、？' ']");
        if (pattern.test(this.form.password)){
          this.$refs.msg.innerHTML='密码不可以使用非法字符'
          this.isLegal = false  
        }
        else{
          this.isLegal = true
        } 
      }
      else{
        this.$refs.msg.innerHTML='密码必须在4-14位'
        this.isLegal = false  
      }
    },

    // 注册窗口打开时自动更新验证码
    register_open(){
      this.$refs.form.resetFields();
      this.fileComponet=false;
      this.register_form.img_url = this.register_form.img_url + '?'
    },

    // 登陆 注销按钮的切换
    checkLogin(){
      // console.log(this.getCookie('token'))
      if(this.getCookie('token')){
        this.isLogin = true
      }
    },
    // 注销实现
    logout(){
      axios.get('/api/logout/').then(res => {
        // console.log(res.data)
        this.isLogin = false
      })
    },
    // 用户登录 
    login(){
      if(this.isLegal){
        axios({
          method: 'post',
          url: '/api/login/',
          data: {
            username: this.form['username'],
            password: this.form['password'],
            code: this.form['code'],
            cookies: document.cookie,
          }
          }).then((result) => {
              // 根据返回值来执行操作
              console.log(result)
              if (result.data == 'suc'){
                this.dialogFormVisible = false
                this.checkLogin()
              }
              else{
                alert(result.data)
                this.form.img_url = this.form.img_url + '?'
              }}).catch((err) => {
                alert('loginfail')
                });
      }
      else{
        alert('请检查输入内容')
      }
    },
    
    // 注册实现
    register(){
      if(this.isLegal){
        axios({
          url: '/api/register/',
          method: 'post',
          data:{
            username: this.register_form['username'],
            password: this.register_form['password'],
            code: this.register_form['code'],
            cookies: document.cookie,
          }
        }).then(res => {
          if (res.data == 'suc'){
                this.dialogFormVisibleRegiter = false

              }
          else{
            alert(res.data)
            this.register_form.img_url = this.register_form.img_url + '?'
            }
        }).catch(
          (err) => {
                alert('registerfail')
                }
                )
      }
      else{
        alert('请检查您的输入')
      }
    },
    
    //  验证码刷新
    changeCode(){
      console.log(this.form.img_url)
      this.form.img_url = this.form.img_url + '?'
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
};

</script>

<style scoped>
.dialog-footer{
  text-align: center;
}

.el-input{
  width: 300px;
}

#login_div{
  width: 80px;
  float: right;
}

.code_img{
  position: absolute;
  right: 0;
  height: 40px;
}
</style>