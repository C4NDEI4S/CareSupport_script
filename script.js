// script.js

document.addEventListener('DOMContentLoaded', function () {
    // URL do arquivo CSV no GitHub (usando caminho relativo)
    const csvUrl = 'seu-arquivo.csv';

    // Função para buscar e exibir o arquivo CSV
    async function fetchAndDisplayCSV() {
        try {
            const response = await fetch(csvUrl);
            const data = await response.text();
            const rows = data.split('\n');
            const table = document.getElementById('csvTable');

            // Preencha a tabela com os dados do CSV
            rows.forEach(row => {
                const cells = row.split(',');
                const tr = document.createElement('tr');

                cells.forEach(cell => {
                    const td = document.createElement('td');
                    td.textContent = cell;
                    tr.appendChild(td);
                });

                table.appendChild(tr);
            });
        } catch (error) {
            console.error('Erro ao buscar o arquivo CSV:', error);
        }
    }

    // Chame a função para buscar e exibir o CSV
    fetchAndDisplayCSV();
});
