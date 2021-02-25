
const storage = {
   fetch(key){
      return JSON.parse(window.localStorage.getItem(key) || '[]')
   },
   save(key, items){
    window.localStorage.setItem(key, JSON.stringify(items))
   }

}
 
export default storage;