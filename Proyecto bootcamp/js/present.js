let dataCSV = [];

document.getElementById('csvFileInput').addEventListener('change', function (e) {
    const file = e.target.files[0];
    if (!file) return;
    Papa.parse(file, {
        header: true,
        dynamicTyping: true,
        complete: function (results) {
            dataCSV = results.data;
            renderTable(results.data);
        }
    });
});

function renderTable(data) {
    const table = document.getElementById("csvTable");
    if (!data.length) return;
    table.innerHTML = "";

    const headers = Object.keys(data[0]);
    const headerRow = table.insertRow();
    headers.forEach(h => {
        const th = document.createElement("th");
        th.textContent = h;
        headerRow.appendChild(th);
    });

    data.forEach(row => {
        const tr = table.insertRow();
        headers.forEach(h => {
            const td = tr.insertCell();
            td.textContent = row[h];
        });
    });
}