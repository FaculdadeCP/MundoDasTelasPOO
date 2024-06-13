

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

const togglePasswordVisibility = () => {
    const senhaField = document.getElementById('senha');
    const passwordToggleIcon = document.querySelector('.toggle-password i');
    const vIcon = document.getElementById('icon');

    vIcon.classList.remove('Hide');
    if (senhaField.type === 'password') {
        senhaField.type = 'text';
        vIcon.classList.add('hide');
    } else {
        senhaField.type = 'password';
        vIcon.classList.remove('hide');
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


/*  */