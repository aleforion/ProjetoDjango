function deleteC(op) {
    /*
    Função responsável por deletar Contas e Categorias
     */
    var dataForm = $("#formDeletar").serialize(), _url;
    if (op == 'conta'){
        _url = "/delete/";
    }else{
        _url = "/delete_categoria/";
    }
    $.ajax({
        type: "POST",
        url:_url,
        data: dataForm,
        success: function (ret, status) {
            if(status == 'success'){
              console.log("Sucesso");
            }
            else{
                console.log("Erro");
            }
        }
    });
}

function criarC() {
     /*
    Função responsável por criar Contas e Categorias
     */
    var serializerConta = $('#formConta').serialize();
    $.ajax({
        type: "POST",
        url: "/inserir_conta/",
        data:serializerConta,
        success: function (ret, status) {
            if (status == 'success'){
                console.log(ret);
                console.log("Funcionou");
            }
            else{
                console.log("Error")
            }
        }
    })
}


$(document).ready(function(){
	$('#tabela').empty(); //Limpando a tabela
    var serializeC = $("formConta").serialize()
	$.ajax({
		type:'POST',		//Definimos o método HTTP usado
		dataType: 'json',	//Definimos o tipo de retorno
		url: '',//Definindo o arquivo onde serão buscados os dados
        data: serializeC,
		success: function(dados){
			for(var i=0;dados.length>i;i++){

				//Adicionando registros retornados na tabela
				$('#tabela').append('<tr><td>'+dados.lista_conta[i].descricao+'</td><td>'+dados.lista_conta[i].categoria+'</td><td>'+dados.lista_conta[i].valor+'</td><td>\'+dados.lista_conta[i].vencimento+\'</td></tr>');
			}
		}
	});
});


function idCHidden(id){
     /*
    Função responsável por incrementar o value no hide do modal conta/categoria delete
     */
    idDelete = id;
    document.getElementById('hiddenId').value =idDelete;
    console.log("chamou");
}



