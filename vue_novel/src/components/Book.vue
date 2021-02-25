<template>
<div>
  <Breadcrumb></Breadcrumb>
  <router-view></router-view>
  </div>
</template>

<script>
import Book_info from '../components/Book_info';
import Breadcrumb from '../components/Breadcrumb';

export default {
  name: 'Book',
  components:{
   Breadcrumb,
  },

}
</script>

<style>

</style>