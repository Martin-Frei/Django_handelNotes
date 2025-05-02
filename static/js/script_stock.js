function loadStockData() {
    fetch('/get_stock_data/')
        .then(response => response.json())
        .then(data => {
            document.getElementById('appel_stock').textContent = data.appel_stock;
            document.getElementById('google_stock').textContent = data.google_stock;
            document.getElementById('microsoft_stock').textContent = data.microsoft_stock;
        });
}


loadStockData();


setInterval(loadStockData, 5000);