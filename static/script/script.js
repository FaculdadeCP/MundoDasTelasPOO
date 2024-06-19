

/* Mascara de CPF */
const handleCPF = (event) => {
    let input = event.target;
    input.value = cpfMask(input.value);
}

const cpfMask = (value) => {
    if (!value) return "";
    value = value.replace(/\D/g, ''); // Remove tudo o que não é dígito
    value = value.replace(/(\d{3})(\d)/, "$1.$2");
    value = value.replace(/(\d{3})(\d)/, "$1.$2");
    value = value.replace(/(\d{3})(\d{1,2})$/, "$1-$2");
    return value;
}


/** Validador de CPF */

function validarCPF() {
    const cpfField = document.getElementById('cpf');
    const cpfFeedback = document.getElementById('cpfFeedback');
    let cpf = cpfField.value.replace(/[^\d]+/g, ''); // Remove caracteres não numéricos

    if (cpf.length !== 11 || /^(\d)\1{10}$/.test(cpf)) {
        cpfField.classList.add('is-invalid');
        cpfFeedback.textContent = 'CPF inválido';
        cpfFeedback.style.color = 'red';
        cpfField.setCustomValidity('CPF inválido');
        return false;
    }

    let soma = 0;
    let resto;

    // Calcula o primeiro dígito verificador
    for (let i = 1; i <= 9; i++) {
        soma += parseInt(cpf.substring(i - 1, i)) * (11 - i);
    }
    resto = (soma * 10) % 11;
    if ((resto === 10) || (resto === 11)) {
        resto = 0;
    }
    if (resto !== parseInt(cpf.substring(9, 10))) {
        cpfField.classList.add('is-invalid');
        cpfFeedback.textContent = 'CPF inválido';
        cpfFeedback.style.color = 'red';
        cpfField.setCustomValidity('CPF inválido');
        return false;
    }

    soma = 0;
    // Calcula o segundo dígito verificador
    for (let i = 1; i <= 10; i++) {
        soma += parseInt(cpf.substring(i - 1, i)) * (12 - i);
    }
    resto = (soma * 10) % 11;
    if ((resto === 10) || (resto === 11)) {
        resto = 0;
    }
    if (resto !== parseInt(cpf.substring(10, 11))) {
        cpfField.classList.add('is-invalid');
        cpfFeedback.textContent = 'CPF inválido';
        cpfFeedback.style.color = 'red';
        cpfField.setCustomValidity('CPF inválido');
        return false;
    }

    cpfField.classList.remove('is-invalid');
    cpfFeedback.textContent = 'CPF válido';
    cpfFeedback.style.color = 'green';
    cpfField.setCustomValidity('');
    return true;
}







/* Mascara do RG */

const handleRG = (event) => {
    let input = event.target;
    input.value = rgMask(input.value);
}

const rgMask = (value) => {
    if (!value) return "";
    value = value.replace(/\D/g, ''); // Remove tudo o que não é dígito
    value = value.replace(/(\d{2})(\d)/, "$1.$2");
    value = value.replace(/(\d{3})(\d)/, "$1.$2");
    value = value.replace(/(\d{3})(\d{1,2})$/, "$1-$2");
    return value;
}


/* Macara do celular */

const handlePhone = (event) => {
    let input = event.target
    input.value = phoneMask(input.value)
}

const phoneMask = (value) => {
    if (!value) return ""
    value = value.replace(/\D/g, '')
    value = value.replace(/(\d{2})(\d)/, "($1) $2")
    value = value.replace(/(\d)(\d{4})$/, "$1-$2")
    return value
}

/* Botão de adicionar quantidade de item no carrinho */

document.addEventListener('DOMContentLoaded', function () {
    const decrementButton = document.getElementById('lower');
    const incrementButton = document.getElementById('more');
    const quantityInput = document.getElementById('quantity');

    decrementButton.addEventListener('click', function () {
        let value = parseInt(quantityInput.value);
        if (value > 1) {
            value--;
            quantityInput.value = value;
        }
    });

    incrementButton.addEventListener('click', function () {
        let value = parseInt(quantityInput.value);
        value++;
        quantityInput.value = value;
    });
});


/*   Mascara CEP  */

const handleCEP = (event) => {
    let input = event.target;
    input.value = cepMask(input.value);
}

const cepMask = (value) => {
    if (!value) return "";
    value = value.replace(/\D/g, '');          // Remove tudo o que não é dígito
    value = value.replace(/(\d{5})(\d)/, "$1-$2"); // Adiciona o hífen entre o quinto e sexto dígito
    return value;
}

/* Validação e Preenchimento Automático do Endereço */

document.getElementById('cep').addEventListener('blur', function () {
    let cep = this.value.replace(/\D/g, ''); // Remove tudo que não é dígito
    if (cep.length === 8) {
        fetch(`https://viacep.com.br/ws/${cep}/json/`)
            .then(response => response.json())
            .then(data => {
                if (!data.erro) {
                    // Preenche os campos do formulário com os dados do endereço
                    document.getElementById('logradouro').value = data.logradouro;
                    document.getElementById('bairro').value = data.bairro;
                    document.getElementById('cidade').value = data.localidade;
                    document.getElementById('estado').value = data.uf;
                } else {
                    alert('CEP não encontrado.');
                }
            })
            .catch(error => {
                console.error('Erro ao buscar CEP:', error);
                alert('Erro ao buscar CEP.');
            });
    } else {
        alert('CEP inválido.');
        document.getElementById('logradouro').value = "";
        document.getElementById('bairro').value = "";
        document.getElementById('cidade').value = "";
        document.getElementById('estado').value = "";
    }
});

/** Validação do Formulário de Endereço ao Submeter */

document.getElementById('enderecoForm').addEventListener('submit', function (event) {
    event.preventDefault(); // Impede o envio do formulário

    let cep = document.getElementById('cep').value;
    let logradouro = document.getElementById('logradouro').value;
    let numero = document.getElementById('numero').value;
    let bairro = document.getElementById('bairro').value;
    let complemento = document.getElementById('complemento').value;
    let estado = document.getElementById('estado').value;
    let cidade = document.getElementById('cidade').value;
    let telefone = document.getElementById('telefone').value;

    // Validações básicas
    if (!cep.match(/^\d{5}-\d{3}$/)) {
        alert('CEP inválido. Formato esperado: 00000-000');
        return;
    }

    if (estado.length !== 2) {
        alert('Estado deve ter 2 caracteres.');
        return;
    }

    if (!telefone.match(/^\(\d{2}\) \d{4,5}-\d{4}$/)) {
        alert('Telefone inválido. Formato esperado: (00) 0000-0000 ou (00) 00000-0000');
        return;
    }

    // Se todas as validações passarem, submete o formulário
    alert('Formulário enviado com sucesso!');
    // Aqui você pode enviar o formulário via AJAX ou processá-lo conforme necessário
});


/**  Ver a senha */


/** <!-- Password field -->
Password: <input type="password" value="FakePSW" id="myInput">

<!-- An element to toggle between password visibility -->
<input type="checkbox" onclick="myFunction()">Show Password */
function myFunction() {
    var x = document.getElementById("senha");
    var eyes = document.getElementById("icon");
    if (x.type === "password") {
        x.type = "text";
        eyes.classList.toggle('hide');
    } else {
        x.type = "password";
        eyes.classList.toggle('hide');
    }
}


/** MODAL POP */

document.addEventListener("DOMContentLoaded", function (event) {
    var errorMessage = "{{ error_message }}";
    if (errorMessage.length > 0) {
        var modalBody = document.querySelector('#errorModal .modal-body');
        modalBody.textContent = errorMessage;
        var errorModal = new bootstrap.Modal(document.getElementById('errorModal'), {});
        errorModal.show();
    }
});


/* Mascara de CNPJ */

document.getElementById('cnpj').addEventListener('input', function (e) {
    var value = e.target.value;
    var rawValue = value.replace(/\D/g, ''); // Remove tudo que não é número

    // Verifica se o CNPJ tem 15 dígitos e se o primeiro dígito é '0'
    if (rawValue.length === 15 && rawValue.startsWith('0')) {
        // Verifica se, ao remover o '0', o restante é um CNPJ válido
        var potentialCNPJ = rawValue.substring(1);
        // Atualiza rawValue para o CNPJ sem o '0' inicial
        if (validaCNPJ(potentialCNPJ)) rawValue = potentialCNPJ;
    }

    var cnpjPattern = rawValue
        .replace(/^(\d{2})(\d)/, '$1.$2') // Adiciona ponto após o segundo dígito
        .replace(/^(\d{2})\.(\d{3})(\d)/, '$1.$2.$3') // Adiciona ponto após o quinto dígito
        .replace(/\.(\d{3})(\d)/, '.$1/$2') // Adiciona barra após o oitavo dígito
        .replace(/(\d{4})(\d)/, '$1-$2') // Adiciona traço após o décimo segundo dígito
        .replace(/(-\d{2})\d+?$/, '$1'); // Impede a entrada de mais de 14 dígitos
    e.target.value = cnpjPattern;
});




/**  Valor em moeda 
 * 
 * Exemplo
 * <input type="text" step="0.01" id="valor" name="valor" required placeholder=" " onKeyPress="return(MascaraMoeda(this,'.',',',event))" >
                <label for="valor">Valor</label>
*/

function MascaraMoeda(objTextBox, SeparadorMilesimo, SeparadorDecimal, e) {
    var sep = 0;
    var key = '';
    var i = j = 0;
    var len = len2 = 0;
    var strCheck = '0123456789';
    var aux = aux2 = '';
    var whichCode = (window.Event) ? e.which : e.keyCode;
    if (whichCode == 13 || whichCode == 8) return true;
    key = String.fromCharCode(whichCode); // Valor para o código da Chave  
    if (strCheck.indexOf(key) == -1) return false; // Chave inválida  
    len = objTextBox.value.length;
    for (i = 0; i < len; i++)
        if ((objTextBox.value.charAt(i) != '0') && (objTextBox.value.charAt(i) != SeparadorDecimal)) break;
    aux = '';
    for (; i < len; i++)
        if (strCheck.indexOf(objTextBox.value.charAt(i)) != -1) aux += objTextBox.value.charAt(i);
    aux += key;
    len = aux.length;
    if (len == 0) objTextBox.value = '';
    if (len == 1) objTextBox.value = '0' + SeparadorDecimal + '0' + aux;
    if (len == 2) objTextBox.value = '0' + SeparadorDecimal + aux;
    if (len > 2) {
        aux2 = '';
        for (j = 0, i = len - 3; i >= 0; i--) {
            if (j == 3) {
                aux2 += SeparadorMilesimo;
                j = 0;
            }
            aux2 += aux.charAt(i);
            j++;
        }
        objTextBox.value = '';
        len2 = aux2.length;
        for (i = len2 - 1; i >= 0; i--)
            objTextBox.value += aux2.charAt(i);
        objTextBox.value += SeparadorDecimal + aux.substr(len - 2, len);
    }
    return false;
}

