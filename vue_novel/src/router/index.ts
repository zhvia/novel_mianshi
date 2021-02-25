import Vue from 'vue'
import VueRouter, { RouteConfig } from 'vue-router'
import mainComponents from '../views/MainComponents.vue'
import Book from '../components/Book.vue'
import Book_info from '../components/Book_info.vue'
import Chapter from '../components/Chapter.vue'
import SearchInfo from '../components/SearchInfo.vue'
import MyBooks from '../components/Mybooks.vue'
import Book_type from '../components/Book_type.vue'
import MyZone from '../components/MyZone.vue'
// import Home from '../views/Home.vue'
// import Main from './comments/Main.vue'

Vue.use(VueRouter)

// const routes: Array<RouteConfig> = [
//   {
//     path: '/main',
//     name: 'Main',
//     component: Main
//   },
//   {
//     path: '/about',
//     name: 'About',
//     // route level code-splitting
//     // this generates a separate chunk (about.[hash].js) for this route
//     // which is lazy-loaded when the route is visited.
//     component: () => import(/* webpackChunkName: "about" */ '../views/About.vue')
//   }
// ]
    
const routes: Array<RouteConfig> = [
  // 主页路由
  { path: '',
    name: 'index',
    component: mainComponents, 
  },
  // 搜索框路由
  {
    path: '/searchinfo',
    name: 'searchinfo',
    component: SearchInfo,
  },
  // 我的书架路由
  {
    path: '/mybooks',
    name: 'mybooks',
    component: MyBooks,
  },
  // 个人中心
  {
    path: '/myzone',
    name: 'myzone',
    component: MyZone,
  },
  // 小说简介
  { 
    path: '/:book_id',
    component: Book,
    children:[{
    path: '',
    name: 'book_info',
    component: Book_info
    },
  // 小说章节
  {
    path: '/:book_id/:chapter_id',
    name: 'chapter',
    component: Chapter
  },
  // 小说类型
  {
    path: '/type/:book_type',
    name: 'book_type',
    component: Book_type
  },
  ]
  },
  // {
  //   path: '/:book_id/:chapter_id',
  //   name: 'chapter',
  //   component: Chapter
  // },
  // { path: '/3', component: c }
  // { path: '/4', component: d }
]

// { path: '/1', component: mainComponents, children: [
//   {
//     path:'/这个男儿是反派'
//     component: 这个男儿是反派,
//   }
// ]}

const router = new VueRouter({
  mode:'history',
  routes
})

export default router
