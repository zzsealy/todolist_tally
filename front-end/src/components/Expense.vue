<template>
  <div>

      <label for="">花费：</label>
      <input v-model="expense" type="text"> <br>
      <laabel>类别：</laabel>
      <input v-model="category" type="text"><br>
      <button @click="submit" class="btn btn-default">增加</button>

  <li v-for="expense in allExpense" v-bind:key="expense.category" >
    {{ expense }}
  </li>
    <p>hello</p>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'Expense',
  data() {
    return {
      expense:'',   // 花费
      category: '',  //类别
      allExpense: '',
      path:'http://localhost:8000/api/expenses/'
    }
  },
  methods: {
    getallExpense() {
      axios.get(this.path)
          .then((res) => {
            this.allExpense = res.data.results;
            // var user_url = [];
            for (let i = 0; i < res.data.results.length; i++) {
              var url = res.data.results[i].user;
              console.log(url);
            }
            console.log(this.allExpense);
          })
          .catch((error) => {
            console.log(error)
          })
    },
    submit(){
      console.log(document.cookie);
      let data = {'expense':this.expense, 'category':this.category}
      axios.post(this.path, data)
          .then((res) => {
          console.log(res);
        })
    }
  },
  created(){
    this.getallExpense();
  }
}
</script>