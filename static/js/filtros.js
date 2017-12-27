function filtroFormConta() {
     /*
    Função responsável por filtrar as contas do formulário
     */
    var input, filter, table, tr, td, i;
    input = document.getElementById("inputFormConta");
    if (input[0] == ""){

    }
    filter = input.value.toUpperCase();
    table = document.getElementById("tableFormConta");
    tr = table.getElementsByTagName("tr");
    for (i = 0; i < tr.length; i++) {
        td = tr[i].getElementsByTagName("td")[0];
        if (td) {
            if (td.innerHTML.toUpperCase().indexOf(filter) > -1) {
                tr[i].style.display = "";
            } else {
                tr[i].style.display = "none";
            }
        }
    }
}

function filtroDropCategoria(op) {
     /*
    Função responsável por filtrar as categorias do formulario
     */
    var filter, table, tr, td, i;
    console.log(op);
    console.log('Funcionou');
    filter = op.toUpperCase();
    console.log(filter);
    table = document.getElementById("tableFormConta");
    tr = table.getElementsByTagName("tr");
    for (i = 0; i < tr.length; i++) {
        td = tr[i].getElementsByTagName("td")[1];
        if (td) {
            if (td.innerHTML.toUpperCase().indexOf(filter) > -1) {
                tr[i].style.display = "";
            } else {
                tr[i].style.display = "none";
            }
        }
    }
}