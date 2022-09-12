function makeChart(records, id){
  var records = JSON.parse(JSON.parse(records)); //なぜか2回parseしないといけない。意味不明...

  var labels = []
  var score_japanese = []
  var score_math = []
  var score_english = []
  var score_sience = []
  var score_social = []
  var score_avg = []

  for(let i=0; i<records.length; i++){
    labels.push(records[i]['fields']['name']);
    score_japanese.push(records[i]['fields']['score_japanese']);
    score_math.push(records[i]['fields']['score_math']);
    score_english.push(records[i]['fields']['score_english']);
    score_sience.push(records[i]['fields']['score_sience']);
    score_social.push(records[i]['fields']['score_social']);
    avg = (score_japanese[i] + score_math[i] + score_english[i] + score_sience[i] + score_social[i]) / 5
    score_avg.push(avg)
  }


  console.log(score_japanese)

  const ctx = document.getElementById(id).getContext('2d');
  const myChart = new Chart(ctx, {
    type: 'line',
    data: {        
      labels: labels,
      datasets: [{
        label: '国語',
        data: score_japanese,
        borderColor: [ 'rgba(255, 99, 132, 1)',],
        tension: 0.2,
      },{
        label: '数学',
        data: score_math,
        borderColor:['rgba(54, 162, 235, 1)'],
        tension: 0.2,
      },{
        label: '英語',
        data: score_english,
        borderColor:['rgba(153, 102, 255, 1)'],
        tension: 0.2,
      },{
        label: '理科',
        data: score_sience,
        borderColor:['rgba(75, 192, 192, 1)',],
        tension: 0.2,
      },{
        label: '社会',
        data: score_social,
        borderColor:['rgba(255, 206, 86, 1)'],
        tension: 0.2,
      },{
        label: '5教科平均',
        data: score_avg,
        borderColor:['rgba(40, 40, 40, 1)'],
        tension: 0.2,
      }]
    }, 
    options: {
      scales: {
        y: {
          beginAtZero: true,
          suggestedMin: 0,
          suggestedMax: 100,

        }
      }
    }
  })
  return myChart
}
