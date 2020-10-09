<template>
  <div>
    {{ msg }}
  </div>
</template>

<script>

export default {
  name: 'Ping',
  data() {
    return {
      msg: 'hello world!'
    }
  },
  beforeMount(){
    alert("hello")
  }
}
</script>
