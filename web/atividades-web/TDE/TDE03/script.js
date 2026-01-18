const url = "https://jsonplaceholder.typicode.com/posts";
const resultado = document.getElementById("resultado");
const btnCarregar = document.getElementById("btnCarregar");
const form = document.getElementById("mini-form");
const tituloForm = document.getElementById("titulo-form");

let posts = [];
let editandoId = null;

// GET
btnCarregar.addEventListener("click", async () => {

    try {

        const resposta = await fetch(url);

        if (!resposta.ok){ throw new Error(`Erro: ${resposta.status}`) };

        const data = await resposta.json();
        posts = data.slice(0, 5); 
        listarPosts();

    } catch (erro) {

        resultado.innerHTML = `<p style="color:red;">${erro.message}</p>`;

    }
});

// READ
function listarPosts() {

    resultado.innerHTML = "";
    posts.forEach(p => {
        const div = document.createElement("div");
        div.classList.add("post");
        div.innerHTML = `
        <h3>${p.title}</h3>
        <p>${p.body}</p>
        <button class="btn-editar" onclick="editarPost(${p.id})">Editar</button>
        <button class="btn-deletar" onclick="deletarPost(${p.id})">Deletar</button>
        `;
        resultado.appendChild(div);
    });
}

// CREATE e UPDATE
form.addEventListener("submit", (e) => {

    e.preventDefault();

    const titulo = document.getElementById("titulo").value.trim();
    const conteudo = document.getElementById("conteudo").value.trim();

    if (!titulo || !conteudo) {
        
        alert("Preencha todos os campos!");
        return;

    }

    if (editandoId) {

        // PUT
        const index = posts.findIndex(p => p.id === editandoId);
        posts[index].title = titulo;
        posts[index].body = conteudo;

        alert(`Post ${editandoId} atualizado com sucesso!`);
        editandoId = null;
        tituloForm.textContent = "Criar Novo Post";

    } else {

        // POST 
        const novoPost = {

            id: Date.now(),
            title: titulo,
            body: conteudo

        };

        posts.unshift(novoPost);
        alert("Post criado com sucesso!");
    }

    form.reset();
    listarPosts();
});

// DELETE (só funciona loclamnte )
function deletarPost(id) {

    posts = posts.filter(p => p.id !== id);
    listarPosts();
    alert(`Post ${id} deletado com sucesso!`);

}

// UPDATE (preenchendo o form)
function editarPost(id) {

    const post = posts.find(p => p.id === id);
    document.getElementById("titulo").value = post.title;
    document.getElementById("conteudo").value = post.body;

    editandoId = id;
    tituloForm.textContent = "Editando Post";
    alert(`Editando post ${id} — altere os campos e clique em "Enviar" para salvar.`);

}
