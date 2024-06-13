

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


/*     */