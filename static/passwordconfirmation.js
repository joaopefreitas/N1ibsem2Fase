
function validarSenha() {
    var senhaid = document.getElementById("senhaid"), csenha = document.getElementById("csenha");
    if (senhaid.value != csenha.value) {
        csenha.setCustomValidity("Senhas não são iguais!");
    } else {
        csenha.setCustomValidity('');
    }
}
senhaid.onchange = validarSenha;
csenha.onkeyup = validarSenha;
