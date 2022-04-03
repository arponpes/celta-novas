async function fetchData() {
    let response = await fetch('/api/articles_metrics');

    console.log(response.status); // 200
    console.log(response.statusText); // OK

    if (response.status === 200) {
        let data = await response.json();
        renderChart(data);
    }
}


let renderChart = function (data) {
    const ctx = document.getElementById("chart").getContext("2d");
    let labels = []
    let data_values = []
    for (let source in data['articles_by_source']) {
        labels.push(source);
        data_values.push(data['articles_by_source'][source]);
    }

    new Chart(ctx, {
        type: 'bar',
        data: {
            labels: labels,
            datasets: [{
                label: 'Numero de artigos',
                data: data_values,
                backgroundColor: [
                    'rgba(255, 99, 132, 0.2)',
                    'rgba(54, 162, 235, 0.2)',
                    'rgba(255, 206, 86, 0.2)',
                    'rgba(75, 192, 192, 0.2)',
                ],
                borderColor: [
                    'rgba(255, 99, 132, 1)',
                    'rgba(54, 162, 235, 1)',
                    'rgba(255, 206, 86, 0.2)',
                    'rgba(75, 192, 192, 0.2)',
                ],
                borderWidth: 1
            }]
        },
        options: {
            scales: {
                y: {
                    beginAtZero: true
                }
            }
        }
    });
}

fetchData();