document.addEventListener("DOMContentLoaded", function() {
    var ctx1 = document.getElementById("lineChart").getContext("2d");
    var lineChart = new Chart(ctx1, {
        type: "line",
        data: {
            labels: ["0 Hours", "1 Hours", "2 Hours", "3 Hours", "4 Hours", "5 Hours", "6 Hours", "7 Hours", "8 Hours"],
            datasets: [{
                label: "Appointments",
                data: [300, 400, 450, 500, 530, 600, 700, 800, 950],
                borderColor: "#20c997",
                backgroundColor: "rgba(32, 201, 151, 0.2)",
                fill: true,
                tension: 0.4
            }]
        }
    });

    var ctx2 = document.getElementById("barChart").getContext("2d");
    var barChart = new Chart(ctx2, {
        type: "bar",
        data: {
            labels: ["11/03/2025", "12/03/2025", "13/03/2025", "14/03/2025", "15/03/2025", "16/03/2025", "17/03/2025", "18/03/2025", "19/03/2025", "20/03/2025"],
            datasets: [{
                label: "Appointments Booked",
                data: [4200, 4300, 2900, 2700, 4000, 5200, 6300, 6100, 5400, 5800],
                backgroundColor: "rgba(54, 162, 235, 0.6)",
                borderColor: "#36A2EB",
                borderWidth: 1
            }]
        }
    });
});
