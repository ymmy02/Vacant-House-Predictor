<template>
  <div id="app">
    <header class="header">
      <h1>空き家判別機</h1>
    </header>
    <Predictor />
  </div>
</template>

<script>
import Predictor from './components/Predictor.vue';

export default {
  name: 'app',
  components: {
    Predictor
  }
}
</script>

<style>
.header {
  padding: 10px 0 10px 0;
  color: #fafdff;
  background-color: #4e454a;
  text-align: center;
}
</style>
