<template>
  <div>
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
      allExpense: ''
    }
  },
  methods: {
    getallExpense() {
      const path = 'http://localhost:8000/api/expenses/'
      axios.get (path)
        .then((res) => {
          this.allExpense = res.data.results;
          // var user_url = [];
          for(let i=0; i<res.data.results.length; i++) {
           var url = res.data.results[i].user;
           console.log(url);
          }
          console.log(this.allExpense);
        })
        .catch((error) => {
          console.log(error)
        })
    }
  },
  created(){
    this.getallExpense();
    alert('Jinlaile')
  }
}
</script>