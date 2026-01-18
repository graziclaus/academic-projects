const btnEsconder = document.getElementById('btnEsconder');
const btnTamanho = document.getElementById('btnTamanho');
const img = document.getElementById('foto');

function esconderImagem() {

    if (img.style.display === 'none') {

        img.style.display = 'block';
        img.style.margin = '20px auto';

    } else {

        img.style.display = 'none';
    
    }
}

function alterarTamanho() {

    if (img.style.width === '250px') {

        img.style.width = '400px';

    } else {

        img.style.width = '250px';
        
    }
}

btnEsconder.addEventListener('click', esconderImagem);
btnTamanho.addEventListener('click', alterarTamanho);
