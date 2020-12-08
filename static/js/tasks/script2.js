import * from './vue.js';

Vue.component('display-tasks', {
      data: function () {
        return {
        count: 0,
        list: ["Egor", "Alisa", "Tolik"]
        }
      },
      template: '<ul><li v-for="item in list">{{item}}</li></ul>'
    })

    Vue.component('add-task', {
      data: function () {
        return {
        count: 0,
        list: ["Egor", "Alisa", "Tolik"]
        }
      },
      template:
        `<form method="get">
          <input type="text" name="taskname" required placeholder="Название задачи">
          <button type="submit"></button>
        </form>`
    })

    out = new Vue({
      el: '#output',
      data: {
        display: false,
        add: false,
      }
    })

    menu = new Vue({
      el: '#menu',
      data: {
        content : "hf",
        count: 0,
      },
      methods:{
        display_tasks(){
          out.add = false;
          out.display = true;
        },
        search_task(){
          alert("2");
        },
        add_task(){
          out.display = false;
          out.add = true;
        },
        edit_task(){
          alert("4");
        },
        delete_task(){
          alert("5");
        },
        restart_task(){
          alert("6");
        }
      }
   })