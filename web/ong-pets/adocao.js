const filtros = document.querySelectorAll('.filtro-opcoes li');
const inputNome = document.getElementById('buscar-nome');
const pets = document.querySelectorAll('.pets-disponiveis');

let filtroFalso = 'todos';

function atualizarPets() 
{

    const texto = inputNome.value.toLowerCase();

    pets.forEach(pet => 
    {

        const nomePet = pet.querySelector('h2').textContent.toLowerCase();
        const idPet = pet.id.toLowerCase();
        const filtragem = (filtroFalso === 'todos' || idPet.includes(filtroFalso));

        const nomeExiste = nomePet.includes(texto);

        if(filtragem && nomeExiste) 
        {

            pet.style.display = 'flex';
            pet.style.flexDirection = 'column';

        } 
        
        else{

            pet.style.display = 'none';

        }
    });
}

filtros.forEach(filtro => 
{

    filtro.addEventListener('click', () => 
    {

        filtroFalso = filtro.id.toLowerCase();
        atualizarPets();

    });
});

inputNome.addEventListener('input', () =>
{

    atualizarPets();
    
});

document.getElementById('encontre-h2').addEventListener('click', function() {
document.getElementById('encontrei').scrollIntoView({ behavior: 'smooth', block: 'start' });
});
