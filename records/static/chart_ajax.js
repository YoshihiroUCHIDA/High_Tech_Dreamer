$(function () {
  var $RecordsChart = $(".records-chart");
  types = []
  $RecordsChart.each( function (){
     types.push(($( this ).attr( "id" )))
  } );

  $.ajax({
    url: $RecordsChart.data("url"),
    success: function (data) {
      for(let i=0; i<$RecordsChart.length; i++){
        var ctx = $RecordsChart[i].getContext("2d");

        var score_japanese = []
        var score_math = []
        var score_english = []
        var score_sience = []
        var score_social = []
        var labels= []

        for(let j=0; j<data["records"].length; j++){
          records = data["records"][j]
          if (records['type'] == types[i]){
            labels.push(records['name']);
            score_japanese.push(records['score_japanese']);
            score_math.push(records['score_math']);
            score_english.push(records['score_english']);
            score_sience.push(records['score_sience']);
            score_social.push(records['score_social']);
          }
        }
        console.log(labels)

        new Chart(ctx, {
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
            }],
            options: {
              responsive: true,
              borderWidth: 1,
              legend: {
                display: false,
              }
            },
            scales: {
              y: {
                beginAtZero: true,
              },
              gridLines: {
                display: false
              }
            }
          }
        });
      }
    },
  });
});
