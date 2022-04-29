const colors = {
    'TOTAL': 'rgb(54, 162, 235)',
    'MARCA': 'rgb(255, 107, 107)',
    'MOI CELESTE': 'rgb(255, 217, 61)',
    'FARO DE VIGO': 'rgb(107, 203, 119)',
    'LA VOZ DE GALICIA': 'rgb(77, 150, 255)',
}


async function fetchData() {
    let response = await fetch('/api/articles_metrics');

    if (response.status === 200) {
        let data = await response.json();
        renderChartArticlesBySource(data);
        renderChartArticlesByWeekDay(data)
        renderChartArticlesByMonthDay(data)
        document.getElementById('total_articles').innerHTML = data['total_articles'] | "-";
        document.getElementById('articles_trend').innerHTML = data['article_creation_trend'] | "-";
    }
}


let renderChartArticlesBySource = function (data) {
    const ctx = document.getElementById("chart_articles_by_source").getContext("2d");
    let labels = []
    let data_values = []
    for (let source in data['articles_by_source']) {
        labels.push(source);
        data_values.push(data['articles_by_source'][source]);
    }

    new Chart(ctx, {
        type: 'doughnut',
        data: {
            labels: labels,
            datasets: [{
                label: 'Total',
                data: data_values,
                backgroundColor: [
                    colors['MARCA'],
                    colors['MOI CELESTE'],
                    colors['FARO DE VIGO'],
                    colors['LA VOZ DE GALICIA'],
                ],
            }]
        },
        options: {
            responsive: true,
            plugins: {
                legend: {
                    position: 'top',
                },
                title: {
                    display: true,
                    text: 'Numero de artigos por fonte'
                }
            }
        },
    });
}


let renderChartArticlesByWeekDay = function (data) {
    const ctx = document.getElementById("chart_articles_by_week_day").getContext("2d");
    let labels = []
    let dataValuesTotal = []

    for (date of data['articles_last_week_by_date']) {
        labels.push(date['created_at__date']);
        dataValuesTotal.push(date['count']);
    }
    let dataSets = [{
        label: 'Total',
        data: dataValuesTotal,
        borderColor: colors['TOTAL'],
        borderWidth: 1
    }]

    for (const [source, dataData] of Object.entries(data['articles_last_week_by_date_by_source'])) {
        let sourceData = []
        for (date of dataData) {
            sourceData.push(date['count'])
        }
        let dataSet = {
            label: source,
            data: sourceData,
            borderWidth: 1,
            borderColor: colors[source]
        }
        dataSets.push(dataSet);
    }

    new Chart(ctx, {
        type: 'line',
        data: {
            labels: labels,
            datasets: dataSets
        },
        options: {
            responsive: true,
            tension: 0.3,
            plugins: {
                legend: {
                    position: 'top',
                },
                title: {
                    display: true,
                    text: 'Numero de artigos por dia da semana'
                }
            }
        },
    });
}

let renderChartArticlesByMonthDay = function (data) {
    const ctx = document.getElementById("chart_articles_by_month_day").getContext("2d");
    let labels = []
    let dataValuesTotal = []

    for (date of data['articles_last_year_by_date_by_source']) {
        labels.push(moment(date['month']).format('MMMM, YYYY'));
        dataValuesTotal.push(date['total']);
    }
    let dataSets = [{
        label: 'Total',
        data: dataValuesTotal,
        borderColor: colors['TOTAL'],
        borderWidth: 1
    }]


    new Chart(ctx, {
        type: 'line',
        data: {
            labels: labels,
            datasets: dataSets
        },
        options: {
            responsive: true,
            tension: 0.3,
            plugins: {
                legend: {
                    position: 'top',
                },
                title: {
                    display: true,
                    text: 'Numero de artigos por mes'
                }
            }
        },
    });
}

window.addEventListener("load", function () {
    fetchData();
});