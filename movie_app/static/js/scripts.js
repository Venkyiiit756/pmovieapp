$(document).ready(function() {
    // Initialize DataTables
    var cityTable = $('#cityTable').DataTable();
    var theaterTable = $('#theaterTable').DataTable();
    var showTable = $('#showTable').DataTable();
    var categoryTable = $('#categoryTable').DataTable();

    // Initialize Chart.js
    var ctx = document.getElementById('cityChart').getContext('2d');
    var cityChart = new Chart(ctx, {
        type: 'bar',
        data: {
            labels: [], // City names
            datasets: [{
                label: 'Total Gross',
                data: [],
                backgroundColor: 'rgba(54, 162, 235, 0.6)',
                borderColor: 'rgba(54, 162, 235, 1)',
                borderWidth: 1
            }]
        },
        options: {
            responsive: true,
            plugins: {
                legend: { position: 'top' },
                title: { display: true, text: 'City-wise Total Gross' }
            },
            scales: {
                y: { beginAtZero: true }
            }
        }
    });

    // Fetch Data Button Click
    $('#fetchDataBtn').click(function() {
        var selectedCities = $('#citySelect').val();
        console.log("Fetch Data button clicked. Selected cities:", selectedCities);

        if (selectedCities.length === 0) {
            alert("Please select at least one city.");
            return;
        }

        // Handle "All Cities" selection
        if (selectedCities.includes('all')) {
            selectedCities = $('#citySelect option').map(function() {
                return $(this).val();
            }).get();
            selectedCities = selectedCities.filter(city => city !== 'all');
            console.log("All cities selected. Total cities:", selectedCities.length);
        }

        // Show loading indicator
        $('#loading').show();

        // Send AJAX POST request to fetch data
        $.ajax({
            url: '/get_data',
            type: 'POST',
            contentType: 'application/json',
            data: JSON.stringify({ cities: selectedCities }),
            success: function(response) {
                console.log("AJAX request successful. Response:", response);

                // Hide loading indicator
                $('#loading').hide();

                // Clear existing data in tables
                cityTable.clear().draw();
                theaterTable.clear().draw();
                showTable.clear().draw();
                categoryTable.clear().draw();

                // Populate City Table
                response.CityData.forEach(function(row) {
                    cityTable.row.add([
                        capitalizeWords(row.City.replace('-', ' ')),
                        row.AvailableTickets,
                        row.TotalTickets,
                        row.BookedTickets,
                        row.TotalGross,
                        row.BookedGross
                    ]).draw(false);
                });

                // Populate Theater Table
                response.TheaterData.forEach(function(row) {
                    theaterTable.row.add([
                        capitalizeWords(row.City.replace('-', ' ')),
                        capitalizeWords(row.Theater),
                        row.Audi,
                        row.ShowTime,
                        row.AvailableTickets,
                        row.TotalTickets,
                        row.BookedTickets,
                        row.TotalGross,
                        row.BookedGross
                    ]).draw(false);
                });

                // Populate Show Table
                response.ShowData.forEach(function(row) {
                    showTable.row.add([
                        capitalizeWords(row.City.replace('-', ' ')),
                        capitalizeWords(row.Theater),
                        row.Audi,
                        row.ShowTime,
                        row.Category,
                        row.AvailableTickets,
                        row.TotalTickets,
                        row.BookedTickets,
                        row.TotalGross,
                        row.BookedGross
                    ]).draw(false);
                });

                // Populate Category Table
                response.CategoryData.forEach(function(row) {
                    categoryTable.row.add([
                        capitalizeWords(row.City.replace('-', ' ')),
                        row.Category,
                        row.AvailableTickets,
                        row.TotalTickets,
                        row.BookedTickets,
                        row.TotalGross,
                        row.BookedGross
                    ]).draw(false);
                });

                // Update Chart
                updateChart(response.CityData);
            },
            error: function(xhr) {
                console.error("AJAX request failed. Status:", xhr.status, "Response:", xhr.responseText);
                // Hide loading indicator
                $('#loading').hide();

                if (xhr.responseJSON && xhr.responseJSON.error) {
                    alert(xhr.responseJSON.error);
                } else {
                    alert("An error occurred while fetching data.");
                }
            }
        });
    });

    // Function to update Chart.js with new data
    function updateChart(cityData) {
        console.log("Updating chart with CityData:", cityData);
        var labels = [];
        var dataPoints = [];

        cityData.forEach(function(row) {
            labels.push(capitalizeWords(row.City.replace('-', ' ')));
            dataPoints.push(row.TotalGross);
        });

        cityChart.data.labels = labels;
        cityChart.data.datasets[0].data = dataPoints;
        cityChart.update();
        console.log("Chart updated successfully");
    }

    // Utility function to capitalize words
    function capitalizeWords(str) {
        return str.replace(/\b\w/g, function(char) { return char.toUpperCase(); });
    }
});
