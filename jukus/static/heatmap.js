const App = {
  data() {
    return {
      heatmap_data: ['燃え上がるほど'],
    }
  },
  compilerOptions: {
    delimiters: ['[[', ']]'],
  },
  methods: {
    getHeatmap(){
      fetch(HEATMAP_URL, {
        method: 'get',
        headers: {
          'Content-Type':  'application/json',
        },
      })
      .then((response) => {
        console.log(response)
        return response.json();
      })
      .then((data) => {
        this.heatmap_data = data;
      })
      .catch(error => {
        console.error('There has been a problem with your fetch operation:', error);
      });
    },
  },
  created() {
    this.getHeatmap();
  },
}

Vue.createApp(App).mount('#heatmap')
