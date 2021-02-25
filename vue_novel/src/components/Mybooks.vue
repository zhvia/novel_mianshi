<template>
<div id="mybook_div">
  <el-table
    ref="multipleTable"
    :data="mybooks,book_type"
    tooltip-effect="dark"
    style="width: 100%"
    @selection-change="handleSelectionChange">
    <el-table-column
      type="selection"
      width="55">
    </el-table-column>
    <el-table-column
      prop="fields.book_name"
      label="书名"
      width="180">
    </el-table-column>
    <el-table-column
      prop="fields.book_author"
      label="作者"
      width="180">
    </el-table-column>
    <el-table-column
      prop="fields.book_type"
      label="小说类型"
      width="180"
      show-overflow-tooltip>
    </el-table-column>
  </el-table>
  <div style="margin-top: 20px">
    <el-button @click="toggleSelection()">取消选择</el-button>
    <el-button @click="delete_book()">取消收藏</el-button>
  </div>
  </div>
</template>

<script>
  export default {
    data() {
      return {
        mybooks: [],
        multipleSelection: [],
        book_type: {
          1: '玄幻修真',
          2: '仙侠武侠',
          3: '历史军事',
          4: '科幻游戏',
          5: '悬疑灵幻',
          6: '二次元',
          7: '免费',
        },
        book_num: {},
        mybook_key: 0,
      }
    },

    created() {
      this.getMybooks()
    },

    methods: {
      toggleSelection(rows) {
        if (rows) {
          rows.forEach(row => {
            this.$refs.multipleTable.toggleRowSelection(row);
          });
        } else {
          this.$refs.multipleTable.clearSelection();
          
        }
      },
      handleSelectionChange(val) {
        this.multipleSelection = val;
        console.log(this.multipleSelection)
      },

      // 得到图书地址
    getImg(val){
      return 'http://localhost:8000/static/book_images/'+val 
    },

    // 获取当前 token
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

    // 查询用户所有加入到书架里的小说信息
    getMybooks(){
      axios({
        url: '/api/my_books/',
        methods: 'get',
        params:{
          cookie: this.getCookie('token'),
        }
      }).then(res => {
        this.mybooks = res.data

        // 将django中的book_type转成汉字
        for(const b in this.mybooks){
          this.mybooks[b].fields.book_type = this.book_type[this.mybooks[b].fields.book_type]
          
        }
      })
    },

    // 取消小说收藏
    delete_book(){
      if(this.multipleSelection.length != '0' ){
        // 将选定小说的小说id加入到数组中并且传到后端
        for(const book in this.multipleSelection){
          this.book_num[book]  = this.multipleSelection[book].pk
        }
        
        console.log(this.book_num)
        axios({
          url:'/api/delete_mybook/',
          methods:'get',
          params:{
            book_num: this.book_num
          }
        }).then(res => {
          alert('取消成功')
          this.$router.go(0)
        })
      }
      else{
        alert('请选择取消收藏的小说')
      }
    },

    // 刷新页面 
    forceRerender() {

      this.mybook_key += 1; 

    }

    }
    }

    
</script>



<style scoped>
#mybook_div{
  line-height: normal;
  min-height: 500px;
}
</style>