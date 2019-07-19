

var dataurl='/data';
var dataval;
$.ajax({
    method: 'GET',
    url: dataurl,
    success: function(data)
    {
        console.log(data);
        dataval=data;
       
    },
    error : function(er){
        console.log("error",er);
    }

});


window.onload= function()
{
    var ctx = document.getElementById('chart');
    var myChart = new Chart(ctx, {
        type: 'line',
        data: {
            labels: ['Politics','Non-Political','AskIndia', "[R]eddiquette", 'Science/Technology', 'Policy/Economy', 'Business/Finance', 'Scheduled', 'Sports', 'Food', 'Photography'],
            datasets: [{
                label: '# of Votes',
                data: dataval['upvote'],
                backgroundColor:
                    'rgba(255, 115, 0,0.1)',
                borderColor:
                    'rgb(255, 115, 0)',
                borderWidth: 1
            },
        ]
        },
        options: {
            title: {
                display: true,
                text :"No. of Upvotes for each Flair"
            },
            scales: {
                yAxes: [{
                    ticks: {
                        beginAtZero: true
                    }
                }]
            }
        }
    });

    

    var ctx2 = document.getElementById('chart2');
    var myChart2 = new Chart(ctx2, {
        type: 'line',
        data: {
            labels: ['Politics','Non-Political','AskIndia', "[R]eddiquette", 'Science/Technology', 'Policy/Economy', 'Business/Finance', 'Scheduled', 'Sports', 'Food', 'Photography'],
            datasets: [{
                label: '# of Comments',
                data: dataval['comment'],
                backgroundColor:
                    'rgba(0, 0, 0,0.1)',
                borderColor:
                    'rgb(0, 0, 0)',
                borderWidth: 1
            }]
        },
        options: {
            title: {
                display: true,
                text : "No of Comments for each Flair"
            },
            scales: {
                yAxes: [{
                    ticks: {
                        beginAtZero: true
                    }
                }]
            }
        }
    });

}
